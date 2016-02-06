#Integración Continúa PLUCO-RLG en Shippable

Para la integración continua, voy a usar la herramienta Shippable, la cual es bastante fácil de usar y muy útil.
Para ello procedemos de la siguiente forma

1. Nos registramos en Shippable
2. Enlazamos con nuestro repositorio de github que queremos que tenga la integración continua.
3. Configuramos el archivo configuration.yml que es donde se pondrá las reglas que queremos que haga, los test, las herramientas a instalar etc.

##Pasos más detallados:

Para la integración y testeo de mi proyecto en github voy a usar [**Shippable**](https://app.shippable.com).
Para ello le damos a la opción de añadir un nuevo proyecto desde la interfaz web:
![Imagen](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-10-18%20200348_zpse5yuipbb.png)
Para la gestión y automatización de paquetes, usaré Pip de Python.
Para ello instalamos **python-pi** con el instalador de paquetes.

Nos creamos un archivo para hacer los test, con extensión **yml**:
```
language: python
build_image: shippableimages/ubuntu1204_python
python:
  - 2.6
  - 2.7
  - 3.2
  - 3.3
  - 3.4
  - pypy
author:
  - Rafael Lachica Garrido
name:
  - Pluco RLG
description:
  - A platform for sharing information, with forums to sharing issues and resolve problems.
install:
 - pip install pyyaml
 - pip install grunt-django
 - pip install nose
 - pip install pytest
 - pip install tox
 - pip install pytest-cov
 - pip install pytest-xdist
 - easy_install nose
 - pip install pystache
 - pip install pygments
 - pip install markdown
 - pip install importlib
 - pip install epydoc

# Make folders for the reports
before_script:
  - mkdir -p shippable/testresults
  - mkdir -p shippable/codecoverage
  - mkdir -p shippable/documentation
  - mkdir -p shippable/test

script:
  - which python
  - nosetests
  - make   #ejecutamos makefile
  #Basic test central
  #- py.test --cov=tests/
  #Distribution load test
  #- py.test --cov= -n 2 tests/
notifications:
  email:
   - rafaellg8@correo.ugr.es

```

Subimos a github y esperamos a que se ejecuten las pruebas en shippable.
Se ejecuta correctamente:
![Shippable](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/Captura%20de%20pantalla%20de%202015-10-18%20210433_zps1zlqo3nf.png)
Los test funcionan correctamente en shippable
![TestShipable](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/temp1_zpsxfpgraug.png)
