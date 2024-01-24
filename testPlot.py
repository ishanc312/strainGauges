import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import random

x_temp = [1]
y_temp = [3]

def updateValues():
    x_temp.append(x_temp[len(x_temp) - 1] + 1)
    y_temp.append(y_temp[len(y_temp) - 1] + 3 * random())
def plot(frame):
    updateValues()
    plt.cla()
    plt.plot(x_temp, y_temp, label = 'Values', color='green')
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.legend()

fig, ax = plt.subplots()
animation = FuncAnimation(fig, plot, frames=60, interval=1000)
plt.show()

