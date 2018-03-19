import hashlib
import time
import psycopg2

print time.clock()
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
            cur.execute("INSERT INTO %s(plain, hash) VALUES (%s,%s)" % (j,i,m.hexdigest()))
            conn.commit()

cur.close()
conn.close()


for i in hashlib.algorithms_available:
    print i
    m = hashlib.new(i)
    m.update("hola")
    print m.hexdigest()

print time.clock()
