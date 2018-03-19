import hashlib
import time

print time.clock()

with open("rockyou.txt",'r') as f:
    for i in f.readlines():
        m = hashlib.md5()
        m.update(i)
        print m.hexdigest()


#for i in range(500000):
#    m2 = hashlib.md5()
#    m2.update("")
#    print m2.hexdigest()

print time.clock()
#for i in hashlib.algorithms_available:
#    print i

for i in hashlib.algorithms_guaranteed:
    print i
    m = hashlib.new(i)
    m.update("hola")
    print m.hexdigest()


for i in hashlib.algorithms_available:
    print i
    m = hashlib.new(i)
    m.update("hola")
    print m.hexdigest()
