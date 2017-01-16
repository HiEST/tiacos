import time
import numpy as np

rows = 1000
columns = 1000

MyMatrix = np.random.rand(rows, columns)

sum = 0;
items = 0;

start_time = time.time()
for r in range(0, rows):
  for c in range(0, columns):
    sum = sum + MyMatrix[r,c]
    items = items +1
elapsed_time = time.time() - start_time
print "Time by Rows: %d items with a final valu of %f in %.3f" % (items, sum, elapsed_time)

sum = 0;
items = 0;

start_time = time.time()
for c in range(0, columns):
  for r in range(0, rows):
    sum = sum + MyMatrix[r,c]
    items = items +1
elapsed_time = time.time() - start_time
print "Time by Columns: %d items with a final valu of %f in %.3f" % (items, sum, elapsed_time)

