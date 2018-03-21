#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import crypt


def obtener_salt():
    salts = []
    with open("/etc/shadow",'r') as f:
        l = f.readline()
        while l:
            s = l.split(':')
            if len(s[1].split('$')[1:]) > 0:
                salts.append(('$%s$%s$' % tuple((s[1].split('$')[1:])[:-1]) , s[1] ))
            l = f.readline()
    return salts

def obtener_pass(arch):
    with open(arch) as f:
        l = f.readline()
        while l:
            for i in obtener_salt():
                c = crypt.crypt(l[:-1],i[0])
                if i[1] == c:
                    print l     
            l = f.readline()

obtener_pass("rockyou.txt")
