import os
import sys

def child():
   os.execl('/usr/bin/python3', '/usr/bin/python3', '/home/ubuntu/labs/3.2/print_pid.py')

def parent(goal):
   num = 0;
   while num < goal:
     num = num + 1
     newpid = os.fork()
     if newpid == 0:
        child()
     else:
        pids = (os.getpid(), num, newpid)
        print("This is the parent process. PID: %d, child #%d - PID: %d\n" %  pids)


try:
   numchilds = int(sys.argv[1])
except:
   print ('First parameter must be a number', sys.argv[1])

print('Number of childs to create: ', numchilds)
parent(numchilds)
