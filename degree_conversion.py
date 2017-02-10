import matplotlib.pyplot as plot
from numpy import arange
import math

def f(x):
    temperature = ((x * 9)/5) + 32
    return temperature

xs = arange(0, 30, 0.1)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
