import matplotlib.pyplot as plot
from numpy import *

ores = ['Coal', 'Iron', 'Gold', 'Redstone', 'silly jillies', 'Lapis', 'Emerald', 'Lava', 'Bedrock']
fig, ax = plot.subplots()


ax.bar(0.5, 256, 0.8, 0, color='black') #coal 0-256
ax.bar(1.5, 64, 0.8, 0, color='#E5BA9C') #iron 0-64
ax.bar(2.5, 32, 0.8, 0, color='gold') #gold 0-32
ax.bar(3.5, 16, 0.8, 0, color='red') #redstone 0-16
ax.bar(4.5, 8, 0.8, 8, color='#7FFFFF') #diamond 8-16
ax.bar(5.5, 8, 0.8, 8, color='#0126FA') #lapis 8-16
ax.bar(6.5, 28, 0.8, 4, color='#00FF00') #emerald 4-32
ax.bar(7.5, 10, 0.8, 0, color='#FF5F00') #lava  0-10
ax.bar(8.5, 4, 0.8, 0, color='#434343') #bedrock 0-4
ax.bar(4.5, 6, 9, 10, color='none', edgecolor='purple') #best mining depth 10-16
ax.annotate('Best mining depth', xy=(8.5, 17), xytext=(8, 55),
    arrowprops=dict(facecolor='purple', shrink=0.05),
    horizontalalignment='right'
    )

ax.set_xlim(0, 9)
ax.set_xticks(arange(0.5, 9, 1))
ax.set_xticklabels(ores)

ax.set_xlabel('ORE', color='red')

ax.set_ylim(0, 256)
ax.set_ylabel('DEPTH', color='red')

ax.set_yticks(range(0, 257, 16))
ax.set_yticklabels(range(0, 257, 16))

#ax.grid(True)
ax.yaxis.grid(color='black', linestyle=(0, (5, 10)), linewidth=0.5)

ax.set_title('Depths of Ores in Minecraft')
plot.show()
#plot.gca().set_position([0, 0, 1, 1])
#plot.savefig("test.svg")