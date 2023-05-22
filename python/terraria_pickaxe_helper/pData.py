def l2s(lst, sep = ', '): #Fancy list to string function
    return sep.join(map(str, lst))

class Pick: #class for pickaxes
    def __init__(self, id=0, ore=[], power=0, dmg=0, useT=0, mineS=0, kb=0,
    rar=0, sell=['p','g','s','c'], bonus='', AxPwr=0):
        self.id = id #Internal Item IDentification (IIID/IID/ID)
        self.ore = l2s(ore) #max ore(s) that can be broken (and convert it fancily)
        self.power = power #pickaxe power
        self.dmg = dmg #damage
        self.useT = useT #use time
        self.mineS = mineS #mine speed
        self.kb = kb #knockback
        self.rar = rar #rarity
        # if only 3 types of coins are added, a 0 for copper coins is added b/c most
        # items that don't sell for more than a silver do not have copper value too
        if len(sell) == 3: 
            self.sell = sell.append(0)
        else:
            self.sell = sell #sell value [platinum, gold, silver, copper]

        if bonus != '':# if a value is given for bonus, set it for the new object
            self.bonus = bonus
        if AxPwr != 0: # if a value for axe power is set, set it for the new object(?)
            self.AxPwr = AxPwr

pickNames = ('Cactus Pickaxe','Copper Pickaxe','Tin Pickaxe','Iron Pickaxe','Lead Pickaxe','Silver Pickaxe',
'Bone Pickaxe','Tungsten Pickaxe','Candy Cane Pickaxe','Gold Pickaxe','Platinum Pickaxe','Nightmare Pickaxe',
'Deathbringer Pickaxe','Molten Pickaxe','Reaver Shark','Cobalt Pickaxe','Palladium Pickaxe','Mythril Pickaxe',
'Orichalcum Pickaxe','Adamantite Pickaxe','Titanium Pickaxe','Chlorophyte Pickaxe','Pickaxe Axe',
'Shroomite Digging Claw','Spectre Pickaxe','Picksaw','Nebula Pickaxe','Solar Flare Pickaxe','Stardust Pickaxe',
'Vortex Pickaxe') #All pickaxe names

# rarities:
# -1=Gray, 0=White, 1=Blue, 2=Green, 3=Orange, 4=Light Red, 5=Pink, 6=Light Purple, 7=Lime,
# 8=Yellow, 9=Cyan, 10=Red, 11=Purple 
# (Expert) -12=Rainbow, (Quest) -11=Amber

# use times: (inclusive)
# <8 Insanely Fast
# 9-20 Very Fast
# 21-25 Fast
# 26-30 Average
# 31-35 Slow
# 36-45 Very Slow
# 46-55 Extremely Slow
# >56 Snail

# name = Pick(IID, ores, pickaxe power, damage, use time, mine speed, knockback, rarity, sell value, axe power[1])
# [1]: optional
cactus          = Pick(882, ['Gold', 'Platinum'], 35, 5, 23, 15, 2, 0, [0,0,4])
copper          = Pick(3509,['Gold', 'Platinum'], 35, 4, 23, 15, 2, 0, [0,0,1], '-1 range')
tin             = Pick(3503,['Gold', 'Platinum'], 35, 5, 21, 14, 2, 0, [0,0,1,50])
iron            = Pick(1,   ['Gold', 'Platinum'], 40, 5, 20, 13, 2, 0, [0,0,4])
lead            = Pick(3497,['Gold', 'Platinum'], 43, 6, 19, 12, 2, 0, [0,0,6])
silver          = Pick(3515,['Gold', 'Platinum'], 45, 6, 19, 11, 2, 0, [0,0,10])
bone            = Pick(1320,['Meteorite'], 50, 8, 19, 11, 3, 1, [0,0,30])
tungsten        = Pick(3491,['Meteorite'], 50, 6, 21, 19, 2, 0, [0,0,15])
candycane       = Pick(1917,['Crimtane', 'Demonite'], 55, 7, 20, 16, 2.5, 0, [0,0,20])
gold            = Pick(3521,['Crimtane', 'Demonite'], 55, 6, 20, 17, 2, 0, [0,0,20])
platinum        = Pick(3485,['Crimtane', 'Demonite'], 59, 7, 19, 15, 2, 0, [0,0,30])
nightmare       = Pick(103, ['Hellstone', 'Obsidian', 'Ebonstone', 'Crimstone', 'Desert Fossil',\
'Dungeon Brick'], 65, 9, 20, 15, 3, 1, [0,0,36])
deathbringer    = Pick(798, ['Hellstone', 'Obsidian', 'Ebonstone', 'Crimstone', 'Desert Fossil',\
'Dungeon Brick'], 70, 12, 22, 14, 3.5, 1, [0,0,36])
molten          = Pick(122, ['Cobalt', 'Palladium'], 100, 12, 23, 18, 2, 3, [0,0,54])
reavershark     = Pick(2341,['Cobalt', 'Palladium'], 100, 16, 22, 18, 3, 3, [0,1,50])
cobalt          = Pick(776, ['Mythril', 'Orichalcum'], 110, 10, 25, 13, 5, 4, [0,1,8])
palladium       = Pick(1188,['Mythril', 'Orichalcum'], 130, 12, 25, 11, 5, 4, [0,1,44])
mythril         = Pick(777, ['Adamantite', 'Titanium'], 150, 15, 25, 10, 5, 4, [0,1,62])
orichalcum      = Pick(1195,['Adamantite', 'Titanium'], 165, 17, 25, 8, 5, 4, [0,1,98])
orichalcumD     = Pick(1196,['Adamantite', 'Titanium'], 165, 17, 25, 10, 5, 4, [0,1,98])
adamantite      = Pick(778, ['Adamantite', 'Titanium'], 180, 20, 25, 7, 5, 4, [0,2,16])
titanium        = Pick(1202,['Adamantite', 'Titanium'], 190, 27, 25, 7, 5, 4, [0,2,52])
chlorophyte     = Pick(1230,['Chlorophyte'], 200, 40, 25, 7, 5, 7, [0,4,32], '+1 range')
pickaxe_axe     = Pick(990, ['Chlorophyte'], 200, 35, 25, 7, 4.75, 4, [0,4,40], AxPwr=110)
shroomiteDC     = Pick(2176,['Chlorophyte'], 200, 45, 12, 4, 6, 8, [0,1,0], '-1 range', 125)
spectre         = Pick(1506,['Chlorophyte'], 200, 32, 24, 10, 5.25, 8, [0,4,32], '+3 range')
picksaw         = Pick(1294,['Lihzahrd Brick'], 210, 34, 16, 6, 5.5, 7, [0,4,32], '+1 range', 125)
nebula          = Pick(2781,['Lihzahrd Brick'], 225, 80, 12, 6, 5.5, 10, [0,5,0], '+4 range')
solarflare      = Pick(2786,['Lihzahrd Brick'], 225, 80, 12, 6, 5.5, 10, [0,5,0], '+4 range')
stardust        = Pick(3466,['Lihzahrd Brick'], 225, 80, 12, 6, 5.5, 10, [0,5,0], '+4 range')
vortex          = Pick(2776,['Lihzahrd Brick'], 225, 80, 12, 6, 5.5, 10, [0,5,0], '+4 range')

picks = [cactus,copper,tin,iron,lead,silver,bone,tungsten,candycane,gold,platinum,nightmare,deathbringer,molten,reavershark,
cobalt,palladium,mythril,orichalcum,adamantite,titanium,chlorophyte,pickaxe_axe,shroomiteDC,spectre,picksaw,nebula,
solarflare,stardust,vortex] #put all pickaxe objects into a list for ease of future refrence

items = [ #items[0] == picks, items[1] == mineable ores, items[2] == crafting ingredients
    ['cactus','copper','tin','iron','lead','silver','bone','tungsten','candycane',
    'gold','platinum','nightmare','deathbringer','molten','reavershark','cobalt','palladium',
    'mythril','orichalcum','adamantite','titanium','chlorophyte','pickaxe_axe','shroomiteDC',
    'spectre','picksaw','nebula','solarflare','stardust','vortex'],

]


'''
print(cactus.id)
print(cactus.ore)
print(vars(cactus))
for i in range(len(pickNames)):
    print(pickNames[i], "    vars:", vars(picks[i]))'''

def listItems(mode=0):
    if mode == 0:
        print(l2s(items))
    if mode == 1:
        print( l2s(items[1]) )




print(l2s(items))