import time
import numpy as np

rows = 10000
columns = 10000
np.random.seed(0)

print("\nStarting Matrix generation")
MyMatrix = np.random.rand(rows, columns)
print(" Matrix generated with %d elements\n" % (rows*columns))

sum = 0;
items = 0;

print("Starting processing by Rows... can take up to a minute to complete")
start_time = time.time()
for r in range(0, rows):
  for c in range(0, columns):
    sum = sum + MyMatrix[r,c]
    items = items +1
elapsed_time = time.time() - start_time
print(" Time by Rows: %d items with a final value of %f in %.3f\n" % (items, sum, elapsed_time))

sum = 0;
items = 0;

print("Starting processing by Columns... can take up to a minute to complete")
start_time = time.time()
for c in range(0, columns):
  for r in range(0, rows):
    sum = sum + MyMatrix[r,c]
    items = items +1
elapsed_time = time.time() - start_time
print(" Time by Columns: %d items with a final value of %f in %.3f\n" % (items, sum, elapsed_time))

