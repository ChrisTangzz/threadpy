import threading
import time
import math

sum  = 0

lock = threading.Lock()

def job(index,st, end):
    global sum, lock
    print("thread ", index, " 開始")
    lock.acquire()
    for i in range(st, end+1):
        sum += i
    lock.release()    
    print("thread ", index, " 結束") 
     
thnum = int(input("thread 的個數x : "))
ternum = int(input("計算到 : "))

threads = []


for i in range(thnum):
  threads.append(threading.Thread(target = job, args = (i+1,math.floor((i)*(ternum/thnum)+1), math.floor((i+1)*(ternum/thnum)))))
  threads[i].start()
  
for i in range(thnum):
  threads[i].join()

print("threading sum : ",sum)