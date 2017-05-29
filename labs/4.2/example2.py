import os
import sys

def maximum(v):
    cur_max = 0
    for i in v:
        if i>cur_max:
            cur_max = i
    return(cur_max)

vector = [1,5,6,2,4,1,19,245,32,19]
len_div3 = int(len(vector)/3)

# Pipe to receive partial result
(r, w) = os.pipe()

child = 0

while (child < 3):
    NewPiD = os.fork()
    if NewPiD == 0:
        # Child 0
        os.close (r)
        start = len_div3 * child
        end = len_div3 * (child + 1)
        if child == 2:
            end = len(vector) # To solve th eproblem of vectors that canot be evenly divided
        print("Child",child,"need to fin the maximum of this subvector",vector[start:end]) 
        my_max = maximum(vector[start:end])  
        print("Child",child,"the maximum is", my_max)  
        os.write(w,bytes([my_max]))
        
        os.close (w)
        sys.exit(0)
    else:
        child = child + 1

# Parent
os.close (w)
print("Parent: this is the whole vector to sort", vector)
result = 0
child = 0
while child < 3:
    chunk=os.read(r,1)
    if chunk[0]>result:
        result = chunk[0]
    print ("Parent: value received =", chunk[0], "current max =", result)
    child = child + 1

print ("Parent: MAX =", result)

os.close (r)
sys.exit(0)

