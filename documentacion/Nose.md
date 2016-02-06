#Testeando PLUCO-RLG en NOSE

###Para los test he usado la herramienta NOSE
Es una herramiena para Python.

Código en python:
```
def test():
      forum = addForum('Ayuda','Tema de Ayuda','HELP')

      testingUser = addUser('testingUser','Testing','Testing firstname',
            'Testing SecondName','0001-01-01','testing@mail.com','password','Granada, España')

      #añadimos ahora el testing user y el forum como una clave externa a comentarios
      addComment(forum,1,'Testeando','Testeando un comentario',testingUser,datetime.date.today())

      for f in Forum.objects.all():
            for c in Comment.objects.all():
                  print "- {0} - {1} - {2} -{3}".format(str(f), str(c),c.username,c.commentText)


```

Más info sobre el archivo [testingPluco.py](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/testingPluco.py)


Arrancamos el servidor, y comprobamos que pasa el test y funciona completamente todo.

Subimos todo a git-hub para que travis detecte los cambios:
```
rafaellg8: ~/IV-PLUCO-RLG $ git push origin master
Username for 'https://github.com': rafaellg8
Password for 'https://rafaellg8@github.com':
Counting objects: 10, done.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 870 bytes | 0 bytes/s, done.
Total 6 (delta 2), reused 0 (delta 0)
To https://github.com/rafaellg8/IV-PLUCO-RLG
   d6801b7..f1e2559  master -> master
```

Ejecución de los tests con **make test**:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ make test
cd pluco && nosetests test/testingPluco.py
/usr/local/lib/python2.7/dist-packages/django/contrib/sites/models.py:78: RemovedInDjango19Warning: Model class django.contrib.sites.models.Site doesn't declare an explicit app_label and either isn't in an application in INSTALLED_APPS or else was imported before its application was loaded. This will no longer be supported in Django 1.9.
  class Site(models.Model):

.
----------------------------------------------------------------------
Ran 1 test in 0.254s

OK

```
