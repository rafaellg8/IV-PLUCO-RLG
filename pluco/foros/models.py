#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.forms import ModelForm
from django.contrib.auth.models import User

#Modelo Foros
class Forum(models.Model):
      title = models.CharField(max_length=128,help_text="Título de la hebra o foro nuevo",unique=True)
      theme = models.CharField(max_length=50,help_text="Tema",unique=True)
      asignature = models.CharField(max_length=25,help_text="asignature",unique=True)
      visits = models.IntegerField(default=0)
      slug = models.SlugField()

      def save(self, *args, **kwargs):
          # Uncomment if you don't want the slug to change every time the name changes
          #if self.id is None:
          #self.slug = slugify(self.name)
          self.slug = slugify(self.theme)
          super(Forum, self).save(*args, **kwargs)

      def __unicode__(self):
            return self.title

#Comentarios
class Comment(models.Model):
      """docstring for Comment"""
      """temas, idComentario (número comentario)
      título, comentario, usuario que hace el comentario,
      url donde el usuario pone la url de su archivo a compartir si procede"""
      theme = models.ForeignKey(Forum)
      idComment = models.IntegerField(null=False)
      title = models.CharField(max_length=128,help_text="Título del comentario, asunto",unique=True)
      commentText = models.TextField(max_length=500,help_text="Introduce aquí tu comentario")
      username = models.ForeignKey(User)
      date = models.DateField()
      likes = models.IntegerField(null=True,default=0)
      #url = models.URLField(blank=True)

      def __unicode__(self):
            return self.title
