#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time

print time.clock()


with open("/etc/shadow",'r') as f:
    l = f.readline()
    while l:
        s = l.split(':')
        print s[1].split('$')[1:]
        l = f.readline()

print time.clock()

st = raw_input("hola: ")
print st
