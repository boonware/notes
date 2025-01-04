import numpy
from scipy.stats import norm, t
from matplotlib import pyplot


X = numpy.linspace(-4, 4, 200)

pyplot.title("Student's T-Distribution - Probability Density Function")
pyplot.xlabel('t')
pyplot.ylabel(r'f(t|$\nu$)')

Y = norm.pdf(X)
pyplot.plot(X, Y, marker='none', color='green', label='Normal distribution', linestyle='solid', markersize=1, linewidth=0.5)

Y = t.pdf(X, df=5)
pyplot.plot(X, Y, marker='none', color='blue', label=r'$\nu = 5$', linestyle='solid', markersize=1, linewidth=0.5)

Y = t.pdf(X, df=10)
pyplot.plot(X, Y, marker='none', color='black', label=r'$\nu = 10$', linestyle='solid', markersize=1, linewidth=0.5)

pyplot.legend(loc='upper left')
#pyplot.savefig('t-distribution.png')
pyplot.show()
pyplot.close()
