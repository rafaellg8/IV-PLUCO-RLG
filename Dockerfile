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
