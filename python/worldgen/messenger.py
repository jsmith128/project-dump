import math
from os import system
from random import randint, choice
from pynput import keyboard
from time import time

from names import Names
names = Names()

localenames = {
	"street": ["Aalto Place", "Chestnut Terrace", "Christi Court", "Del Mar Drive", "Hibiscus Drive", "Gentle Terrace", "Gina Place"],
}

system("")  # enables ansi escape characters in terminal

class Directory:
	def directory(self, listt, selector:int, scroll:int, lines:int):
		printBuffer = "" # For avoiding long waits between cls and print
		printBuffer += self.name+":"+"\t\t"+str(selector+1)+"/"+str(len(listt)) +'\n'
		if lines > len(listt): # make sure we dont go outside of list
			lines = len(listt)

		for i in range(lines):
			i+=scroll #add scroll to get scroll effect
			if (i != selector):
				printBuffer += "\t"+listt[i].name +'\n'
			else:
				printBuffer += "\t> "+listt[i].name+" <" +'\n'
		return printBuffer

class World(Directory):
	def __init__(self):
		self.parent = self # has no parent
		self.name = "Earth"
		self.countries = []
	def getlist(self):
		return self.countries


class Country(Directory):
	def __init__(self, parent):
		self.parent = parent
		self.name = choice(names.Country)
		self.states = []
	def getlist(self):
		return self.states

class State(Directory):
	def __init__(self, parent):
		self.parent = parent
		self.name = choice(names.State)
		self.cities = []
	def getlist(self):
		return self.cities


class City(Directory):
	def __init__(self, parent):
		self.parent = parent
		self.name = choice(names.City)
		self.streets = []
	def getlist(self):
		return self.streets


class Street(Directory):
	def __init__(self, parent):
		self.parent = parent
		self.name = choice(localenames["street"])
		self.houses = []
	def getlist(self):
		return self.houses

class House(Directory):
	def __init__(self, housenum:int, parent):
		self.parent = parent
		self.name = str(housenum)
		self.residents = []
	def getlist(self):
		return self.residents

class Human:
	def __init__(self, parent):
		self.parent = parent
		self.name = ""
		if randint(0,1):
			self.name = choice(names.Male)
		else:
			self.name = choice(names.Female)
	def stats(self):
		printBuffer = ""
		printBuffer += self.name +'\n'
		printBuffer += "Lives in house #" + self.parent +'\n'

		return printBuffer



class Browser:
	def __init__(self, lines, inittarget):
		self.sel = 0
		self.scroll = 0
		self.lines = lines
		self.maxlines = len(inittarget.getlist())

		self.lastaction = time()
		self.actrate = 0.1

		self.target = inittarget
		system("cls")
	def render(self, sel:int, scroll:int, lines:int):
		
		printBuffer = ""
		# if (type(self.target) == Human):
		# 	printBuffer = self.target.stats()
		# else:
		printBuffer = self.target.directory(self.target.getlist(), sel, scroll, lines)

		#print("\033[F"*23)
		system('cls') #consider adding print counter. once hits certan value then clear screen. or never cls
		print( printBuffer )

	# cmd: u= up, d= down, s= select, b= back
	def move(self, cmd:str):
		# Avoiding terrible flickering when holding arrow
		if time() < self.lastaction + self.actrate:
			return
		self.lastaction = time()

		if cmd == "s":
			if type(self.target.getlist()[self.sel]) != Human:
				self.target.savedsel = self.sel
				self.setTarget( self.target.getlist()[self.sel]	)


		if cmd == "b":
			self.setTarget( self.target.parent )

		else:
			if cmd == "u":
				self.sel -= 1
			elif cmd == "d":
				self.sel += 1

		if self.sel < 0: self.sel = 0
		if self.sel > self.maxlines-1: self.sel = self.maxlines -1


		mid = self.lines//2 +self.scroll

		self.scroll = self.sel - self.lines//2

		if self.scroll + self.lines >= self.maxlines: self.scroll = self.maxlines - self.lines
		if self.scroll < 0: self.scroll = 0

		# print(self.target)

		self.render(self.sel, self.scroll, self.lines)

	def setTarget(self, newtarget):
		self.target.savedsel = self.sel
		if hasattr(newtarget, "savedsel"):
			self.sel = newtarget.savedsel
		else:
			self.sel = 0
		self.maxlines = len(newtarget.getlist())
		self.scroll	= 0
		self.target = newtarget


world = World()

n_countries = randint(3,5)

min_states = 10
max_states = 30

min_cities = 20
max_cities = 20

min_streets = 10
max_streets = 10

min_houses = 1
max_houses = 5

min_residents = 1
max_residents = 2

c=0

for i in range(n_countries):
	c+=1
	country = Country(world)
	world.countries.append(country)
	for i in range(randint(min_states, max_states)):
		c+=1
		state = State(country)
		country.states.append(state)
		for i in range(randint(min_cities, max_cities)):
			c+=1
			city = City(state)
			state.cities.append(city)
			for i in range(randint(min_streets, max_streets)):
				c+=1
				street = Street(city)
				city.streets.append(street)
				numstart = randint(10,24)*100
				for i in range(randint(min_houses, max_houses)):
					c+=1
					house = House(numstart + i, street)
					street.houses.append(house)
					for i in range(randint(min_residents, max_residents)):
						c+=1
						resident = Human(house)
						house.residents.append(resident)




browser = Browser(20, world)
browser.setTarget(world)
browser.render(0, 0, 20) #force a render
print(str(c) + " items created.")
# while True:
# 	inp = input()
# 	cmd = ""
# 	if inp == "w": cmd = "u"
# 	if inp == "s": cmd = "d"
# 	if inp == "d": cmd = "s"
# 	if inp == "a": cmd = "b"
# 	browser.move(cmd)

def on_press(key):
    cmd = None
    if (key == keyboard.Key.up):
    	cmd = "u"
    elif (key == keyboard.Key.down):
    	cmd = "d"
    elif (key == keyboard.Key.left):
    	cmd = "b"
    elif (key == keyboard.Key.right):
    	cmd = "s"

    if (cmd != None):
    	browser.move(cmd)


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()