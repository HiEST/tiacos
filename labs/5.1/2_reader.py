import mmap
import os
import sys 
import time

RECORD_LEN=101
ID_LEN=50

try:
    fd_tmp = os.open(sys.argv[1].rstrip(),  os.O_RDWR)
except:
    print("Temporary file",sys.argv[1], "can not be open")
    sys.exit(0)


##PLACE the code here to:
# map the temporary file in a variable called 'map_tmp'


while 1:
  print("Contents:    ",map_tmp[0:RECORD_LEN-1])
  time.sleep(1)

os.close(fd_tmp)

