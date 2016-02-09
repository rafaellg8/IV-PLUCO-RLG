#Makefile autor: Rafael Lachica Garrido
all: install run
clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	git rm $(git ls-files --deleted)

install:
	sudo apt-get update --fix-missing
	sudo apt-get install -y python-dev
	sudo apt-get install -y python2.7-dev
	sudo apt-get install -y libpq-dev
	sudo apt-get install -y libffi-dev
	sudo apt-get install -y libffi6
	sudo apt-get install -y python-pip
	sudo apt-get install -y libfreetype6*
	sudo apt-get install -y freetype2*
	sudo apt-get -y install libjpeg8 libjpeg62-dev
	sudo apt-get -y install fabric
	sudo apt-get -y install python-unicodecsv
	sudo pip install --upgrade pip
	echo "Instalación paquetes terminada, instalano ahora requirements.txt"
	sudo pip install -r requirements.txt

migrate:
	cd pluco && python manage.py makemigrations
	cd pluco && python manage.py migrate

box:
	if vagrant box list | grep "azure";  then   echo "Si esta azure";  else vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box; fi

collect:
	cd pluco && python manage.py collectstatic --noinput

doc:
	cd pluco && epydoc index manage __index__ -o docs/

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

fabric:
	fab -p rafaellg8 -H pluco@pluco.cloudapp.net testeo -p 22

test:
	cd pluco && nosetests test/testingPluco.py

#Desplegar toda la app en Azure a través de vagrant y ansible
despliegue:
	#virtual box añadir
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
	cd VagrantAzure && sudo vagrant provision

docker:
	sudo apt-get -y install -y docker.io
	sudo docker pull rafaellg8/iv-pluco-rlg
	sudo docker run -p 8000:8000 -t -i rafaellg8/iv-pluco-rlg /bin/bash

#Quito el run porque a los 10 minutos de inactividad el servidor se para y da error
run:
	$(MAKE) collect
	$(MAKE) migrate
	#sudo chmod a+wr pluco/db.sqlite3
	nohup python pluco/manage.py runserver 0.0.0.0:8000 &
