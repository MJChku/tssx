
import socket
import sys 
from time import time
import os 
from shared import c 
os.unlink("./test")
import numpy as np
sumMean = 0
a = 0

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.bind("./test")
    s.listen(1)
    conn, addr = s.accept()
    st = time()
    # print("whatsup")
    # c = 10000000
    while c:
        data = conn.recv(128)
        data = conn.send(data)
        c -= 1
        # print(c)
    print("time ", time()-st, sumMean)
    s.close()
    exit()
        # nparr = np.frombuffer(data, dtype=float)
        # if nparr.size > 0:
        #     sumMean += nparr.sum()
        # # a += sys.getsizeof(nparr)
        # # print(4*1000000-a)
        # if sumMean == 6*10000000:
        #     print("time ", time()-st, sumMean)
        #     s.close()
        #     exit()
   
