#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import crypt


def obtener_salt(shadowf):
    """
    Obtiene todos los salts presentes en un archivo con el formato del archivo shadow
    Argumentos:
        Nombre del archivo con formato shadow (str)
    Salida:
        Tupla con los salts presentes y su respectivo hash (str)
    """
    salts = []
    with open(shadowf,'r') as f:
        l = f.readline()
        while l:
            s = l.split(':')
            if len(s[1].split('$')[1:]) > 0:
                salts.append(('$%s$%s$' % tuple((s[1].split('$')[1:])[:-1]) , s[1] ))
            l = f.readline()
    return salts

def obtener_pass(arch,sh):
    """
    Obtiene en tiempo real todos los hashes resultado de la combinacion de una lista de salts con cada una
    de las contraseñas presentes en un archivo de contraseñas imprimiendo todas las contraseñas en claro 
    que generan coincidencias
    Argumentos:
        Nombre del archivo con todas las contraseñas en claro (str)
        Tupla de salts con su respectivo hash ((str,str)[])
    Salida:
        Lista de coincidencias encontradas (str[])
    """
    with open(arch) as f:
        t = []
        l = f.readline()
        while l:
            for i in sh:
                c = crypt.crypt(l[:-1],i[0])
                if i[1] == c:
                    t.append((l,i[1]))
            l = f.readline()
        return t

print obtener_pass("rockyou.txt",obtener_salt("shadow"))
