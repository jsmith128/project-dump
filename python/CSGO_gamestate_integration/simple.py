from flask import Flask, request
from tqdm import tqdm
from time import sleep
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#TODO: make game class
class player:
    #['player']
    steamid = 0
    name = "name"
    team = "T"
    activity = "playing"

    #['player']['state']
    health = 100
    armor = 0
    helmet = False
    flashed = 0
    smoked = 0
    burning = 0
    money = 0
    round_kills = 0
    round_killhs = 0
    equip_value = 0
    #['player']['match_stats']
    kills = 0
    assists = 0
    deaths = 0
    mvps = 0
    score = 0

def HEALTH(plr):
    print("HEALTH: [", end="")
    for i in range(20):
        if (i < plr.health / 5):
            print("#", end="")
        elif (plr.health == 0):
            print("X", end="")
        else:
            print("_", end="")
    if (plr.health > 0):
        print("] ("+ str(plr.health)+")")
    else: 
        print("] (DEAD)")

def ARMOR(plr):
    print("ARMOR:  [", end="")
    for i in range(20):
        if (i < plr.armor / 5):
            print("#", end="")
        else:
            print("_", end="")
    print("] ("+ str(plr.armor)+")")


plr = player()

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result(): #CALLED EVERY TIME DATA CHANGES
    data = request.json

    
    #['player']
    plr.steamid      = data['player']['steamid']
    plr.name         = data['player']['name']
    try:
        plr.team     = data['player']['team']
    except(KeyError):
        plr.team     = "none"
    plr.activity     = data['player']['activity']

    #['player']['state']
    plr.health       = data['player']['state']['health']
    plr.armor        = data['player']['state']['armor']
    plr.helmet       = data['player']['state']['helmet']
    plr.flashed      = data['player']['state']['flashed']
    plr.smoked       = data['player']['state']['smoked']
    plr.burning      = data['player']['state']['burning']
    plr.money        = data['player']['state']['money']
    plr.round_kills  = data['player']['state']['round_kills']
    plr.round_killhs = data['player']['state']['round_killhs']
    plr.equip_value  = data['player']['state']['equip_value']

    #['player']['match_stats']
    plr.kills        = data['player']['match_stats']['kills']
    plr.assists      = data['player']['match_stats']['assists']
    plr.deaths       = data['player']['match_stats']['deaths']
    plr.mvps         = data['player']['match_stats']['mvps']
    plr.score        = data['player']['match_stats']['score']
    

    #print(data['round']['phase'])
    #print(plr.deaths)
    #print(plr.name)
    print(data)
    return 'Received !' # response to your request.

app.run(debug=False, port='3000')

