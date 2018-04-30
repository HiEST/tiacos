import os
import sys
import time
import signal

def child():
   print("This is the  child. The infinite loop will start in 2sec")
   time.sleep(2)
   while True:
     print("looping in process ",os.getpid())

def parent(goal):
   num = 0;
   while num < goal:
     num = num + 1
     newpid = os.fork()
     if newpid == 0:
        child()
     else:
        ownpid = os.getpid()
        print("This is the parent process. PID: %d, child #%d - PID: %d\n" %  (ownpid, num, newpid))
        print('Waiting 5seconds before killing child')
        time.sleep(5);
        print('\nKilling process ', newpid)
        os.kill(newpid, signal.SIGKILL)



numchilds=1
parent(numchilds)
