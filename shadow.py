#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import psycopg2

print time.clock()


with open("/etc/shadow",'r') as f:
    l = f.readline()
    while l:
        print l
        s = l.split(':')
        print s[1]
        print s[1].split('$')[1:]
        l = f.readline()

print time.clock()
