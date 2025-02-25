# -*- coding: utf-8 -*-
"""Untitled.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mC6kf7ZK8XDjV1nglqUVDciWcykkvSZP
"""

import numpy as np
a=np.array([1,2,3,4,5])
for i in range(0,5):
     a[i]= a[i]+2

print(a)

import numpy as np
a=np.array([1,2,3,4,5])
for i in range(0,5):
     a[i]= a[i]*3

print(a)

import numpy as np
a=np.array([1,2,3,4,5])
for i in range(0,5):
     a[i]= a[i]/2

print(a)

#Question 2 a)
import numpy as np
arr=np.array([1,2,3,6,5,4])
arr=np.flip(arr)
print(arr)

#Question 2 b)
import numpy as np
x=np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1,1,1,2,3,4,2,4,3,3])
def most_frequent(arr):
    values, counts = np.unique(arr, return_counts=True)
    most_frequent_value = values[np.argmax(counts)]
    indices = np.where(arr == most_frequent_value)[0]
    return most_frequent_value, indices

most_frequent_x, indices_x = most_frequent(x)
most_frequent_y, indices_y = most_frequent(y)
print(most_frequent_x, indices_x)
print(most_frequent_y, indices_y )

#Question 3
import numpy as np
arr=np.array([[10, 20, 30],
 [40, 50, 60],
  [70, 80, 90]])
print(arr[0,1])
print(arr[2,0])

#Question 4
import numpy as np
Ishant= np.linspace(10,100,25)
dimension = Ishant.ndim
print(dimension)
shapee = Ishant.shape
print(shapee)
total_ele = Ishant.size
print(total_ele)
data_type = Ishant.dtype
print(data_type)
byte = Ishant.nbytes
print(byte)
transpose = Ishant.reshape(25,1)
print(transpose)
transposed_array = Ishant.T
print(transposed_array)
print("\nUsing .T on a 1-D array has no effect, as NumPy treats it as the same array.")

#Question 5
import numpy as np

ucs420_Ishant = np.array([[10, 20, 30, 40],
                            [50, 60, 70, 80],
                            [90, 15, 20, 35]])

mean_value = np.mean(ucs420_Ishant)
median_value = np.median(ucs420_Ishant)
max_value = np.max(ucs420_Ishant)
min_value = np.min(ucs420_Ishant)
unique_elements = np.unique(ucs420_Ishant)

reshaped_ucs420_Ishant = ucs420_Ishant.reshape(4, 3)

resized_ucs420_Ishant = np.resize(ucs420_Ishant, (2, 3))

print("Mean:", mean_value)
print("Median:", median_value)
print("Max:", max_value)
print("Min:", min_value)
print("Unique Elements:", unique_elements)
print("Reshaped Array (4x3):\n", reshaped_ucs420_Ishant)
print("Resized Array (2x3):\n", resized_ucs420_Ishant)