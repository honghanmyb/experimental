import matplotlib.pyplot as plt
import numpy as np

yearRates = [2, 3, 4, 5, 6, 7, 8, 9, 10]
x = np.arange(0, 360, 1)
for yearRate in yearRates:
    mRange = yearRate / 12 / 100
    y = x * mRange * (1 + mRange) ** x / ((1 + mRange) ** x - 1) - 1
    plt.plot(x, y, label ='Year Rate '+str(yearRate)+'%')
plt.yticks(np.arange(0, 2.5, 0.1))
plt.legend()
plt.xlabel("Months")
plt.ylabel("Total interest / principle")
plt.grid()
plt.show()
