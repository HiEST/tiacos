import mmap
import os

MAP_LEN=60

map = mmap.mmap(-1, MAP_LEN)
map.write("Hello world!\n".encode())

pid = os.fork()

if pid == 0: # In a child process
    map.seek(0)
    print(map.readline())

    map.close()