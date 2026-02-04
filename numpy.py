import numpy as np
import time

list_data = list(range(100_000))
start = time.time()
sum_list = [x *2 for x in list_data]
end = time.time()
print("Python list time:", end-start)

array_data = np.array(100_000)
start = time.time()
array_data = array_data * 2
end = time.time()
print("Numpy array time:", end-start)
#%%
