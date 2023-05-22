import random
import string
import time
from io import open

import requests
import json


def listToStr(s): 
    str1 = "" 
    
    for elem in s: 
        str1 += elem
    
    return str1 

def genCode():
    codelen = 16
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

    codelist = random.sample( chars, codelen )
    #code = "https://discord.gift/" + listToStr(codelist)
    code = listToStr(codelist)
    return code

def testCode(code):
    reqURL = "https://discord.com/api/v8/entitlements/gift-codes/" + code
    r = requests.get(reqURL)

    rDict = json.loads( r.text ) 
    return rDict['message']

def codeFinder( iterations ):
    waitime = 13 # 5 times per minute to avoid ratelimiting
    urlprefix = "https://discord.gift/"

    for i in range(iterations):
        print("\n--code #" + str(i+1) + ":")
        code = genCode()
        test = testCode(code)

        if test == "Unknown Gift Code":
            print(urlprefix + code)
            print("'" + test + "'")
        elif test == "You are being rate limited.": # Increase wait time between loops if ratelimited to further avoid ratelimiting
            waitime += 1
            print("Ratelimited at " + str( 60/(waitime-1) ) + " times per minute")
            print("Increased waittime by 1, now " + str( waitime ))
            print("Waiting 60 seconds...")
            time.sleep(60)
        else:
            print("\n\n::SUCCESS::")
            print(urlprefix + code)
            print("::SUCCESS::\n")
            print("'" + test + "'\n\n")
            with open('ncodes.txt', 'a') as f:
                f.write(urlprefix + code + '\n')
                f.write(test + '\n\n')

        time.sleep(waitime)

codeFinder(3000)