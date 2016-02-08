# Despliegue remoto de la app en un IaaS: Azure a través de Ansible y Vagrant

El despliegue se hará en un Ubuntu Server de Azure.
Para la creación y aprovisionamiento de la máquina virtual voy a usar [Vagrant](https://www.vagrantup.com/).
Después con [Ansible](http://www.ansible.com/) terminaremos de instalar los paquetes necearios para que funcione la app y las desplegaremos,arrancando la app y dejándola en ejecución, dentro de la máquina virtual.


##1. Preparando nuestro entorno
Aquí necesitamos instalar varios paquetes, como ansible y vagrant, y que sean las últimas versiones.
Yo lo tengo configurado todo en el makefile de forma automática:
```
  sudo apt-get install nodejs-legacy
	sudo apt-get install npm
	sudo npm install -g azure-cli
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo apt-get install -y vagrant
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y fabric
	vagrant plugin install vagrant-azure

```
Aquí instalamos npm, el cliente de azure, PyYAML para ansible, ansible, vagrant, etc.


##2. Conectándonos con Azure
Para poder desplegar en Azure, necesitamos conectarnos a nuestra suscripción a través de la terminal. Para ello tenemos que crearnos un par de ficheros de certificados de autentificación, e instalar el cliente de azure para **npm**.

Todos estos pasos están detallados en el siguiente [documento](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/azureBasico1.md)

##3. Configurando el archivo de desarrollo de ansible

Aquí, en el archivo [deployBook.yml](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/VagrantAzure/deployBook.yml), tenemos la configuración para la instalación y despligue de la app dentro de una máquina.
```
---
- hosts: localhost
  sudo: yes
  remote_user: pluco
  tasks:
  - name: Actualizar sistema base
    apt: update_cache=yes upgrade=dist
  - name: Instalar paquetes necesarios
    action: apt pkg={{ item }} state=installed
    with_items:
      - python-setuptools
      - python-dev
      - build-essential
      - git
      - make
  - name: Git clone, pluco
    git: repo=https://github.com/rafaellg8/IV-PLUCO-RLG.git dest=IV-PLUCO-RLG clone=yes force=yes

  - name: Ejecutando Make install
    command: chdir=IV-PLUCO-RLG make install

  - name: Make run
    command: chdir=IV-PLUCO-RLG make run &
```
Aquí, tenemos los host, como localhost, porque se ejecutará dentro de nuestra máquina que habremos creado.
Instala los paquetes necesarios, clona el repositorio, lo instala y lo ejecuta.

 Esto en nuestro directorio local funcionaría solo, si creamos nuestro archivo de **ansible_hosts** y hacemos lo siguiente:
**ansible_hosts**
 ```
[localhost]
127.0.0.1	ansible_connection=local

[pluco]
pluco.cloudapp.net

[plucoPlayBook]
prueba-iv-rlg.cloudapp.net ansible_sudo_pass='PlucoAzure1!'
```
Ahora simplemente nos queda exportar las variables de nuestro fichero de ansible_hosts a  **ANSIBLE_HOSTS**:
```
export ANSIBLE_HOSTS=~/ansible_hosts
```
La ejecución la haremos más adelante cuando hayamos creado el servidor en el siguiente paso.


##4. Creando el archivo de aprovisionamiento VagrantFile y creando el servidor en Azure
Para crear la máquina en Azure, necesitamos crear un [VagrantFile](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/VagrantAzure/Vagrantfile), donde tendremos la configuración de por ejemplo, que servidor queremos, nombre de usuario, puertos, etc.

Creamos el Vagrant File con nuestras necesidades.
 **NOTA** como indica el tutorial, hay que añadir nuestra cuenta de Azure y sus ficheros pem con el que usamos para el certificado y loguearnos:
```
VAGRANTFILE_API_VERSION = '2'
  Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.define "localhost" do |l|
    l.vm.hostname = "localhost"
  end

  config.vm.provider :azure do |azure|
    azure.mgmt_certificate = File.expand_path('~/clavesAzure/azure.pem')
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = '2cc2475d-2e3d-4d07-b873-e46b595373f7'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB'
    azure.vm_name = 'pluco'
    azure.vm_user = 'pluco'
    azure.vm_password = '***********'
    azure.vm_location = 'Japan West'
    azure.ssh_port = '22'
    azure.tcp_endpoints = '8000:8000'
    azure.tcp_endpoints = '80:80'
  end

  config.ssh.username = 'pluco'
  config.ssh.password = '***********'

  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "deployBook.yml"
    ansible.verbose = "v"
    ansible.host_key_checking = false
  end
end
```
Alguna cosas a comentar,pues por ejemplo arriba tenemos en el primer segmento del fichero, tenemos:
```
config.vm.box = 'azure'
config.vm.network "public_network"
config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
config.vm.network "forwarded_port", guest: 8000, host: 8000
config.vm.define "localhost" do |l|
  l.vm.hostname = "localhost"
end
```
La caja de azure,los puertos por defecto para python que serán los 8000 en la app de DJANGO, y la red privada que será la de virutal box.

En el siguten bloque tenemos:
```
config.vm.provider :azure do |azure|
  azure.mgmt_certificate = File.expand_path('~/clavesAzure/azure.pem')
  azure.mgmt_endpoint = 'https://management.core.windows.net'
  azure.subscription_id = '2cc2475d-2e3d-4d07-b873-e46b595373f7'
  azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB'
  azure.vm_name = 'pluco'
  azure.vm_user = 'pluco'
  azure.vm_password = '***********'
  azure.vm_location = 'Japan West'
  azure.ssh_port = '22'
  azure.tcp_endpoints = '8000:8000'
  azure.tcp_endpoints = '80:80'
```
Nuestros certificados de claves.
El endpoint de azure, donde se conecta al portal.
La máquina que queremos que nos cree, en este caso un Ubuntu Server 14.
Nuestro nombre de usuario y contraseña.
La localización del servidor,en este caso Oeste de Japón.
Y por último los puertos abiertos, el ssh, HTTP, y el 8000 para DJANGO.

En el último bloque del VagrantFile, tenemos lo siguiente:
```
config.ssh.username = 'pluco'
config.ssh.password = '***********'

config.vm.provision "ansible" do |ansible|
  ansible.sudo = true
  ansible.playbook = "deployBook.yml"
  ansible.verbose = "v"
  ansible.host_key_checking = false
end
```
Que corresponde a la configuración del ssh y datos de acceso. Y por último la llamada a ansible para despligue la app a través del **PlayBook** que hemos creado antes.


## 5. Configuración del Makefile y despligue final de la app:
Una vez configurado todo, he modificado el Makefile de la forma que ejecute todo lo anterior simplemente haciendo
```
make despigue
```

Aquí tenemos el completo [Makefile](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/Makefile).
Algunos detalles a comentar, son la regla del despliegue donde hacemos todo lo anterior, y la regla de ejecución, donde ejecutamos el servidor:
```
despliegue:
	sudo apt-get update --fix-missing
	sudo apt-get install nodejs-legacy
	sudo apt-get install npm
	sudo npm install -g azure-cli
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo apt-get install -y vagrant
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y fabric
	vagrant plugin install vagrant-azure
	sudo vagrant up --provider=azure
```

```
run:
	nohup python pluco/manage.py runserver 0.0.0.0:8000
```
Ejecutamos el servidor por el puerto 8000, con la opción nohup, para que al cerrar sesión siga activo el servidor.

## 6. La magia del despligue automático:
Ejecutamos:
```
make despliegue
```

Y tras esperar, tenemos nuestro servidor desplegado: [pluco.cloudapp.net](pluco.cloudapp.net).

**NOTA**: puede que se haya agotado el crédito, y esté la máquina apagada. Por eso pongo un par de pantallazos en el [siguiente documento](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/documentacion/servidordesplegado.md)
