import os
import sys
import random
import array

def fill_vector(vector, size):
   i = 0
   while i < size:
      vector.append(int(random.random()*100))
      i = i + 1
   print (vector)

def child(vector, start, end):
   max = 0
   original_start = start
   while start < end:
      if vector[start] > max:
         max = vector[start]
      start = start + 1
   print('\nThe Maximum in [', original_start,',',end-1,'] is ',max,'\n')
   sys.exit(max)  

def parent(vectorsize, goal):
   vector = []
   elems = int(vectorsize/goal)
   fill_vector(vector, vectorsize)
   num = 0;
   while num < goal:
     num = num + 1
     newpid = os.fork()
     if newpid == 0:
        if goal == num:
           child(vector, (num-1)*elems, vectorsize)
        else:
           child(vector, (num-1)*elems, num*elems)
     else:
        pids = (os.getpid(), num, newpid)
        print("This is the parent process.\n")
   num = 0
   max = 0
   while num < goal:
     num = num + 1
     (pid, status) = os.wait()
     print (pid,status, os.WEXITSTATUS(status))
     if max < os.WEXITSTATUS(status):
        max = os.WEXITSTATUS(status)
   print('\nThe absolute maximum is', max,'\n')

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
i = 0
while i < len(sys.argv):
	print ('i-th parameter: ', sys.argv[i])
	i = i + 1 

try:
   numchilds = int(sys.argv[2])
except:
   print ('First parameter must be a number', sys.argv[2])

try:
   vectorsize = int(sys.argv[1])
except:
   print ('First parameter must be a number', sys.argv[1])

print('Size of the vector ro create: ', vectorsize)
print('Number of childs to create: ', numchilds)
parent(vectorsize, numchilds)
