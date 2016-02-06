#!/bin/bash
cmd=(dialog --separate-output --checklist "PLUCO : Asistente instalación:" 22 76 16)
options=(1 "Desplegar PLUCO en Azure" off    # any option can be set to default to "on"
         2 "Aprovisionar PLUCO" off
         3 "Instalar el repositorio" off
         4 "Ejecutar PLUCO" off)
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
clear
for choice in $choices
do
    case $choice in
        1)
            echo "Desplegando en 3 .. 2.. 1 .. YA!!!"
            sudo apt-get install -y make && time make despliegue;;
        2)
            echo "Aprovisionar"
            sudo apt-get install -y make && make provision;;
        3)
            echo "Instalar PLUCO"
            sudo apt-get install -y make && make install;;
        4)
            echo "Ejecutar PLUCO"
            sudo apt-get install -y make && make run;;
    esac
done
