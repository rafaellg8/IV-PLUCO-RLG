#Desplegar aplicación en un PaaS -- Heroku


###Despliegue de App
Para la realización de esta práctica he usado el PaaS [Heroku](www.heroku.com). Nos registramos en Heroku previamente.
Después, procederemos a crear la app en python en Heroku, para ello seguimos los pasos del [tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app):
Con esto crearemos una app con una plantilla asociada y un repositorio asociado.
1. Creamos la app, con:
```
heroku login
```
```
heroku create
git push heroku master
```
2. Una vez creada la app, vemos que funciona correctamente, abrimos de forma local con:
```
heroku open
```
3. Una vez vemos que funciona, pasamos todos los archivos de nuestro repositorio a la carpeta que contiene la app de heroku, en mi caso creo una carpeta llamada plucorlg donde dentro está todo el código de este repositorio.
4. Renombramos la app:
```
heroku apps:rename plucorlg
```
5. Configuramos los archivos **Procfile** y **requirements.txt**
**Procfile**
Contiene la ejecución de la app a través de gunicorn
```
web: gunicorn plucorlg.index:app --log-file -
```

**Requirements.txt**
Contiene los archivos y módulos a instalar para la ejecución correcta de la aplicación:
```
dj-database-url==0.3.0
Django==1.8.1
django-postgrespool==0.3.0
gunicorn==19.3.0
psycopg2==2.6
SQLAlchemy==1.0.4
whitenoise==1.0.6
```

En mi caso por ejemplo necesito usar entre otros **Flask**, **WTForms** para los formularios y **PyMongo** para las bases de datos en MongoDB.

Añadimos a git, y hacemos **push heroku master** y ya tenemos la app funcionando en heroku: [APP](http://plucorlg.herokuapp.com/)

![imgHeroku](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20144056_zpsdk0rzibr.png)

Directamente también podemos hacer lo siguiente sobre nuestro repositorio de github:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV$ cd IV-PLUCO-RLG/
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ git init
Reinitialized existing Git repository in /home/rafaellg8/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG/.git/
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ heroku apps:create plucorlg
Creating plucorlg... done, stack is cedar-14
https://plucorlg.herokuapp.com/ | https://git.heroku.com/plucorlg.git
Git remote heroku added
heroku buildpacks:set heroku/python
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ git remote remove heroku
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ git remote add heroku git@heroku.com:plucorlg.git
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ git push heroku master
```
La única parte que puede no ser tan intiutiva es lo del buildpack, que crea uno específico para el lenguaje python en heroku.


Al final en el Makefile, hemos añadido unas líneas para su despliegue automático:

```
heroku:
	sudo apt-get install wget
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	cd ..
	sudo heroku login
	sudo heroku create
	sudo git add .
	sudo git commit -m "heroku despliegue remoto"
	sudo git push heroku master
	sudo heroku run python manage.py syncdb --noinput
	sudo heroku ps:scale web=1
```
