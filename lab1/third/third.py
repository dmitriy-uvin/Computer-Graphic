import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

variant = 25

y1 = lambda x: (2 * variant * 0.01) * np.sin(x)
y2 = lambda x: (3 * variant * 0.01) * np.sin(x)
y3 = lambda x: (4 * variant * 0.01) * np.sin(x)

ax = plt.gca()

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
plt.title("Dependencies y1, y2, y3")
x = np.linspace(0, 20, 200)
plt.xlabel("x")
plt.ylabel("y1, y2, y3")

plt.plot(x, y1(x), x, y2(x), x, y3(x))

plt.show()
