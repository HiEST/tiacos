import math
import os
import sys

def atoi ( ascii_num ):
    val = 0
    for c in ascii_num:
        val = val * 10 + (c - ord('0'))
    return val;

def itoa ( val ):
    c = math.floor(val/100)
    d = math.floor((val-c*100)/10)
    u = val - c*100 - d*10
    ascii_num = "%d%d%d" % (c,d,u)
    return ascii_num.encode();

print('Number of arguments:', len(sys.argv), 'arguments.')

if (len(sys.argv) != 3):
    print("We need 2 file names")
    sys.exit(0)
else:
    print("Source file: ", sys.argv[1])
    print("Text file: ", sys.argv[2])

try:
    fd_source = os.open(sys.argv[1].rstrip(), os.O_RDONLY)
except:
    print("File",sys.argv[1], "not found")
    sys.exit(0)

try:
    fd_bin = os.open(sys.argv[2].rstrip(), os.O_CREAT|os.O_TRUNC|os.O_WRONLY)
except:
    print("File",sys.argv[2], "not found")
    sys.exit(0)


# Reading the matrix
chunk = os.read(fd_source,1)

while len(chunk) > 0:
    print (chunk[0], itoa(chunk[0]));
    os.write(fd_bin, itoa(chunk[0]))
    os.write(fd_bin, bytes([10]))
    chunk = os.read(fd_source,1)
		
os.close(fd_source)
os.close(fd_bin)

