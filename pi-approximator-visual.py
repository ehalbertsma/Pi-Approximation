import matplotlib.pyplot as plt
import numpy.random as rd
from numpy import zeros

# shapes
square = plt.Rectangle((-1, -1), 2,2,color='brown')
circle = plt.Circle((0, 0), 1,color='blue')

fig, ax = plt.subplots()
ax.set(xlim=(-1, 1), ylim = (-1, 1))

ax.add_artist(square)
ax.add_artist(circle)

# points
n = 1000
x = zeros((n,1))
y = zeros((n,1))
for i in range(n):
    x[i] = rd.random()
    y[i] = rd.random()

ax.plot(x,y,'o',color='black',markersize=1)


plt.gcf().set_size_inches(5,5)
plt.savefig("out.png",dpi=100)
