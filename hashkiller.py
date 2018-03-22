#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import psycopg2
import sys

def genera_bd(fname,tabla):
    """
    Genera la base de datos con todos los hashes de cada cadena de un archivo de entrada
    Argumento:
        Nombre del archivo donde se sacan las cadenas en claro (str)
        Nombre de la tabla (str)
    Salida:
        None
    """
    conn = psycopg2.connect("dbname=root user=root password=hola123.,")
    cur = conn.cursor()
    cmd = "select (LOWER(tablename)) from pg_tables where schemaname like 'public' and tablename like LOWER('%s')" % (tabla)
    cur.execute(cmd)
    if cur.fetchone() is None:
        cur.execute("CREATE TABLE %s (id serial PRIMARY KEY, plain varchar%s);" % (tabla, ', "%s" varchar' * len(hashlib.algorithms_available) % tuple(hashlib.algorithms_available)))
	conn.commit()
	with open(fname,'r') as f:
	    for i in f.readlines():
                    p = i
	       	    m = [hashlib.new("%s" % j) for j in hashlib.algorithms_available]
	            for mi in m:
                        mi.update(p)
                    mh = tuple([i.hexdigest() for i in m])
                    cmd = "INSERT INTO %s(plain, %s) VALUES ('%s', %s);" % (tabla, ('"%s",' * len(hashlib.algorithms_available) % tuple(hashlib.algorithms_available))[:-1], p, ("'%s'," * len(mh) % tuple(mh))[:-1])
                    cur.execute(cmd)
	conn.commit()
	cur.close()
	conn.close()

def busca_hash(tabla,digest,algo):
    """
    Busca el texto en claro que corresponde al hash de la entrada
    Argumentos:
        Tabla de busqueda (str)
        Cadena del digest en formato hexadecimal (str)
        Algoritmos posibles para el digest (str[])
    Salida:
        Texto en claro correspondiente al hash de entrada (str[])
    """
    plain = []
    conn = psycopg2.connect("dbname=root user=root password=hola123.,")
    cur = conn.cursor()
    for i in algo:
        if i in hashlib.algorithms_available:
                cmd = "select (tablename) from pg_tables where schemaname like 'public' and tablename like '%s'" % (tabla)
	        cur.execute(cmd)
	        if cur.fetchone():
	            cmd = "SELECT plain FROM %s WHERE %s like '%s'" % (tabla,i,digest)
                    cur.execute(cmd)
	            e = cur.fetchone()
	            if e:
	                plain.append(e[0])
    cur.close()
    conn.close()
    return plain

def identifica(hashh):
    """
    Funcion que identifica el tipo de hash de acuerdo con su logitud
    Argumentos:
        El hash en formato hexadecimal (str)
    Salida:
        Lista de los posibles tipos de hashes de la cadena de entrada (str[])
    """
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

#print genera_bd("rockyou.txt","algos")

digest = 'd577273ff885c3f84dadb8578bb41399'
for i in busca_hash("algos",digest,identifica(digest)):
    print i
#print busca_hash("rockyou",sys.argv[1],identifica(sys.argv[1]))
digest = '2672275fe0c456fb671e4f417fb2f9892c7573ba'
for i in busca_hash("rockyou",digest,identifica(digest)):
    print i

