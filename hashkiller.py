#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import psycopg2
import sys

def genera_bd(fname):
	conn = psycopg2.connect("dbname=root user=root password=hola123.,")
	cur = conn.cursor()
	for i in hashlib.algorithms_guaranteed:
            cmd = "select (tablename) from pg_tables where schemaname like 'public' and tablename like '%s'" % (i)
            cur.execute(cmd)
            if cur.fetchone() is None:
	        cur.execute("CREATE TABLE %s (id serial PRIMARY KEY, plain varchar, hash varchar);" % i)
	        conn.commit()
	with open(fname,'r') as f:
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
	plain = []
        conn = psycopg2.connect("dbname=root user=root password=hola123.,")
	cur = conn.cursor()
        for i in algo:
            cmd = "select (tablename) from pg_tables where schemaname like 'public' and tablename like '%s'" % (i)
            cur.execute(cmd)
            if cur.fetchone():
	        cmd = "SELECT plain FROM %s WHERE hash like '%s'" % (i,digest)
	        cur.execute(cmd)
                e = cur.fetchone()
                if e:
                    plain.append(e[0])
	cur.close()
	conn.close()
        return plain

def identifica(hashh):
	tamano = len(hashh) * 4
	if tamano == 128:
	    return ['md5','md4','NTLM']
	elif tamano == 160:
	    return ['sha1']
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

#genera_bd("rockyou.txt")

digest = 'd577273ff885c3f84dadb8578bb41399'
busca_hash(digest,identifica(digest))
print busca_hash(sys.argv[1],identifica(sys.argv[1]))
digest = '2672275fe0c456fb671e4f417fb2f9892c7573ba'
for i in busca_hash(digest,identifica(digest)):
    print i

