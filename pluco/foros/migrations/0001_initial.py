# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idComment', models.IntegerField()),
                ('title', models.CharField(help_text=b'T\xc3\xadtulo del comentario, asunto', unique=True, max_length=128)),
                ('commentText', models.TextField(help_text=b'Introduce aqu\xc3\xad tu comentario', max_length=500)),
                ('date', models.DateField()),
                ('likes', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'T\xc3\xadtulo de la hebra o foro nuevo', unique=True, max_length=128)),
                ('theme', models.CharField(help_text=b'Tema', unique=True, max_length=50)),
                ('asignature', models.CharField(help_text=b'asignature', unique=True, max_length=25)),
                ('visits', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('firstName', models.CharField(max_length=25)),
                ('secondName', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='theme',
            field=models.ForeignKey(to='foros.Forum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(to='foros.User'),
        ),
    ]
