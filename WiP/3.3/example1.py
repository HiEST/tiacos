import os
import sys
import signal


def handler(signum, frame):
    global a
    a = a + 1
    print (a, 'Seconds') 
    if (a == 10):
       sys.exit(0)
    else:
       signal.alarm(1)

a = 0
signal.signal(signal.SIGALRM, handler)
signal.alarm(1)
while True:
	nop = 1

