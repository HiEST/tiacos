import mmap
import os
import sys 

RECORD_LEN=101
ID_LEN=50

try:
    fd_source1 = os.open(sys.argv[1].rstrip(), os.O_RDWR)
except:
    print("File",sys.argv[1], "not found")
    sys.exit(0)

try:
   RECORD = int(sys.argv[2])
except:
   print ('Second parameter must be an integer', sys.argv[2])
   sys.exit(0)

try:
   BASE = int(sys.argv[3])
except:
   print ('Third parameter must be an integer', sys.argv[3])
   sys.exit(0)


try:
   input = sys.argv[4]
   new_char = ord(input[0])
except:
   print ('Fourth parameter must be a BASE (A,C,T,G)', sys.argv[4])
   sys.exit(0)


if((new_char != ord('A')) and (new_char != ord('C')) and (new_char != ord('T')) and (new_char != ord('G'))):
   print ('Fourth parameter must be a BASE (A,C,T,G)', new_char)
   sys.exit(0)


## Place your mmap-based code here
