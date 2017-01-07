import numpy as np
import matplotlib.pyplot as plt

objects = ['a','b','c']
incomes = [10,15,5]
# y_pos = np.arrange(len(objects))

plt.bar(objects, incomes)
# plt.xticks(y_pos, objects)
plt.show()