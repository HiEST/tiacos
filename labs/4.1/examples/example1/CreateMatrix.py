import struct
import random
import os
import sys

# Checking parameters
# Usage CreateMatrix file rows columns
print('Number of arguments:', len(sys.argv), 'arguments.')

if (len(sys.argv) != 4):
    print("Error in th enumber of parameters. We need 1 file name")
    sys.exit(0)
else:
    file_name = sys.argv[1]
    print("Matrix result in file: ", file_name)

try:
    rows = int(sys.argv[2])
except:
    print("Rows (2nd parameter) needs to be a number")
    sys.exit(0)

try:
    cols = int(sys.argv[3])
except:
    print("Columns (3rd parameter) needs to be a number")
    sys.exit(0)

try:
    fd = os.open(file_name, os.O_CREAT|os.O_TRUNC|os.O_RDWR)
except:
    print("File", file_name, "cannot be created")
    sys.exit(0)

# wrting rows and cols
# bytes([num]) is a way to convert a byte into a bytestring type needed by write
os.write (fd, bytes([rows]))
os.write (fd, bytes([cols]))

# Creating and writing a random matrix
i = 0
while i < rows:
    j = 0
    while j < cols:
       val=random.randint(0, 100)
       os.write (fd, bytes([val]))
       print("(",i,",",j,")=",val)
       j = j +1
    i=i+1

os.close(fd)

