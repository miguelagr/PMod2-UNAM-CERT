# Proyecto final

Para instalar el programa es necesario la descarga del repositorio

# git clone https://github.com/miguelagr/final

Una vez descargado procedemos a cambiar los permisos de ejecución

# chmod -R +x . 

Se instalará el directorio en el PATH del sistema por lo cual podremos hacer uso del comando "proyecto" para la ejecuion del programa principal

Para la ejecución del programa se puede hacer por medio de un comando con las diferentes opciones o con un archivo de configuración con el siguiente formato 

```
op1=arg1
opop2=arg2
...
```

Ejemplos de uso:

Genera una tabla "tablamd5" con todos los md5 de el archivo rockyou.txt

# proyecto -a md5 -g tablamd5 -d rockyou.txt

Hace la busqueda del hash utilizando las constraseñas del archivo md5 en tiempo real utilizando 10 hilos 

# proyecto -k -d rockyou.txt -t 10 -m <hexdigest>
