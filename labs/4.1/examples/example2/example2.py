import os
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')

if (len(sys.argv) != 4):
    print("Error in th enumber of parameters. We need 3 file names.")
    sys.exit(0)
else:
    print("Matrix source in file: ", sys.argv[1])
    print("Matrix result in file: ", sys.argv[2])
    print("Value to search: ", sys.argv[3])

try:
    fd_source = os.open(sys.argv[1].rstrip(), os.O_RDONLY)
except:
    print("File",sys.argv[1], "not found")
    sys.exit(0)

try:
    fd_index = os.open(sys.argv[2].rstrip(), os.O_CREAT|os.O_WRONLY )
except:
    print("File",sys.argv[2], "cannot be created")
    sys.exit(0)

try:
    pattern = int(sys.argv[3])
except:
    print("3rd paramenter is not a number")
    sys.exit(0)



# Reading the matrix
chunk = os.read(fd_source,1)

while len(chunk) > 0:
    val = chunk[0]
    if (val == pattern):
	# remeber that after we have read the byte, the RW pointer has moved to the next position
        pos = os.lseek(fd_source, 0, os.SEEK_CUR) - 1
        print(pos, ":", pattern)
        os.write(fd_index,bytes([pos]))
    chunk = os.read(fd_source,1)
		
os.close(fd_source)
os.close(fd_index)

