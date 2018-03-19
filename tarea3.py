#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
from itertools import *
let_num = {'a':'4','e':'3','i':'1','o':'0','y':'&'}

def printError(msg, exit = False):
    """
    Funcion para salir en caso de erro
    Argumentos:
        Mensaje de error (str)
    Salida:
        Valor para indicar la salida de ejecucion (bool)
    """
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)


def may_min(cad,salida):
    """
    Funcion que genera todas las posibles cadenas cambiando n letras
    a mayusculas
    Argumentos:
        Cadena (str)
        Nombre del archivo donde se escriben las combinaciones (str)
    Salida:
        La salida se escribe directamente en el archivo
    """
    with open(salida,'a+') as sal_dicc:
        for i in range(len(cad)+1)[1:]:
            for comb in combinations(range(len(cad)),i):
                li=list(cad)
                for ind in comb:
                    li[ind]=li[ind].upper()
                sal_dicc.write('%s\n' % ''.join(li))
        sal_dicc.close()


def genera_palabras(cad):
    """
    Funcion que cambia letras por numeros
    Argumentos:
        La cadena a la que se le realiza el cambio (str)
    Salida:
        Cadena con numeros por letras (str)
    """
    cad = ''.join(map(lambda x:let_num[x] if x in let_num else x,cad))
    return cad

def genera_dicc(entrada,salida):
    """
    Funcion que lee las posibles palabras que pueden formar una contraseña
    y genera combinaciones entre las mismas
    Argumentos:
        Archivo de entrada (str)
        Archivo de salida (str)
    """
    dicc = []
    dicci = dicc
    salidav = open(salida,'w')
    salidav.close()
    with open(entrada,'r') as lee_archivo:
        for line in lee_archivo.readlines():
            dicc.append(line[:-1])
            dicc.append(genera_palabras(line[:-1]))
        for palp in permutations(dicci,2):
            dicc.append(''.join(palp))

        print dicc
        for pal in dicc:
            print pal
            may_min(pal,salida)

if __name__ == '__main__':
    """
    Modo de uso
    ./tarea3 "Archivo de entrada" "Archivo de salida"
    """
    if len(sys.argv) != 3:
        printError('Indicar archivo a leer y archivo de reporte.', True)
    else:
        genera_dicc(sys.argv[1],sys.argv[2])

