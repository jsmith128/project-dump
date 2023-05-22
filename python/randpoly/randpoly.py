import math
from random import randint, sample
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

from numpy import deg2rad


poly = []

stepsize = 18
randomness = 25


for i in range(0, 360, stepsize):
	rad = deg2rad(i)
	x = math.sin(rad)
	y = math.cos(rad)

	x += randint(-randomness,randomness) / 100
	y += randint(-randomness,randomness) / 100

	poly.append([x,y])


polygon = Polygon(poly)

fig, ax = plt.subplots(1,1)
ax.add_patch(polygon)

plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()


# class country:
# 	def __init__(self):
# 		pass

# class province:
# 	def __init__(self):
# 		pass

# class street:
# 	def __init__(self):
# 		self.name = "Streetname"

# 		pass


# class user:
# 	def __init__(self, name: str, street: street):
# 		pass