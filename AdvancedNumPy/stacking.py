"""
verticaly 
horizontaly

vstack() row wise
hstack() column wise
"""
import numpy as np

arr1 = np.array([1,4,7])
arr2 = np.array([4,7,9])

print(np.vstack((arr1,arr2)))#vertically stack
print(np.hstack(((arr1,arr2))))#horizontaly 
