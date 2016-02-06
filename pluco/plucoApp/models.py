#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#Usuario, contiene una instancia del usuario que ofrece django
class UserProfile(models.Model):
     # Usa una instancia de User de contrib auth models
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    email = models.EmailField(max_length=30,help_text="dirección email")
    address = models.CharField(max_length=30,help_text="dirección postal")
    picture = models.ImageField(upload_to='media', blank=True)

    # Return the user, for a request.user
    def getUser():
        return self

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
