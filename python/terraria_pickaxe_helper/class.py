def l2s(lst, sep = ', '): #Fancy list to string function
    return sep.join(map(str, lst))

class Pick: #class for pickaxes
    def __init__(self, id=0, ore=[], power=0, dmg=0, useT=0, mineS=0, kb=0, rar=0, sell=0, AxPwr=0):
        self.id = id #Internal Item IDentification (IIID/IID/ID)
        self.ore = l2s(ore) #max ore(s) that can be broken (and convert it fancily)
        self.power = power #pickaxe power
        self.dmg = dmg #damage
        self.useT = useT #use time
        self.mineS = mineS #mine speed
        self.kb = kb #knockback
        self.rar = rar #rarity
        self.sell = sell #sell value
        if AxPwr != 0: #if a value for axe power is set, change it for the new class(?)
            self.AxPwr = AxPwr

pickNames = ('Cactus Pickaxe','Copper Pickaxe','Tin Pickaxe','Iron Pickaxe','Lead Pickaxe','Silver Pickaxe',
'Bone Pickaxe','Tungsten Pickaxe','Candy Cane Pickaxe','Gold Pickaxe','Platinum Pickaxe','Nightmare Pickaxe',
'Deathbringer Pickaxe','Molten Pickaxe','Reaver Shark','Cobalt Pickaxe','Palladium Pickaxe','Mythril Pickaxe',
'Orichalcum Pickaxe','Adamantite Pickaxe','Titanium Pickaxe','Chlorophyte Pickaxe','Pickaxe Axe',
'Shroomite Digging Claw','Spectre Pickaxe','Picksaw','Nebula Pickaxe','Solar Flare Pickaxe','Stardust Pickaxe',
'Vortex Pickaxe') #All pickaxe names

#'legend' v\/v
#name = Pick(IID, ores, pickaxe power, damage, use time, mine speed, knockback, rarity, sell value, axe power[1])
#[1]: optional
cactus          = Pick(882, ['Gold', 'Platinum'], 35, 5, 23, 15, 2, 0, 400)
copper          = Pick(3509,['Gold', 'Platinum'], )
tin             = Pick(3503,['Gold', 'Platinum'], )
iron            = Pick(1,   ['Gold', 'Platinum'], )
lead            = Pick(3497,['Gold', 'Platinum'], )
silver          = Pick(3515,['Gold', 'Platinum'], )
bone            = Pick(1320,['Meteorite'], )
tungsten        = Pick(3491,['Meteorite'], )
candycane       = Pick(1917,['Crimtane', 'Demonite'], )
gold            = Pick(3521,['Crimtane', 'Demonite'], )
platinum        = Pick(3485,['Crimtane', 'Demonite'], )
nightmare       = Pick(103, ['Hellstone', 'Obsidian', 'Ebonstone', 'Crimstone', 'Desert Fossil', 'Dungeon Brick'], )
deathbringer    = Pick(798, ['Hellstone', 'Obsidian', 'Ebonstone', 'Crimstone', 'Desert Fossil', 'Dungeon Brick'], )
molten          = Pick(122, ['Cobalt', 'Palladium'], )
reavershark     = Pick(2341,['Cobalt', 'Palladium'], )
cobalt          = Pick(776, ['Mythril', 'Orichalcum'], )
palladium       = Pick(1188,['Mythril', 'Orichalcum'], )
mythril         = Pick(777, ['Adamantite', 'Titanium'], )
orichalcum      = Pick(1195,['Adamantite', 'Titanium'], )
adamantite      = Pick(778, ['Adamantite', 'Titanium'], )
titanium        = Pick(1202,['Adamantite', 'Titanium'], )
chlorophyte     = Pick(1230,['Chlorophyte'], )
pickaxe_axe     = Pick(990, ['Chlorophyte'], )
shroomiteDC     = Pick(2176,['Chlorophyte'], )
spectre         = Pick(1506,['Chlorophyte'], )
picksaw         = Pick(1294,['Lihzahrd Brick'], )
nebula          = Pick(2781,['Lihzahrd Brick'], )
solarflare      = Pick(2786,['Lihzahrd Brick'], )
stardust        = Pick(3466,['Lihzahrd Brick'], )
vortex          = Pick(2776,['Lihzahrd Brick'], )

picks = [cactus,copper,tin,iron,lead,silver,bone,tungsten,candycane,gold,platinum,nightmare,deathbringer,molten,reavershark,
cobalt,palladium,mythril,orichalcum,adamantite,titanium,chlorophyte,pickaxe_axe,shroomiteDC,spectre,picksaw,nebula,
solarflare,stardust,vortex] #put all pickaxe objects into a list for ease of future refrence

print(cactus.id)
print(cactus.ore)
print(vars(cactus))
for i in range(len(pickNames)):
    print(pickNames[i], "    vars:", vars(picks[i]))