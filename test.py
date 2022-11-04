import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

size = float(input("Size of square grid: "))
samples = int(input("Number of points in square grid: "))
function = str(input())

fig,ax=plt.subplots()
Axes = plt.axes(xlim=(-size, size), ylim=(-size, size))
Axes.set_aspect(0.8)

line, = plt.plot([],[], 'r.')

x = np.linspace(-size, size, samples)
y = np.linspace(-size, size, samples)
X,Y = np.meshgrid(x,y)
z = X + 1j * Y

def init():
    line.set_data([],[])
    
    return line,
def animate(i):
    
    q = z**(0.1*i)  # write the function here

    line.set_data(q.real, q.imag)
    plt.xlabel("Real")
    plt.ylabel("Imaginary")

    return line,

plt.axhline()  # Plots lines for axes
plt.axvline()


wm = plt.get_current_fig_manager()  # Maximizes Window
wm.window.state('zoomed')

# add keyword "frames=" in FuncAnimation to set number of frames for animation
animation = FuncAnimation(fig, animate, init_func=init, interval = 40, blit=False,repeat=False)

plt.show()

