import threading
import time
import math

def job(index,st, end):
    tmp = 0
    print("thread ", index, " 開始")
    for i in range(st, end+1):
        tmp += i
    threadsnum.append(tmp)
    print("thread ", index, " 結束")

thnum = int(input("thread 的個數x : "))
ternum = int(input("計算到 : "))

threads = []
threadsnum = []
sum  = 0 

st1 =  time.time()

for i in range(thnum):
  threads.append(threading.Thread(target = job, args = (i+1,math.floor((i)*(ternum/thnum)+1), math.floor((i+1)*(ternum/thnum)))))
  threads[i].start()
  
for i in range(thnum):
  threads[i].join()

for i in range(thnum):
  sum += threadsnum[i]

print("threading sum : ",sum)
end1 = time.time()

print("threading time : ", end1-st1)

st2 = time.time()

sum = 0

for i in range(1, ternum+1):
    sum += i
print("normal sum : ",sum)

end2 = time.time()

print("normal time : ", end2-st2)

print("normal time / threading time = ", (end2-st2)/(end1-st1))

