import time
import numpy as np

rows = 100000
columns = 10000

MyMatrix = np.random.rand(rows, columns)

start_time = time.time()
sum = np.sum(MyMatrix, axis=0)
elapsed_time = time.time() - start_time
print "By Columns: result = %f, time = %.3f" % (np.sum(sum), elapsed_time)

start_time = time.time()
sum = np.sum(MyMatrix, axis=1)
elapsed_time = time.time() - start_time
print "By Rows: result = %f, time = %.3f" % (np.sum(sum), elapsed_time)

