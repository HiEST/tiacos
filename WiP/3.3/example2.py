import os
import sys
import time
import signal

def handler(signum, frame):
    print ('Signal handler called with signal', signum)
    print ('My parent has killed me using signal', signum)
    sys.exit()

def child():
   parentpid = os.getppid()
   print('This is the  child. The parent PID is: ', parentpid)
   time.sleep(2)
   while True:
      nop = 1

def parent(goal):
   signal.signal(signal.SIGUSR1, handler)
   num = 0;
   while num < goal:
     num = num + 1
     newpid = os.fork()
     if newpid == 0:
        child()
     else:
        ownpid = os.getpid()
        print('This is the parent process. PID: %d, child #%d - PID: %d\n' %  (ownpid, num, newpid))
        time.sleep(5)
        print('I am the parent, and after 5 seconds I kill my child\n')
        os.kill(newpid, signal.SIGUSR1)



numchilds=1
parent(numchilds)
