from scipy import linspace, polyval, polyfit, sqrt, stats, randn
import matplotlib.pyplot as plt

n = 50

t = linspace(-5, 5, n)

a = 0.8; b = -4.0

x = polyval([a, b], t)
x_n = x + randn(n)

(ar,br)=polyfit(t,x_n,1)
xr=polyval([ar,br],t)
err = sqrt(sum(xr-x_n)**2/n)

print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a,b,ar,br,err))

plt.title('Linear Regression Example')
plt.plot(t,x,'g.--')
plt.plot(t,x_n,'k.')
plt.plot(t,xr,'r.-')
plt.legend(['original','plus noise', 'regression'])

plt.show()