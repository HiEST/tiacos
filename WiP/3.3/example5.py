import os
import sys
import time
import signal



def child():
   parentpid = os.getppid()
   print("This is the  child. The parent PID is: ", parentpid)
   time.sleep(1)
   os.kill(parentpid, signal.SIGALRM)
   sys.exit()
   #while True:
   #  print("looping in process ",os.getpid())

def handler(signum, frame):
    print ('Signal handler called with signal', signum)

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
        signal.signal(signal.SIGALRM, handler)
        time.sleep(3)



numchilds=1
parent(numchilds)
