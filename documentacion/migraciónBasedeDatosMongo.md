
###Migración MongoDB desde local a MongoLabs
Para que funcione mi app, como tengo una base de datos en mongodb, tenemos que exportar y migrar la base da datos a MongoLabs.
Para esto nos registramos en MongoLabs, donde nos dan unos datos para conectarnos por ssh e importar y exportar datos. También seguimos las instrucciones que da al inicio y creamos una base de datos y un usuario que administre la base de datos:
![imagenUserDB](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20232554_zpsxgo168be.png)

Creamos un dump en local que después importaremos en MongoLabs:
```
rafaellg8@system32:~$ mongodump --db pluco
2015-11-16T23:14:22.659+0100  writing pluco.usuarios to dump/pluco/usuarios.bson
2015-11-16T23:14:22.659+0100  writing pluco.system.indexes to dump/pluco/system.indexes.bson
2015-11-16T23:14:22.661+0100  writing pluco.usuarios metadata to dump/pluco/usuarios.metadata.json
2015-11-16T23:14:22.662+0100  done dumping pluco.usuarios (5 documents)
```
Esto nos crea la carpeta dump, donde dentro están los archivos. Ahora importamos a MongoLabs:
```
mongorestore ds055584.mongolab.com:55584/pluco -u admin -p  dump/
```

Y ya tenemos nuestra base de datos en MongoLabs. Ahora cambiamos las conexiones en el módulo de python de configdb.py:
```
 #establecemos la conexion
           #configuramos parametros conexion
            server='ds055584.mongolab.com'
            port = 55584
            db_name = 'pluco'
            db_username = 'admin'
            db_password = '*****'
            #establecemos la conexion
            try:
                  #configuramos conexion mongolab
                  print '\nConnecting....'
                  conn = pymongo.MongoClient(server,port)

                  #obtenemos la base de datos
                  print '\nGetting databases....'
                  db = conn[db_name]

                  #autenticamos
                  print '\nAuthenticating....'
                  db.authenticate(db_username,db_password)

                  print "\nConnection succesfully"
```

Y ya tenemos todo configurado. Registramos un usuario de prueba y vemos sus datos en MongoLabs:
![imagen](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20232108_zpszrwktnfd.png)

Configuración del archivo completo [mongo](https://github.com/rafaellg8/IV-PLUCO-RLG/blob/master/plucorlg/configdb.py)
