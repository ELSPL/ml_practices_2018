#!/usr/bin/python

from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open("plotxylist.txt",'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)

#update graph function every 1 second on fig
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()