#Fabric

Para el despliegue con Fabric seguimos los siguientes pasos:

1. Crear el fabfile.py e instalar Fab.

Creamos el fabfile que es lo que ejecutaremos de código una vez despleguemos en Fabric. Lo podemos consultar completo [aquí](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/fabfile.py)
Las principales funciones para ejecutar son:

```
def instalacion():
	run('cd IV-PLUCO-RLG/ && sudo make install')

#Sincronizacion de la aplicacion y la base de datos
def sincronizacion():
	run('cd IV-PLUCO-RLG/pluco/ && python manage.py syncdb --noinput')

#Ejecucion remota del docker
#Instalacion de docker y descarga de imagen
def getDocker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull rafaellg8/iv-pluco-rlg')

#Ejecucion de docker
def runDocker():
	run('sudo docker run -i -t rafaellg8/iv-pluco-rlg')
```

En los requeriments.txt añadimos la siguientes líneas:
```
Fabric
```
Igual en el Makefile:
```
sudo apt-get -y install fabric
```

2. Accedemos a la máquina virtual de plugo donde realizaremos el despliegue:
Instalamos previamente fabric con la orden ```sudo apt-get -y install fabric``` y ejecutamos lo siguiente:
![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-23%20192238_zpsbqzfubyk.png)

Obtenemos la aplicación con "get_aplicacion":

![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-23%20195322_zps6t5eksop.png)

Ahora que hemos descargado la app del repo, procedemos a instalarla:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG/pluco$ fab -p rafaellg8 -H pluco@104.208.30.20 instalacion -p 22
[pluco@104.208.30.20] Executing task 'instalacion'
[pluco@104.208.30.20] run: cd IV-PLUCO-RLG/ && sudo make install
```

**NOTA**: aunque hemos usado siempre la IP, podemos usar también el dominio, con pluco.cloudapp.net

Sincronizamos las bases de datos de los modelos:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG/pluco$ fab -p rafaellg8 -H pluco@104.208.30.20 sincronizacion -p 22
[pluco@104.208.30.20] Executing task 'sincronizacion'
[pluco@104.208.30.20] run: cd IV-PLUCO-RLG/pluco/ && python manage.py syncdb --noinput
```

![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-23%20201128_zpscedmm0zw.png)

Testeamos:
```
rafaellg8@system32:~/Documentos/GII/Cuarto/IV/IV-PLUCO-RLG/pluco$ fab -p rafaellg8 -H pluco@104.208.30.20 testeo -p 22
[pluco@104.208.30.20] Executing task 'testeo'
[pluco@104.208.30.20] run: cd IV-PLUCO-RLG/pluco/ && make test
[pluco@104.208.30.20] Login password for 'pluco':
```

3. Si todo ha ido correcto, ejecutamos la app:
**Nota**: tenemos que desactivar apache primero ya que tiene el puerto 80 ocupado: ```sudo service apache2 stop```

![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-12-23%20204551_zpslb8wx7qz.png)

Y si no se me apagó el servidor, debería estar funcionando aquí [pluco.cloudapp.net](http://pluco.cloudapp.net)
