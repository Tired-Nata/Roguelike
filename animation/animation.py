import time
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

f1 = open("frame1.txt")
f2 = open("frame2.txt")
f3 = open("frame3.txt")
f = [f1,f2,f3]

for k in f:
  for i in k.readlines():
    print(i)
  time.sleep(1)
  cls()
  
