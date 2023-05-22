from random import sample
from time import sleep
from console import fg, bg

def shuffle(cards):
    return sample(cards, k=len(cards))

def printCards(cards):
    for i in cards:
        if i[0] != 'w' and i[2].isdigit(): # if first char IS NOT equal to w AND third char IS a digit
            print( c_dict[ i[0] ], i[2] ) #print stuff
        elif i[0] != 'w' and not i[2].isdigit(): # if the first char IS NOT equal to w AND third char IS NOT a digit
            print( c_dict[ i[0] ], s_dict[ i[2] ] ) # print some more stuff
        else: # I'm not even going to for consistency
            print( s_dict[ i ] ) # aaahhhhhhhhh


#pl: dict = {
#    'cds' : {'r':[],'b':[],'g':[],'y':[]}
#}

# one 0 card
# two 1 cards
# two 2s, 3s, 4s, 5s, 6s, 7s, 8s and 9s
# two Draw Two cards
# two Skip cards
# and two Reverse cards
# --non color dependent:
# four Wild cards
# four Wild Draw Four cards

# cards: x=color (r,b,g or y)
# x-0,x-1,x-2,x-3,x-4,x-5,x-6,x-7,x-8,x-9
# x-r, x-s, x-d = reverse, skip, draw 2
# wld, wd4 = wild, wild draw 4
colors = ('r','b','g','y')
c_dict = {  # color dictionary
    'r' : 'Red',  
    'b' : 'Blue', 
    'g' : 'Green', 
    'y' : 'Yellow'
}
s_dict = { # special dictionary
    'r' : 'Reverse',
    's' : 'Skip',
    'd' : 'Draw Two',
    'wld' : 'Wild',
    'wd4' : 'Wild Draw Four'
}

mode, turn = 'play', 'pl'

p= {
    'c' : [],
    's' : 0
}

c= {
    'c' : [],
    's' : 0
}


dc = [] # Discard
deck = []
for co in range(4): #4 colors
    deck.append(colors[co]+'-0') # make one 0 card per color
    deck.append('wld') # make 4 Wild and Wild Draw Four cards
    deck.append('wd4')

    for i in range(2): # everything done here is done x2 per color
        deck.append(colors[co]+'-r') # reverse
        deck.append(colors[co]+'-s') # skip
        deck.append(colors[co]+'-d') # draw 2
        for n in range(1,10): # make a card for each number (except 0 & 10!):
            deck.append(colors[co]+'-'+str(n))
            

deck = shuffle(deck)
for _ in range(7): # give players cards
    p['c'].append(deck.pop())
    c['c'].append(deck.pop())
dc.append(deck.pop()) # start discard pile
p['c'].sort() # Sort player's hand


print(deck)
print(len(deck))

c['c'].sort()
print(c['c'])
print(p['c'])

print('\n\n\n')

print('Your cards:')
printCards(p['c'])



'''
while mode == 'play': # game loop
    while turn == 'pl':

        print("Player's turn is over")
        turn = 'pc'

    while turn == 'pc':
        print("PC's turn is over")
        turn = 'pl'
'''