import time
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

f11,f12,f13,f14,f15,f16,f17,f18 = open("Battle1.1.txt"),open("Battle1.2.txt"),open("Battle1.3.txt"),open("Battle1.4.txt"),open("Battle1.5.txt"),open("Battle1.6.txt")
,open("Battle1.7.txt"),open("Battle1.8.txt")
f1=[f11,f12,f13,f14,f15,f16,f17,f18]

def animation1(f1):
    for k in f:
      for i in k.readlines():
        print(i)
      time.sleep(1)
      cls()
  
