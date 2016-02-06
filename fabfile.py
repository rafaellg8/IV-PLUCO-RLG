from fabric.api import run, local, hosts, cd
from fabric.contrib.files import exists
from fabric.contrib import django

#infomacion del host
def informacion_host():
    run('uname -s')

#descarga de la aplicacion utilizando git. Si existe el directorio lo actualiza
def get_aplicacion():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	if dir():
		update()
        else:
		run('sudo git clone https://github.com/rafaellg8/IV-PLUCO-RLG.git')

#Instalacion necesaria para host virgen
def instalacion():
	get_aplicacion()
	run ('sudo apt-get install -y build-essential')
	run('cd IV-PLUCO-RLG/ && sudo make install')

#Sincronizacion de la aplicacion y la base de datos
def sincronizacion():
	run('cd IV-PLUCO-RLG/pluco/ && python manage.py syncdb --noinput')

#Ejecucion de test
def testeo():
	run('cd IV-PLUCO-RLG/pluco/ && make test')

#Compobar que el directorio existe. Si existe lo actualizamos
def dir():
    if exists('IV-PLUCO-RLG', use_sudo=True):
	return True
    else:
	return False

#Ejecucion de la aplicacion
def ejecucion():
	update()
	sincronizacion()
	run('cd IV-PLUCO-RLG/ && make run')

#peticion
def peticion():
	run('curl http://localhost:8000/')

def update():
    run('cd IV-PLUCO-RLG/ && git pull')

#Ejecucion remota del docker
#Instalacion de docker y descarga de imagen
def getDocker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull rafaellg8/iv-pluco-rlg')

#Ejecucion de docker
def runDocker():
	run('sudo docker run -p 80:80 -t -i rafaellg8/iv-pluco-rlg /bin/bash')

def docker():
	getDocker()
	runDocker()
