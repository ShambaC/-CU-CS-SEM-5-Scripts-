import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 3, 4, 5]

plt.subplot(1, 2, 1)
plt.plot(x, y, 'o')

x = [2, 3, 4, 5]
y = [3, 4, 5, 6]

plt.subplot(1, 2, 2)
plt.plot(x, y, 'o')

plt.show()