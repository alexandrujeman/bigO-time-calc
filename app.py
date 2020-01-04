import pandas as pd
import matplotlib.pyplot as plt
import time

x = []
y = []
incr = []

for i in range(20000):
    start_time = time.time()

    def twoSum(arr, targetSum):
        index = {}
        for i in range(len(arr)):
            potentialMatch = targetSum - arr[i]
            indexedMatch = index.get(potentialMatch)
            if indexedMatch == None:
                index[arr[i]] = i
            else:
                return [indexedMatch, i]
        return -1

    twoSum(incr, i)

    y.append(time.time() - start_time)
    incr.append(i)
    x.append(i)

plt.plot(x, y)
plt.title("testest plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()