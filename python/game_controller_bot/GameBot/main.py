import discord
import os
from time import sleep


import keyboard
import mouse





#CONFIG#
debug = 1

#%BOT%#
basedir = os.getcwd() #should be GameBot folder
os.chdir(basedir) #set to gamebot folder
client = discord.Client()

game = discord.Game('type a letter to do stuff')


#________;PROGRAM;________#

def sendkey(key):
    keyboard.press( key )
    sleep(1)
    keyboard.release( key )

    print("keypress:", key )

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    await client.change_presence(status=discord.Status.idle, activity=game) #change status to be hip!
    print('INFO: changed game to:', game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content) == 1: #does the message only have one letter?
        
        sendkey( str(message.content[0]) )
        
    if message.content == 'backspace':
        sendkey('backspace')
    if message.content == 'space':
        sendkey('space')

    if message.content == 'm1':
        mouse.click(button='left')
        print('mouse: left clicked')
    if message.content == 'm2':
        mouse.click(button='right')   
        print('mouse: right clicked')

    if message.content.lower().startswith('mu'):
        mouse.move(0, -int( message.content.lower().split()[1] ), absolute=False)
        print('mouse: move up')
    if message.content.lower().startswith('md'):
        mouse.move(0, int( message.content.lower().split()[1] ), absolute=False)  
        print('mouse: move down')
    if message.content.lower().startswith('ml'):
        mouse.move(-int( message.content.lower().split()[1] ), 0, absolute=False)
        print('mouse: move left')
    if message.content.lower().startswith('mr'):
        mouse.move(int( message.content.lower().split()[1] ), 0, absolute=False)  
        print('mouse: move right')

client.run(BOT KEY HERE)