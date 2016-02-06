#Ajustando Pipelines en SNAP-CI y configurando la app para TEST y depués DESPLIEGUE

###Configuración Travis y Shippable para pasar test y después subir a Heroku

Para esto, tenemos que configurarlo todo desde el dashbord de Heroku:

Buscamos la opción en Deploy-> Connect with Github y conectamos con nuestro repositorio:

![Connect](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20175120_zpssrnq3sby.png)

Por último para que pase los test y después muestre en Heroku, creamos un "Pipeline" a través del software [SNAP CI](https://snap-ci.com/)

Creamos un pipeline donde primero instale y testee y depués despliegue la app en Heroku:
![snapci1](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20182305_zpsf77zeyyh.png)

![Snapci2](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20182300_zpslf7211nh.png)
En esta parte hay que hacer loggin en heroku y seleccionar desplegar app de forma básica.

Pulsamos Build now y esperamos los resultados:
![snapci3](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-11-16%20182633_zpsw6dm8lds.png)

