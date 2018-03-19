import hashlib
import threading
import time


def hashes(num):
    for i in range(100000):
        m = hashlib.md5()
        m.update("n")
        print m.hexdigest()
    print time.clock()

threads = []
print time.clock()
for i in range(5):
    t = threading.Thread(target=hashes, args=(i,))
    threads.append(t)
    t.start()
print time.clock()
    
#m2 = md4.new()
#m2.update("")
#print m2.hexdigest()

#for i in hashlib.algorithms_available:
#    print i
