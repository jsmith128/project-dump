import matplotlib.pyplot as plot
one = [(0, 1), (2, 4)]
redstone = []


fig, ax = plot.subplots()

ax.barh(10, 1, 15, 0, color=('tab:blue'))


ax.set_xlim(0, 7)
ax.set_xlabel('ore')

ax.set_ylim(0, 255)
ax.set_ylabel('depth')

ax.set_yticks(range(0, 256, 15))
ax.set_yticklabels(range(0, 256, 15))
ax.grid(True)
ax.set_title('t')
plot.show()