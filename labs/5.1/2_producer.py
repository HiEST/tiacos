import mmap
import os
import sys 
import time

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
    fd_tmp = os.open(sys.argv[3].rstrip(), os.O_CREAT | os.O_TRUNC | os.O_RDWR)
except:
    print("Temporary file",sys.argv[3], "can not be created")
    sys.exit(0)

#we need to initialize the temporary file
os.write(fd_tmp, ('\x00' * mmap.PAGESIZE).encode())


## PLACE the code here to
# 1. map the input file (fastq)
# 2. map the temporary file
# 3. copy the contents of the record #RECORD from the source file to the temporary map
  
os.close(fd_source1)
os.close(fd_tmp)

