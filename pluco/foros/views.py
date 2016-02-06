#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.template import RequestContext
from foros.models import Comment,Forum
from plucoApp.models import User
from django.http import HttpResponse
from plucoApp.forms import Forums,Comments,userForms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Max
import datetime

@login_required
def showComments(request,slug):
    #obtenemos el foro asociado a un tema
    #Hemos cambiado los campos tema por slug, que es el tema en forma slugify, ej: tema-de-prueba
    form = Forum.objects.get(slug=slug)
    #Obtenemos el tema asociado al foro, filtrado por slug
    theme = form.theme
    #filtramos comentarios de un foro con un tema, ordenados por la fecha más reciente
    comForm = Comment.objects.filter(theme=form).order_by('-date')

    if request.method =="POST":
        idC = 0
        com = Comment.objects.order_by('-idComment')[:1]
        for c in com:
            idC = c.idComment+1

        com = Comments(request.POST)

        username = request.user
        f = get_object_or_404(Forum,slug=slug)
        #validamos el formulario
        if com.is_valid():
            comment = Comment()
            comment.theme = f
            comment.idComment = idC
            comment.username = username
            comment.commentText = request.POST["commentText"]
            comment.title = request.POST["title"]
            comment.date = datetime.date.today()

            comment.save()

            return redirect("/foros/theme/"+slug,{'com': comForm,})
    else:
        com = Comment.objects.order_by('-idComment')[:1]
        for c in com:
            idC = c.idComment+1
        com = Comment()

    context = {'com': comForm,'commentForm':com,'theme': theme}
    return render(request,'comentarios.html',context)

#Funcion que muestra los foros
@login_required
def showForums(request):
    #obtenemos todos los foros
    com = Forum.objects.all()
    context = {'forum': com}

    #si se hace un POST, se crea el formulario para añadir foro
    if request.method =="POST":
        form = Forums(request.POST)
        #validamos el formulario
        if form.is_valid():
            newForum = Forum()
            newForum.title = request.POST["title"]
            newForum.theme = request.POST["theme"]
            newForum.asignature = request.POST["asignature"]
            #guardamos los datos del foro
            newForum.save()

            return redirect("/foros")
        else:
            print form.errors
    #si no se hace POST, se crea el foro y se renderiza la página donde se muestran los foros
    else:
        form = Forum()
    return render(request,'foros.html', {'forum': com,'form': form})

"""
Aumenta el número de visitas cada vez que se muestran los comentarios
"""
@login_required
def numberVisits(request,slug):
    #Obtener el foro por tema, en la forma slug
    f = get_object_or_404(Forum,slug=slug)
    f.visits = f.visits+1
    f.save()

    return showComments(request,slug)

"""
Obtener número visitas de los comentarios
"""
def getVisits (request):
    f = Forum.objects.all()
    i=0
    dataTheme = []
    dataVisits = []
    for forum in f:
        dataTheme.append(forum.theme)
        dataVisits.append(forum.visits)

    data = {'theme': dataTheme,'visits': dataVisits}

    return JsonResponse(data, safe=False)


@login_required
def comment(request,theme):
    if request.method =="POST":
        idC = 0
        com = Comment.objects.order_by('-idComment')[:1]
        for c in com:
            idC = c.idComment+1


        com = Comments(request.POST)

        username = request.user
        f = get_object_or_404(Forum,theme=theme)
        #validamos el formulario
        if com.is_valid():
            comment = Comment()
            comment.theme = f
            comment.idComment = idC
            comment.username = username
            comment.commentText = request.POST["commentText"]
            comment.title = request.POST["title"]
            comment.date = datetime.date.today()
            comment.save()

            return (showComments(request,theme))
        else:
            print comm.errors
    else:
        com = Comment.objects.order_by('-idComment')[:1]
        for c in com:
            idC = c.idComment+1
        com = Comment()

    return render(request,'comentarios.html',{'commentForm':com})

@login_required
def ForumSlug(request, theme_slug):
    #Creamos el contexto que vamos a enviar
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        #Obtenemos el comentario
        forum = Forum.objects.get(slug=theme_slug)
        print theme_slug
        #Pasamos el tema al contexto
        context_dict['theme'] = forum.theme
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        comment = Comment.objects.filter(theme=forum)

        # Adds our results list to the template context under name pages.
        context_dict['comment'] = comment
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['forum'] = forum
        return render(request, 'foros.html', context_dict, RequestContext(request))
    except Forum.DoesNotExist:
        return HttpResponseRedirect("/")
        # We get here if we didn't find the specified category.

"""
Vista que controla los botones "LIKE"
Recibe idCom que es el comentario asociado, con su clave primaria por la que están ordenados que es idComment.
Aumenta la visita y guarda el comentario otra vez.
"""
@login_required
def like_comment(request):
    context = RequestContext(request)
    if request.method == 'GET':
        com_id = request.GET.get('idCom')
        #No encuentra la categoria
    likes = 0
    if com_id:
        #obtenemos el comentario con la id asociada que hemos recibido
        comment = Comment.objects.get(idComment=int(com_id))
        if comment:
            likes = comment.likes + 1
            comment.likes =  likes
            comment.save()
    return HttpResponse(likes)

"""
Crea un foro, con su formulario correspondiente para que el usuario lo relleno con sus datos asociados.
"""
@login_required
def forums(request):
    if request.method =="POST":
        form = Forums(request.POST)
        #validamos el formulario
        if form.is_valid():
            newForum = Forum(request.POST["title"],request.POST["theme"],request.POST["asignature"])
            return render(request,'foros.html', {'form': form},context_instance=RequestContext(request))
    else:
        form = Forum()
    return render(request,'foros.html', {'form': form},)
