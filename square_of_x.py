import matplotlib.pyplot as plot

def f(x):
    square = x*x
    return square

xs = range(-100, 101)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
