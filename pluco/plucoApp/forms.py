#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pluco.settings')

import django
django.setup()

from plucoApp.models import UserProfile
from foros.models import Comment,Forum
from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.db import models
from django.contrib import admin
from easy_maps.widgets import AddressWithMapWidget

#Formulario de los usuarios
class userForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#Formulario datos extra para los usuarios
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email','address', 'picture')

    def addUser(username,firstname,email,password,address,picture):
          u = UserProfile.objects.get_or_create(username=username,first_name=firstname,email=email,password=password,address=address,picture=picture)[0]
          u.save()
          return u

#Comentarios
class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title','commentText',)

    def addComment(self,forum,idC,tit,commentTxt,user,url,date):
          com = Comment.objects.get_or_create(theme=forum,idComment=idC,title=tit,commentText=commentTxt,username=user,date=date)
          com.save()
          return com

class Forums(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title','theme','asignature',)

    def addForum(self,title,theme,asignature):
                forum = Forum.objects.get_or_create(title=title,theme=theme,asignature=asignature)[0]
                forum.save()
                print ("Guardamos el foro")
                return forum
