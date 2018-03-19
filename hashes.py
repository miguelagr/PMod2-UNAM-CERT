import hashlib
import time

m = hashlib.md5()
m.update("")
print m.hexdigest()
for i in range(500000):
    m2 = hashlib.md5()
    m2.update("")
    print m2.hexdigest()

print time.clock()
#for i in hashlib.algorithms_available:
#    print i


