# from http.server import BaseHTTPRequestHandler, HTTPServer
# import json

# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/html')
#         self.end_headers()

#         message = "Hello, World! Here is a GET response"
#         self.wfile.write(bytes(message, "utf8"))

#     def do_POST(self):
#         self.send_response(200)
#         file_length = int(self.headers['Content-Length'])
#         data = self.rfile.read(file_length)

#         data = json.dumps(data)

#         print(data)

# with HTTPServer(('', 3000), handler) as server:
#     server.serve_forever()

from flask import Flask, request
from tqdm import tqdm
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

    #def __init__(self, name, age):
#TODO: maybe put these in player class
def IDENT(plr):
    print("steamid: "+ plr.steamid)
    print("Name: "+ plr.name)
    print("Team: "+ plr.team)
    print("Activity: "+ plr.activity)

def STATUS(plr):  
    print("Money: "+ str(plr.money))
    print("")
    print("Flashed: "+ str(plr.flashed))
    print("Smoked: "+ str(plr.smoked))
    print("Burning: "+ str(plr.burning))

def STATS(plr):
    print("Kills: "+ str(plr.kills), "("+str(plr.round_kills)+")")
    print("Assists: "+ str(plr.assists))
    print("Deaths: "+ str(plr.deaths))
    print("MVPs: "+ str(plr.mvps))
    print("Score: "+ str(plr.score))

def HELMET(plr):
    print("Helmet: "+ str(plr.helmet))

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



def update(plr):
    print('\n\n\n\n\n\n\n')
    IDENT(plr)
    print('')
    
    STATUS(plr)
    print('')

    STATS(plr)
    print('\n')

    HELMET(plr)
    ARMOR(plr)
    HEALTH(plr)

plr = player()

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
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



    # print(plr.health)
    # print(plr.activity)
    #print(vars(plr))
    update(plr)
    return 'Received !' # response to your request.

app.run(debug=False, port='3000')

