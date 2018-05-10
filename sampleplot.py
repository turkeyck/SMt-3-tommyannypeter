import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
T = 0.1
#P = np.arange(0.01, 2.0, 0.01)
P = np.linspace(0.01, 2.0, 200)
V = T/P

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(P, V, '-*r', label='T=0.1')

ax.set(xlabel='P (some unit)', ylabel='V (some unit)',
       title='PV curve for ideal gas')
ax.legend()
ax.grid()

fig.savefig("test.png")
plt.show()
