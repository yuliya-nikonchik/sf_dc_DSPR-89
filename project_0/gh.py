import numpy as np
arr = np.array([1,5,2,9,10])
print(arr.dtype)
print(2**16)

print(np.arange(5))

arr = np.linspace(1, 2, 10)
print(arr)

arr, step = np.linspace(-6, 21, 60, retstep=True, endpoint=False)
print(step)