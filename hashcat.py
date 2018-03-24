#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import hashlib
import binascii
import sys
import threading
from Crypto.Hash import MD4
import Queue

#############################################################################################################################
#                                                                                                                           #
# Función mediante la cuál vamos a generar los hashes, regresa un diccionario;                                              #
# en el cuál la contraseña a analizar es la llave y el valor es un arreglo con los diferentes hashes para dicha contraseña  #
#                                                                                                                           #
#############################################################################################################################
def generaHashes(archivo,hilos,hilo,q):
	hashes = {}
	try:
		contrasenas = open(archivo,"r")
                for i in range(1,hilo + 1):
		    linea = contrasenas.readline()
		while linea:
			linea = linea.rstrip('\n') #Quitamos saltos de línea
			linea = linea.rstrip('\t') #Quitamos tabuladores 
			linea = linea.rstrip('\r') #Quitamos retorno de carro 				#A partir de aquí empezamos a calcular los hashes
			md4 = MD4.new()
			md4.update(linea)
			md5 = hashlib.md5()
			sha1 = hashlib.sha1()
			sha224 = hashlib.sha224()
			sha256 = hashlib.sha256()
			sha384 = hashlib.sha384()
			sha512 = hashlib.sha512()
			ntlm = hashlib.new('md4', linea.encode('utf-16le', 'ignore')).digest()
			md4.update(linea)
			md5.update(linea)
			sha1.update(linea)
			sha224.update(linea)
			sha256.update(linea)
			sha384.update(linea)
			sha512.update(linea)
			#print("***************************")
			#print("----------md4--------------")
			#print(md4.hexdigest())
			#print("----------md5--------------")
			#print(md5.hexdigest())
			#print("----------sha1-------------")
			#print(sha1.hexdigest())
			#print("---------sha224------------")
			#print(sha224.hexdigest()) 
			#print("---------sha256------------")
			#print(sha256.hexdigest())
			#print("---------sha384------------")
			#print(sha384.hexdigest())
			#print("----------sha512-----------")
			#print(sha512.hexdigest())
			#print("----------ntlm-------------")
			#print(binascii.hexlify(ntlm))
			valores = [md4.hexdigest(), md5.hexdigest(), sha1.hexdigest(), sha224.hexdigest(), sha256.hexdigest(), sha384.hexdigest(), sha512.hexdigest(), binascii.hexlify(ntlm)]
			hashes[linea] = valores #Guardamos como llave la contraseña y como valor un arreglo con los hashes
                        for i in range(hilos):
                            linea = contrasenas.readline()
		#print(hashes)
		q.put(hashes)
		contrasenas.close()
	except IOError:
		print "Ocurrió un error al tratar de abrir el archivo"


#for numero_hilos in range(3):
#		hilo = threading.Thread(target=generaHashes, args=numero_hilos)

#		hilo.start()
    	
########################################################################################################################
#																													   #
#Función que a partir del diccionario que nos regresa generaHashes y un hash dado, busca la coincidencia               #                                                                                                        #   
#																													   #
########################################################################################################################

def buscaContrasena(diccionario,hash):
	#contador = 0
	for key in diccionario.keys():
			for value in diccionario[key]:
				#print value
				if value == hash:
					print "La contraseña es: " + key
def hashcat(hilos,archivo,digest):
        threads = []
        q = Queue.Queue()
        for i in range(hilos):
                        t = threading.Thread(target=generaHashes, args=(archivo,hilos,i + 1,q,))
                        threads.append(t)
                        t.start()
                        t.join()
        for item in range(len(threads)):
                        buscaContrasena(q.get(),digest)



#hashcat(10,"rockyou.txt", sys.argv[1])



#m2 = md4.new()
#m2.update("")
#print m2.hexdigest()

#for i in hashlib.algorithms_available:
#    print i
