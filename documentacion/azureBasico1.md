# Azure CLI: Certficados y acceso a la cuenta de Azure a través de la terminal
1. Instalamos el cliente a través de npm:
```
rafaellg8@system32:~/Desktop/pruebasIV$ sudo apt-get install nodejs-legacy
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias       
Leyendo la información de estado... Hecho
nodejs-legacy ya está en su versión más reciente.
0 actualizados, 0 se instalarán, 0 para eliminar y 12 no actualizados.
rafaellg8@system32:~/Desktop/pruebasIV$ sudo npm install -g azure-cli
```

2. Descargamos nuestra cuenta de azure para poder conectarnos:
```
rafaellg8@system32:~/Desktop/pruebasIV$ azure account download
info:    Executing command account download
info:    Launching browser to http://go.microsoft.com/fwlink/?LinkId=254432
help:    Save the downloaded file, then execute the command
help:      account import <file>
info:    account download command OK
rafaellg8@system32:~/Desktop/pruebasIV$

```

3. Nos logueamos a través de **azure login**:
```
rafaellg8@system32:~/Desktop/pruebasIV$ azure login
info:    Executing command login
-info:    To sign in, use a web browser to open the page https://aka.ms/devicelogin. Enter the code DKYYNDULZ to authenticate. If you're signing in as an Azure AD application, use the --username and --password parameters.
```
Introducimos el código para conectar el dispositivo.
Nos da lo siguiente:
```
/-
|info:    Added subscription Azure Pass
info:    Setting subscription "Azure Pass" as default
+
info:    login command OK
```

4. Mostramos nuestra cuenta, para comprobar que todo esté correcto:
![azureaccount](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202016-01-17%20082950_zpstrzoxrfl.png)

5. Creamos una clave y nos conectamos a través de ssh:
```
ssh-keygen
```
Guardamos la clave, en mi caso clavePrueba.

Ahora añadimos la id a nuestro servidor,en mi caso pluco:
```
ssh-copy-id -i ~/.ssh/clavePrueba.pub pluco@pluco.cloudapp.net
```
