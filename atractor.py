import numpy
import matplotlib
import matplotlib.pyplot


delta=0.01
t=100
sigma=10
beta=2.2667
rho=28
x0=0
y0=1
z0=1.05

t = range(101)
y = range (101)
x = range (101)
z = range (101)
y[0] = y0
x[0] = x0
z[0] = z0
for i in range(10*1000):
      x1=delta*(sigma*(y0-x0))
      y1=delta*(x0*(rho-z0)-y0)
      z1=delta*((x0*y0)-delta*z0)
      y0=y1
      x0=x1
      z0=z1
      
      x[i]=x1
      z[i]=z1
      t[i]=i*delta

ynew = numpy.array(y)
xnew = numpy.array(x)
znew = numpy.array(z)
tnew = numpy.array(t)

print ynew
print xnew
print znew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.plot(tnew,xnew)
matplotlib.pyplot.plot(tnew,znew)
matplotlib.pyplot.show()

matplotlib.pyplot.plot (znew,xnew)
matplotlib.pyplot.show()
