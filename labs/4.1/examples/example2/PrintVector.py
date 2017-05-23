import struct
import random
import os
import sys

# Checking parameters
# Usage CreateMatrix file rows columns
print('Number of arguments:', len(sys.argv), 'arguments.')

if (len(sys.argv) != 2):
    print("Error in the number of parameters. We need 1 file name")
    sys.exit(0)
else:
    # The rstrip() is added because Python adds a charater \r to the last parameter and we need to remove it
    file_name = sys.argv[1].rstrip()
    print("Matrix result in file: ", file_name)

#Reading the file to make sure everything went well
try:
    fd = os.open(file_name, os.O_RDONLY)
except:
    print("File", file_name, "cannot be created")
    sys.exit(0)

# Reading the matrix
i = 0
chunk = os.read(fd,1)
while len(chunk) > 0:
    print(i,":",chunk[0])
    chunk = os.read(fd,1)
    i = i + 1
		
os.close(fd)

