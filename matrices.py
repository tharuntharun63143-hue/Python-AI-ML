#3x3 array
import numpy as np
arr1 = np.array(["fruits","vegetable"])
arr2 = np.array(5)
print("fruits" + "vegetable")
print(arr2 * 5)

#indexing
arr3 = np.array([
                 [2,3,4,5],
                 [6,7,8,9],
                 [10,11,12,13]])
print("first row:", arr3[0])
print("second row:", arr3[1])
print("third row:", arr3[2])

#slicing
print("first column:", arr3[0:3])
print("second column:", arr3[:0])



