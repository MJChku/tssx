
import socket
import sys 
from time import time
import numpy  as np
from shared import c 
n = 4
a = np.arange(0, n).astype(float)
a_size = sys.getsizeof(a)
abytes = a.tobytes()
print(np.frombuffer(abytes).sum())
print ('%d bytes, %dKB, %dMB' % (a_size, a_size/1024, a_size/1024/1024))

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
    client.connect("./test")
    # c = 10000000
    st = time()
    while c:
        client.send(abytes)
        client.recv(128)
        c -= 1
        # print(c)
    print("time ", time()-st)
    client.close()
