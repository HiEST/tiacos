import struct
import random
import os
import sys

# Checking parameters
# Usage CreateVector file elements
print('Number of arguments:', len(sys.argv), 'arguments.')

if (len(sys.argv) != 3):
    print("Error in the number of parameters. We need 1 file name")
    sys.exit(0)
else:
    file_name = sys.argv[1]
    print("Matrix result in file: ", file_name)

try:
    rows = int(sys.argv[2])
except:
    print("Elements (2nd parameter) needs to be a number")
    sys.exit(0)

try:
    fd = os.open(file_name, os.O_CREAT|os.O_TRUNC|os.O_RDWR)
except:
    print("File", file_name, "cannot be created")
    sys.exit(0)


# Creating and writing a random matrix
i = 0
while i < rows:
    val=random.randint(0, 10)
    os.write (fd, bytes([val]))
    print(val)
    i=i+1

os.close(fd)

