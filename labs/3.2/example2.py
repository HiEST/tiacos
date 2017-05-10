import os
import sys

def child():
   print('\nThis is the child process. PID: ',  os.getpid())
   sys.exit(0)  

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


try:
   numchilds = int(sys.argv[1])
except:
   print ('First parameter must be a number', sys.argv[1])

print('Number of childs to create: ', numchilds)
parent(numchilds)
