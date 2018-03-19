#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
	parser = optparse.OptionParser()
	parser.add_option('-m','--romperHash', dest='romperHash', default=None, help='Recibe un hash a romper')
	parser.add_option('-M', '--romperHashes', dest='romperHashes', defalult=None, help='Recibe una lista de hashes a romper')
	parser.add_option('-a', '--algoritmo', dest='algoritmo', default=None, help='Algoritmo con el que fue calculado el hash a romper/algoritmos para la rainbow table')
	parser.add_option('-d', '--diccionario', dest='diccionario', default=None, help='Diccionario de contraseñas para el cálculo de hashes')
	parser.add_option('-s', '--salt', dest='salt', default=None, help='Salt a usar para el cálculo del hash')
	parser.add_option('-f', '--formato', dest='formato', default=None, help='Formato de uso de la salt ($salt$pass o $pass$salt)')
	parser.add_option('-o', '--output', dest='output', default=None, help='Archivo dónde se guardará el reporte de los resultados')
	parser.add_option('-t', '--threads', dest='threads', default=None, help='Número de hilos a utilizar para el calculo de los hashes')
	parser.add_option('-c', '--config', dest='config', default=None, help='Archivo de configuración que puede ser usado para modificar la ejecución')
	parser.add_option('-i', '--identif', dest='identif', default=None, help='Identifica el tipo de hash introducido')
	parser.add_option('-g', '--genera', dest='genera', default=None, help='Genera una base de datos con los hashes de un diccionario de contraseñas')
	parser.add_option('-b', '--hashkiller', dest='hashkiller', default=None, help='Usar modo "hash killer" para romper contraseñas')
	parser.add_option('-k', '--hashcat', dest='hashcat', default=None, help='Usar modo "hashcat" para romper contraseñas')
	parser.add_option('-e', '--shadow', dest='shadow', default=None, help='Usar un archivo con el formato /etc/shadow')
	parser.add_option('-v', '--verbose', dest='verbose', default=None, help='Imprime la información detallada de la ejecucuión del programa')
	parser.add_option('-h', '--help', dest='help', default=None, help='Muestra información sobre las banderas')
	opts,args = parser.parse_args()
	return opts