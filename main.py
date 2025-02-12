import matplotlib.pyplot as plt
import numpy as np
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.style.use('dark_background')
#Define the figure as 'fig' and axes as 'ax'.
fig, ax = plt.subplots()
xmin, xmax = -1.2, 1.2
ymin, ymax = -1.2, 1.2
depth = 10
points = 10

#Here where you choose the constants value c.
a, b = 0, 0
c = complex(a, b)

#a function is goingto be used for the steps.
def steps(axis):
    if axis == 'x':
        step = (xmax - xmin) / depth
        return step
    if axis == 'y':
        step = (ymax - ymin) / depth
        return step
    else:
        print('The input only can be x or y !!')

#A function mapps from a complex number z to z^2 + c, where c is a complex number too (Maybe Im(c)=0).
def F_z(z):
    return z**2 + c

#The Seq function make the animation of the point Ditribution for every z in The set of the Complex Numbers.
def Seq(re, im):
    ax.clear()
    x = np.arange(0, 2*np.pi, 2*np.pi/1000)
    ax.stackplot(np.cos(x), np.sin(x), color='white')
    ax.set_aspect('equal')
    ax.set_title(r'$z_{n+1}=z_{n}+c$')
    ax.set_xlabel(r'$\Re$')
    ax.set_ylabel(r'$\Im$')
    ax.set(xlim=[xmin, xmax + steps('x')], ylim=[ymin, ymax + steps('y')], 
           xticks=np.arange(xmin, xmax + steps('x'), steps('x')), 
           yticks=np.arange(ymin, ymax + steps('y'), steps('y')))
    r = ['left', 'right', 'top', 'bottom']
    for spine in r:
        ax.spines[spine].set(color='c', alpha=.9)
    plt.grid(which='both', color='gray', alpha=.6)
    plt.tight_layout()
    ax.scatter(0, 0, marker='.', alpha=.4)
    z = complex(re, im)
    ax.scatter(z.real, z.imag, color='red', marker='.', alpha=.9)
    for _ in range(points):
        ax.plot([z.real, F_z(z).real], [z.imag, F_z(z).imag], color='green', alpha=.7, lw=.5)
        z = F_z(z)
        ax.scatter(z.real, z.imag, color='c', marker='.', alpha=1)
    plt.draw()

# A method using pyplot from matplotlib to get the mouse's coordinates in the 'ax' object.
def mouse(event):
    if event.inaxes is not None:
        re = event.xdata
        im = event.ydata
        Seq(re, im)
fig.canvas.mpl_connect('motion_notify_event', mouse)

#Initial value of the first point.
Seq(0, 0)

plt.tight_layout()
plt.show()
