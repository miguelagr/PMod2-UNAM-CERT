#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import psycopg2

print time.clock()

conn = psycopg2.connect("dbname=root user=root password=hola123.,")
cur = conn.cursor()

for i in hashlib.algorithms_guaranteed:
    cur.execute("CREATE TABLE %s (id serial PRIMARY KEY, plain varchar, hash varchar);" % i)
    conn.commit()

with open("rockyou.txt",'r') as f:
    for i in f.readlines():
        for j in hashlib.algorithms_guaranteed:
            m = hashlib.new("%s" % j)
            m.update(i)
            cmd = "INSERT INTO %s(plain, hash) VALUES ('%s','%s');" % (j,i[:-1],m.hexdigest())
            #print cmd
            cur.execute(cmd)
            conn.commit()

cur.close()
conn.close()

print time.clock()
