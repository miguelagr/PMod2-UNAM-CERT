import datetime

print datetime.datetime.now().strftime('%H:%M:%S:%f')

def reporte(inicio,fin,hashes = []):
    print "Hora de inicio" + inicio
    print "Hora de término" + fin

    print "Hashes encontrados:"
    for i in hashes:
        print i[0] + ", " + i[1]

