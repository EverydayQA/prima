
import numpy as np
import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c', 'group_d']
values = [-1.0, -1.5,2.5, -3.0 ]

plt.figure(figsize=(20, 6))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
