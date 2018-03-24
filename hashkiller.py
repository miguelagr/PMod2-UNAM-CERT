#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import time
import psycopg2
import sys
import binascii

def genera_bd(fname,tabla,algo):
    """
    Genera la base de datos con todos los hashes de cada cadena de un archivo de entrada
    Argumento:
        Nombre del archivo donde se sacan las cadenas en claro (str)
        Nombre de la tabla (str)
    Salida:
        None
    """
    disponibles = list(hashlib.algorithms_available)
    disponibles.append('ntlm')
    algo = filter(lambda x: x in disponibles ,algo)
    if len(algo) < 1:
        sys.exit("Introducir un hash valido")
    conn = psycopg2.connect("dbname=root user=root password=hola123.,")
    cur = conn.cursor()
    cmd = "select (LOWER(tablename)) from pg_tables where schemaname like 'public' and tablename like LOWER('%s')" % (tabla)
    cur.execute(cmd)
    if cur.fetchone() is None:
        cur.execute("CREATE TABLE %s (id serial PRIMARY KEY, plain varchar%s);" % (tabla, ', "%s" varchar' * len(algo) % tuple(algo)))
	conn.commit()
	with open(fname,'r') as f:
            i = f.readline()
	    while i:
                p = i[:-1]
                if 'ntlm' in algo:
                    algo = filter(lambda x: x in hashlib.algorithms_available,algo)
                    ntlm = hashlib.new('md4', i.encode('utf-16le', 'ignore')).digest()
                    hntlm = binascii.hexlify(ntlm)
                else:
                    ntlm = None
                    hntlm = None
	       	m = [hashlib.new("%s" % j) for j in algo]
                for mi in m:
                    mi.update(p)
                mhh = [i.hexdigest() for i in m]
                if ntlm:
                    mhh.append(hntlm)
                    algo.append('ntlm')
                mh = tuple(mhh)
                cmd = "INSERT INTO %s(plain, %s) VALUES ('%s', %s);" % (tabla, ('"%s",' * len(algo) % tuple(algo))[:-1], p, ("'%s'," * len(mh) % tuple(mh))[:-1])
                cur.execute(cmd)
                i = f.readline()
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
    disponibles = []
    conn = psycopg2.connect("dbname=root user=root password=hola123.,")
    cur = conn.cursor()
    cmd = "select (column_name) from information_schema.columns where LOWER(table_name) like LOWER('%s')" % (tabla)

    cur.execute(cmd)
    al = cur.fetchone()
    while al:
        disponibles.append(al[0])
        al = cur.fetchone()
    for i in algo:
        if i in disponibles:
                cmd = "select (tablename) from pg_tables where schemaname like 'public' and tablename like '%s'" % (tabla)
	        cur.execute(cmd)
	        if cur.fetchone():
	            cmd = "SELECT plain FROM %s WHERE %s like '%s'" % (tabla,i,digest)
                    cur.execute(cmd)
	            e = cur.fetchone()
	            if e:
	                plain.append((e[0],digest))
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
#print genera_bd(sys.argv[1],sys.argv[2],sys.argv[3:])

#digest = 'd577273ff885c3f84dadb8578bb41399'
#<<<<<<< HEAD
#print busca_hash(sys.argv[1],sys.argv[2],identifica(sys.argv[2]))
#=======
#print busca_hash(sys.argv[1],sys.argv[2],identifica(sys.argv[2]))
#>>>>>>> d06f7a02b4a066e1cc30b2c0ccbd08d80ff81701
#    print i


#print busca_hash("rockyou",sys.argv[1],identifica(sys.argv[1]))
#digest = '2672275fe0c456fb671e4f417fb2f9892c7573ba'
#for i in busca_hash("rockyou",digest,identifica(digest)):
#    print i


