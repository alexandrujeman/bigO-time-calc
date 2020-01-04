import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import time

x = []
y = []
runs = 10000

for i in range(runs):
    start_time = time.time()
####### Function to be checked goes There(Passed data used is i from loop and array x which keep increasing after each loop) ########

    def binarySearch(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            potentialMatch = arr[middle]
            if target == potentialMatch:
                return middle
            elif target < potentialMatch:
                right = middle - 1
            else:
                left = middle + 1
        return

    binarySearch(x, i)
##########################################################
    y.append((time.time() - start_time) * 10000000)
    x.append(i)

# Attempt to smooth Y and X
npx_arr = np.array(x)
npy_arr = np.array(y)
x_smooth = np.linspace(npx_arr.min(), npx_arr.max(), 300)
spl = make_interp_spline(npx_arr, npy_arr, k=3)
y_smooth = spl(x_smooth)

# Show graph
plt.plot(x_smooth, y_smooth)
plt.title("Big O time")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
