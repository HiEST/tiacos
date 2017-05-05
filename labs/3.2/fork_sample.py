import os

def child():
   print('\nThis is the child process. PID: ',  os.getpid())
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("This is the parent process. PID: %d, child PID: %d\n" % pids)
      break

parent()
