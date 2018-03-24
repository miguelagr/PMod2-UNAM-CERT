#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import re
import sys
import optparse
from hashcat import buscaContrasena, generaHashes
from identificador import identifica


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
	parser.add_option('-k', '--hashcat', dest='hashcat', default=False,action='store_true',help='Usar modo "hashcat" para romper contraseñas')
	parser.add_option('-e', '--shadow', dest='shadow', default=None, help='Usar un archivo con el formato /etc/shadow')
	parser.add_option('-v', '--verbose', dest='verbose', default=False, action='store_true', help='Imprime la información detallada de la ejecucuión del programa')
	opts,args = parser.parse_args()
	return opts

##############################################################
# Método para leer configuraciones desde un archivo de texto #
# y pasarlas a un diccionario                                #
# Recibe:                                                    #
# Un archivo de texto                                        #
##############################################################
def lee_configuracion(archivo):
	res = {}
	with open(archivo,'r') as configuraciones:
		for linea in configuraciones.readlines():
			linea = linea.split('=')
			opcion = linea[0]
			valor = linea[1]
			if linea[0] == 'verbose' or linea[0] == 'hashcat':
				obten_bool[linea[1]]
			res[opcion] = valor
	return res			

############################################################################################
#                                                                                          #
#Función para almacenar las opciones que nos pasen por línea de comandos en un diccionario #
#																						   #
############################################################################################			
def obten_valores(opts):
    valores = {} 
    valores['hash'] = opts.valores
    valores['hashes'] = opts.hash
    valores['algoritmo'] = opts.hashes
    valores['diccionario'] = opts.diccionario
    valores['salt'] = opts.salt
    valores['formato'] = opts.formato
    valores['output'] = opts.output
    valores['threads'] = opts.threads
    valores['config'] = opts.config
    valores['identif'] = opts.identif
    valores['genera'] = opts.genera
    valores['hashkiller'] = opts.hashkiller
    valores['verboso'] = opts.verboso
    valores['hashcat'] = opts.hashcat
    valores['shadow'] = opts.shadow 
    return valores

#####################################################################################################
#																									#
#Función para cambiar el diccionario original en caso de recibir un archivo de configuración        #
#																									#
#####################################################################################################

def cambia_parametros(original, modificado):
	for key in modificado.keys():
		original[key] = modificado[key]
	return original


#####################################################################################################
#                                                                                                   #
#Función que va a revisar que las opciones se pasaron corréctamente                                 #                                  
#                                                                                                   #
#####################################################################################################

def revisa_opciones(opts):
	if opts['hashcat'] is not False and opts['hashkiller'] is not None: #Evita que se pasen al mismo tiempo el modo hashcat y el modo hashkiller
		error('¡¡No puedes usar al mismo tiempo las opciones hashcat y hashkiller!!')
	
	if opts['shadow'] is not None and opts['algoritmo'] is not None: #Evita que al usar un archivo con formato /etc/shadow se pasen las opciones: salt, algoritmo y genera (base de datos)
		error('¡¡No puedes usar al mismo tiempo las opciones shadow y algoritmo!!')
	elif opts['shadow'] is not None and opts['salt'] is not None:
		error('¡¡No puedes usar al mismo tiempo las opcines shadow y salt!!')
	elif opts['shadow'] is not None and opts['genera'] is not None:
		error('¡¡No puedes usar al mismo tiempo las opciones shadow y genera!!')

	if opts['salt'] is not None and opts['formato' is None]: #Evita que se pase la salt sin formato
		error('Debes especificar el formato de la salt')

#######################################################################################################
#																								      #
#Función que convierte el 'True' del archivo de configuración en un booleano                          #
#																									  #
#######################################################################################################

def obten_bool(parametro):
	parametro.lower in ('True')


####################################################################################################
#																								   #
#										Función main                                               #
#																								   #
####################################################################################################

if __name__ == '__main__':
	try:
		opts = addOptions()
		if obten_valores(opts)['config'] is not None:
			configuraciones = cambia_parametros(obten_valores(opts),lee_configuracion(obten_valores(opts)['config']))
		else: 
			configuraciones = obten_valores(opts)

		revisa_opciones(configuraciones)

		if configuraciones['hashcat'] :
			hashcat = hashcat()
			contrasenas = hashcat.generaHashes(configuraciones['diccionario'])
			hashcat.buscaContrasena(contrasenas)

		elif configuraciones['identif'] is not None:
			identificador = identificador()
			identificador.identifica(configuraciones['configuraciones'])

	except Exception as e:
		print 'Ocurrió un error'
        #error('Ocurrió un error')
		#error(e, True)