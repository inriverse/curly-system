import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider 

prob = 0.5
t= np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(6, 5))
plt.subplots_adjust(bottom=0.25)
ax.set_ylim(0, 3)
y = 1 - (1 - prob) ** t
l = plt.plot(t, y, lw=2)

ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'probability', 0.01, 0.99, valinit=prob)


def update(val):
    prob = slider.val
    l[0].set_ydata(1 - (1 - prob) ** t)
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
