#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import psycopg2
import sys

def genera_bd():
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
	            cur.execute(cmd)
	            conn.commit()
	cur.close()
	conn.close()

def busca_hash(digest,algo):
	conn = psycopg2.connect("dbname=root user=root password=hola123.,")
	cur = conn.cursor()
        for i in algo:
            print i 
	    cmd = "SELECT plain FROM %s WHERE hash like '%s'" % (i,digest)
	    cur.execute(cmd)
            print cur.fetchone()
	cur.close()
	conn.close()

def identifica(hashh):
	tamano = len(hashh) * 4
	if tamano == 128:
	    return ['md5']
	elif tamano == 180:
	    return ['SHA1']
	elif tamano == 224:
	    return ['SHA224']
	elif tamano == 256:
	    return ['SHA256']
	elif tamano == 384:
	    return ['SHA384']
	elif tamano == 512:
	    return ['SHA512']
	else:
            sys.exit("hash invalido")

digest = 'd577273ff885c3f84dadb8578bb41399'
busca_hash(digest,identifica(digest))
