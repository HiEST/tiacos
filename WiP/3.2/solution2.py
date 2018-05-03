import os
import sys
import time

def child(sibling):
   print('\nI am a child with PID', os.getpid(),'- my sibling is',sibling,'- and my parent is',os.getppid(),'\n')
   sys.exit(0)  

def parent(goal):
   num = 0
   sibling = 0
   while num < goal:
     num = num + 1
     newpid = os.fork()
     if newpid == 0:
        child(sibling)
     else:
        sibling = newpid
        pids = (os.getpid(), num, newpid)
        print("This is the parent process.\n")

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
i = 0
while i < len(sys.argv):
	print ('i-th parameter: ', sys.argv[i])
	i = i + 1 

try:
   numchilds = int(sys.argv[1])
except:
   print ('First parameter must be a number', sys.argv[1])

print('Number of childs to create: ', numchilds)
parent(numchilds)
