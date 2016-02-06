#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext, loader
from plucoApp.forms import userForms,UserProfileForm
from plucoApp.models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from unidecode import unidecode

def index(request):
    if request.user.is_authenticated():
        registered = True
        try:
            us = UserProfile.objects.get(user=request.user)
            #data = User.objects.get(username=request.user.username)
            return render(request, 'perfil.html',{'user': us})
        except:
            us = False
    else:
        us = False
    return render(request, 'hijo.html',{'user': us})

def about(request):
    if request.user.is_authenticated():
        registered = True
        try:
            us = UserProfile.objects.get(user=request.user)
        except:
            us = False
            return render(request, 'about.html',{'user': us})
    else:
        us = False
    return render(request, 'about.html',{'user': us})

def contact(request):
      return render(request,'contact.html')

@login_required
def user_profile(request):
    registered = True
    try:
        us = UserProfile.objects.get(user=request.user)
    except:
        us = False
    return render(request,'perfil.html',{'user' : us})

def register(request):
    if request.method == 'POST':  # If the form has been submitted...
        #creamos el formulario de doble password
        #creamos el formulario completo de email etc
        form = UserCreationForm(request.POST)
        profile = UserProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            user = form.save()  # Save new user attributes and get the user in the return

            profile = profile.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            else:
                picture = "anonymous.png"
                profile.picture = picture
            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            #Como el formulario se supone valido procedemos a una vez guardado el usuario logearlo directamente
            username = request.POST.get('username')
            password = request.POST.get('password1')
            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)
            login(request, user)
            #Pasamos una variable para que marque el registro como correcto
            return HttpResponseRedirect('/perfil',{'registered': True})  # Redirect after POST
    else:
        form = UserCreationForm()
        profile = UserProfileForm()
    return render_to_response('register.html', {'user_form': form,'profile_form': profile}, context_instance=RequestContext(request))



""" Editar perfil """
@login_required
def user_editData(request):
    registered = True
    #Si se ha enviado un formulario
    if request.POST:
        user = User.objects.get(username=request.user.username)
        user.username=request.POST.get('username')

        #Comprobamos que ambas contraseñas sean correctas
        if request.POST.get('password')!= "" and request.POST.get('password')==request.POST.get('password2'):
            user.set_password(request.POST.get('password'))
            modified = True
        user.save()

        #obtenemos el usuario
        userProfile = UserProfile.objects.get(user=request.user)
        #obtenemos email
        userProfile.email=request.POST.get('email')
        #Quitamos las tildes de la direccion
        address = unidecode(request.POST["address"])
        userProfile.address = address

        #Comprobamos que exista foto
        if 'picture' in request.FILES:
            userProfile.picture = request.FILES.get('picture',"")

        #Guardamos los datos
        userProfile.save()

        #mostramos el perfil
        return render(request,'perfil.html',{'user': userProfile,'update': True})

    else:
        try:
            us = UserProfile.objects.get(user=request.user)
            return render(request, 'editar.html',{'user': us})
        except:
            return render(request, 'editar.html')


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/perfil')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Cuenta inactiva, cierra sesión automático")
        else:
            # Bad login details were provided. So we can't log the user in.
            # If the user exists, but the password is incorrect, exists = True
            try:
                (User.objects.get(username=username))
                exists = True
            except:
                exists = False
            return render(request,'errorUser.html',{'error': exists})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def user_address(request):
    return render(request,'address.html')
