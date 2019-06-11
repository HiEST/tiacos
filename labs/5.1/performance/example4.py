import mmap
import os
import sys 

MAP_LEN=60

try:
    fd_source1 = os.open(sys.argv[1].rstrip(), os.O_RDWR)
except:
    print("File",sys.argv[1], "not found")
    sys.exit(0)


map = mmap.mmap(fd_source1, 0)
len = map.size() 

print("Total length of the mapped file:",len,"bytes")

i = 0
while i < map.size():
	print("Reading contents of the range:",(i+0),"-",(i+3))
	print("Contents:",map[i+0:i+3])
	i = i + 4

os.close(fd_source1)
