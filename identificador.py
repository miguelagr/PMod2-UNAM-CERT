#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import sys

###########################################################################
# Función para identificar el tipo de has introducido                     #                                                   #
###########################################################################
def identifica(hashh):
	tamano = len(hashh) * 4
	if tamano == 128:
		print "El tipo de hash puede ser MD5, MD4 o NTLM"
	elif tamano == 180:
		print "El tipo de hash es SHA1"
	elif tamano == 224:
		print "El tipo de hash es SHA-224"
	elif tamano == 256:
		print "El tipo de hash es SHA-256"
	elif tamano == 384:
		print "El tipo de hash es SHA-384"
	elif tamano == 512:
		print "El tipo de hash es SHA-512"
	else:
		print "No se pudo identificar el hash"

#identifica(sys.argv[1])

