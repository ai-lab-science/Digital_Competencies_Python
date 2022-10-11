import numpy
import matplotlib.pyplot as plt

omega = 1
x = numpy.linspace(0, 4*numpy.pi, 200)
cos = numpy.cos(omega*x)
sin = numpy.sin(omega*x)

plt.figure()
plt.plot(x, cos, label='cos(x)')
plt.plot(x, sin, label='sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()