# IV-PLUCO-RLG

##Proyecto PLUCO - Red Social PLUCO

==
Rafael Lachica Garrido
[![Build Status](https://travis-ci.org/rafaellg8/IV-PLUCO-RLG.svg?branch=master)](https://travis-ci.org/rafaellg8/IV-PLUCO-RLG)
[![Shippable](https://img.shields.io/shippable/561d708d1895ca44741d9f63.svg)](https://app.shippable.com/projects/561beb831895ca44741d2a7b)
[![Build Status](https://snap-ci.com/rafaellg8/IV-PLUCO-RLG/branch/master/build_image)](https://snap-ci.com/rafaellg8/IV-PLUCO-RLG/branch/master)
[<img src="http://azuredeploy.net/deploybutton.png" alt="Azure" height=32>](http://pluco.cloudapp.net/)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://plucorlg.herokuapp.com/)

#INFRAESTRUCTURA VIRTUAL

#PLATAFORMA UNIVERSITARIA DE COMPARTICIÓN DE CONOCIMIENTOS: PLUCO

###Introducción

Plataforma académica de compartición de archivos de la Universidad de Granada, y que permita la colaboración en grupo entre los usuarios del sistema. Añade servicios de mensajería y foros,potenciando la interacción de los usuarios, y agrupando a los mismos por varios grupos de o bien asignaturas o cursos.

###Seguridad

En cuanto a la seguridad de nuestra plataforma los objetivos son: Permitir tener un sistema seguro en el que se separen datos sensibles y credenciales de los usuarios, y por otra parte archivos de los mismos. Por otra parte tendremos una web con foros que si es atacada no compremete la privacidad de los usuarios ni sus archivos.

###Infraestuctura
####Red Social PLUCO####
En la parte que realizaré, mi propósito viene a ser implementar una red social en la que los usuarios puedan participar en la compartición
del conocimiento y apoyo en problemas que puedan surgir en las asignaturas o tareas determinadas.
Tendremos los usuarios asociados, donde los podremos agrupar por grupos de asignaturas o cursos,etc.
Para ello implementaré un sistema web en Azure, con un servidor al que se conectarán los usuarios y hará de frontend,
y que contendrá la información de asignaturas asociadas a cada usuario, foros en los que participa, información de los usuarios.
Todo está información estará en una base de datos independiente que a su vez, se complementará con la base de datos general
que creará mi compañero con información más exhaustiva.


El resto de mis compañeros deberán crear:

   1. Un sistema de gestión de datos de usuarios, mediante una base de datos que se gestionará por MySQL. Dicho sistema permitirá recuperar la información de los usuarios,consultar sus datos asociados. Además la gestión permitirá modificar los datos y los procesos asociados a dar de alta o baja de los usuarios.
   2. Un sistema de almacenamiento sftp de recursos en la nube, que se usaraá para la organización, administración y compartición de archivos. Todo esto irá implementado en otro servidor que usaremos de Cloud Storage, además de un sistema de acceso a los datos y recursos por parte de los usuarios.

Al final del proyecto, deberemos enlazar en conjunto las tres partes del proyecto, y realizar el despliegue correcto.

[Apuntados en el proyecto de software libre de la oficina OSL](http://osl.ugr.es/bases-de-los-premios-a-proyectos-libres-de-la-ugr/)

==
#Integracion Continua

Para la integración continúa usaré el [Shippable](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/Shippable.md) y  [Travis](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/Travis.md)

Si quiere más info puede consultar la configuración de los archivo Makefile del proyecto donde se llaman a los test y se ejecutan la aplicación. [más info](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/Makefile)


#Configuracion
Para la configuración voy a usar un archivo makefile que generará los tests pertinentes, la documentación y por último ejecutará la aplicación. Aquí dejo un fragmento de mi Makefile, el cual llama al archivo testing pluco para procesar los test y pone a funcionar la app y su despliegue automático.

```
#Makefile autor: Rafael Lachica Garrido
test:
	cd pluco && python testingPluco.py

#Desplegar toda la app en Azure a través de vagrant y ansible
#virtual box añadir
despligue:
  sudo sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian trusty contrib" >> /etc/apt/sources.list.d/virtualbox.list'
  sudo apt-get install -y dkms linux-headers-generic
  sudo apt-get update --fix-missing
  sudo apt-get install -y nodejs-legacy
  sudo apt-get install -y npm
  sudo npm install -g azure-cli
  sudo apt-get install -y python-pip python-dev
  sudo pip install paramiko PyYAML jinja2 httplib2 ansible

#Instalar Vagrant
  wget https://releases.hashicorp.com/vagrant/1.8.1/vagrant_1.8.1_x86_64.deb
  sudo dpkg -i  vagrant_1.8.1_x86_64.deb

  sudo apt-get install -y --force-yes virtualbox-5.0 dkms
  sudo apt-get install -y fabric
  sudo apt-get install -y virtualbox-dkms

#añadimos la caja de azure
  $(MAKE) box

#instalamos la máquina en vagrant
  vagrant plugin install vagrant-azure
  cd VagrantAzure && sudo vagrant up --provider=azure

provisionar:
	sudo vagrant provision

  test:
  	cd pluco && nosetests test/testingPluco.py

  run:
  	nohup python pluco/manage.py runserver 0.0.0.0:8000 &

  ```

#Tests
Los tests se generarán directamente desde el archivo [testingPluco](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/pluco/testingPluco.py).
Este archivo lo único que hace es crear un usuario,y a su vez un comentario y un foro.
De manera que nos queda
**Foro de prueba**
-- **Comentario de prueba** por parte del **Usuario de Prueba**

Todo el test se ejecuta automáticamente desde el [Makefile](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/Makefile), el cual llamará a **NOSETESTS** que ejecutará la batería de tests.

Para los test usaré la herramienta [Nose](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/Nose.md)

#Despligue de la app en el PaaS HEROKU

Para la realización de esta práctica he usado el PaaS Heroku.
Detalles sobre el despligue en [Heroku](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/IntegracionHeroku.md). Con esto podremos tener nuestra app alojada en Heroku y desplegar la app de forma remota. Resultado del despliegue tenemos la app desplegada en [pluco](http://pluco.herokuapp.com/)

## Configuración del despliegue de la app, testeando remotamente y integración continúa en Travis y Shippable

Para esto podremos elegir desde Heroku que queremos hacer a la hora del despliegue. Esto es útil porque podemos elegir que testee antes de desplegar la app, y que lo haga en el caso de que no tenga errores.
Para esto, he usado las herramientas de Shippable y Travis para que pasen los tests de integración continúa, usando para ello la herramienta SNAP-CI, donde podemos usar pipelines y los configuramos para que pase los test y después despliegue, aquí vemos el resultado:
![snapci3](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20182633_zpsw6dm8lds.png)

Para más información consulte el [enlace](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/integracionContinuaSnap.md)

#Migrando la app de Flask a Django

Para ello, he usado el framework Django y he actualizado y creado varias aplicaciones que se interelacionen entre ellas.
La principal es la app **Pluco** a la que se conectan las 2 siguientes:
1. PlucoApp: manejo de gestión de usuarios y acceso a los distintas funciones de la web.
2. Foros: manejo de los foros y comentarios que hacen los usuarios.

[Más info](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/DJANGO-P4-5-6.md)

#Probando la app en el entrono de pruebas Docker

[Docker]([Docker](https://www.docker.com/))
Como dice el eslogan de Docker, es una plataforma distribuida de aplicaciones para el desarrollo y administración de sistemas.

Hemos creado un entorno para probar la app, que funcione todo correctamente y generar ahí varios tests durante el desarrollo.

###Dockerfile
Para el correcto funcionamiento de docker, necesitamos un archivo de configuracion de [Docker](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/Dockerfile).

En mi caso contiene lo siguiente el Dockerfile:

```
FROM ubuntu:14.04

#Autor
MAINTAINER Rafel Lachica Garrido <rafaellg8@correo.ugr.es>

#Actualizamos e instalamos cosas
RUN sudo apt-get update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN sudo apt-get install
RUN sudo apt-get install -y git
RUN sudo apt-get install -y libpq-dev
RUN sudo apt-get install -y python-setuptools
RUN sudo git clone https://github.com/rafaellg8/IV-PLUCO-RLG.git
RUN ls -l
RUN cd IV-PLUCO-RLG/
#Ejecutamos la instalación de make que llama a requeriments.txt y ejecuta la app
RUN cd IV-PLUCO-RLG/ && git init && git pull
RUN cd IV-PLUCO-RLG/ && ls -l
RUN cd IV-PLUCO-RLG/ && sudo make -f Makefile install
RUN cd IV-PLUCO-RLG/ && make -f Makefile run
```
Segumimos el [tutorial](http://docs.docker.com/mac/started/) y sus respectivos pasos.

Accedemos a la web de [Docker Hub](https://hub.docker.com/) y nos registramos.

Creamos una "AutomaticBuild" para nuestra imagen, de nuestro repositorio y linkamos nuestro repo de github con Docker.

Tras hacer un push nos queda lo siguiente:
![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-08%20000916_zpshnkfr7qz.png)

...

[Detalles de Docker y más info sobre mi configuración](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/Docker.md)
[Imagen de PLUCO en Docker](https://hub.docker.com/r/rafaellg8/iv-pluco-rlg/)


#Despligue remoto de la app: [Fabric](http://www.fabfile.org/)

Se trata de una librería que permite controlar un grupo de servidores SSH de forma paralela. Es posible utilizar Fabric directamente desde linea de comandos ejecutando la utilidad fab o con la API que contiene todas las clases y decoradores necesarios para declarar un conjunto de servidores SSH, así como las tareas que queremos ejecutar sobre ellos.

Acerca de mi despliegue [+info](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/fabric.md)


#Despliegue remoto de la app en un IaaS: Azure  a través de Ansible y Vagrant

Para el despliegue de la app, he usado la suscripción que tengo de Azure. He montado los servidores con Vagrant en Azure y los he desplegado
y ejecutado con Ansible.

Básicamente para desplegar la app, he tenido que configurar los archivos de [VagrantFile](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/Vagrantfile), y el archivo de despligue de ansible [deployBook](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/ansible_hosts).

He configurado el [Makefile](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/Makefile), para que sólo tenga que hacer un ```make despligue```, para que se despligue todo en azure.

En teoría,si no se me ha agotado el crédito de Enero, estará funcionando en [pluco.cloudapp.net](pluc.cloudapp.net).

Para más información sobre el despligue consulte [aquí](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/despliegueAzure.md)
