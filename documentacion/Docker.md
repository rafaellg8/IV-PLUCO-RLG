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

A continuación, creamos una "AutomaticBuild" para nuestra imagen, de nuestro repositorio. Para ello linkamos nuestro repo de github con Docker.
Así nos tiene que quedar el link de github ![imagen](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-07%20195810_zpsdqzd4m2u.png)
Seleccionamos nuestro repo de github para automatizar la creacion :
![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-07%20202217_zpsevelvcqh.png)

Una vez creada nuestra imagen de Docker, la tendremos funcionando y cada vez que modifiquemos nuestro repo de github, se integrará y copiará a nuestra imagen de manera automática. Así se llamará  a la construcción de la imagen cada vez que hagamos un "git push" en nuestro repositorio.

Vemos que se actualiza y se vuelve a construir tras un push:
![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-08%20000916_zpshnkfr7qz.png)

###Entorno de pruebas
Para la construcción de un entorno de pruebas, tendremos nuestra imagen en un contenedor donde se ejecutarán las pruebas.
Para el entorno de pruebas necesitamos configurar el Makefile para docker, y mandar un contenedor a nuestro repo. Para ello seguimos los pasos:


1. Nos logueamos
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ sudo docker login --username=rafaellg8 --email=rafaellg93@gmail.com
Password:
WARNING: login credentials saved in /home/rafaellg8/.dockercfg.
Login Succeeded
```
2. Añadimos un tag a la imagen:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
plucomachine_rlg    latest              7b09b787d194        11 days ago         555.9 MB
ubuntu              latest              7b09b787d194        11 days ago         555.9 MB
<none>              <none>              a9d5ba1c69ae        11 days ago         428.3 MB
<none>              <none>              ae99eb727d80        12 days ago         416.9 MB
<none>              <none>              e1d96ade4553        12 days ago         416.9 MB
<none>              <none>              03cdfd98b972        12 days ago         416.8 MB
<none>              <none>              e0d59055104a        12 days ago         416.8 MB
<none>              <none>              443a021339a0        12 days ago         416.8 MB
<none>              <none>              46d5f65e35d3        12 days ago         416.8 MB
commit_ubuntu       latest              d2571d9f30db        12 days ago         266.6 MB
<none>              <none>              cdcdbaba3536        12 days ago         266.6 MB
mongo               latest              ae293c6896a1        2 weeks ago         261.6 MB
debian              latest              ea6bab360f56        2 weeks ago         125.1 MB
ubuntu              14.04               ca4d7b1b9a51        3 weeks ago         187.9 MB

rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ sudo docker tag 7b09b787d194 rafaellg8/plucomachine_rlg:latest
```
3. Enviamos:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG$ sudo docker push rafaellg8/plucomachine_rlg
The push refers to a repository [rafaellg8/plucomachine_rlg] (len: 1)
```
Estos 3 pasos los podemos encontrar en el [tutorial](http://docs.docker.com/mac/step_six/) de Docker.

Modificamos el [Makefile]() para que obtenga la imagen del repo y ejecute docker:
```
docker:
	sudo apt-get -y install -y docker.io
	sudo docker pull rafaellg8/iv-pluco-rlg
	sudo docker run -p 8000:8000 -t -i rafaellg8/iv-pluco-rlg /bin/bash
```

Esto creará nuestra imagen dentro del contenedor y lo pondrá a funcionar, y si todo es correcto, al igual que hicimos con los ejercicios del tema de los contenedores, si introducimos la **IP** del contendor y el puerto 8000 que tengo configurado, nos aparece nuestra app:
![imagen](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-08%20114755_zpscvpgwkxd.png)
