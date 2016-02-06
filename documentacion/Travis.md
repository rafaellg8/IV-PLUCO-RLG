##Integración continúa de PLUCO-RLG en Travis

He creado un archivo .travis.yml que contiene la configuración para otra parte de la integración continua en Shippable con travis:
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
Es el mismo fichero que uso para shippable, ya que estoy haciendo lo mismo pero en 2 entornos de integración distintos.

Para que funcione todo en Travis, además de la configuraciónd de archivos, hace falta hacer como en shippable registrarse y enlazar reposotorio
1. Nos registramos [Travis](https://travis-ci.org)
2. Enlazamos repositorio ![img](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/temp1_zps58uunex0.png)
3. Subimos todo a git-hub para que travis detecte los cambios
```
rafaellg8: ~/IV-PLUCO-RLG $ git commit -m "Nuevo travis python"
[master 1342e2d] Nuevo travis python
 1 file changed, 42 insertions(+), 28 deletions(-)
 rewrite .travis.yml (72%)
rafaellg8: ~/IV-PLUCO-RLG $ git push origin master
```
4. Ejecutan los tests en Travis y funciona todo de forma correcta
![Imagen Travis](http://i1383.photobucket.com/albums/ah302/Rafael_Lachica_Garrido/temp1_zpsajopzafs.png)
