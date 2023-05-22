from itertools import product
from urllib import parse
import urllib.request
from time import time
chars = 'abcdefghijklmnopqrstuvwxyz1234567890- '
domNamesCommon = ('.com','.net','.org','.edu','.gov','.info','.biz','.name','.pro','.aero','.asia',
            '.cat','.coop','.int','.jobs','.mil','.mobi','.museum','.tel','.travel','.zone'            
            )
domNamesMoreCommon = ('.com','.net','.org','.gov','.info','.mil','.edu','.io')
countryNames = ('.us','.jp','.uk','.co.uk','.br','.ru','.eu','.fr','.de','.au')

with open('domains.txt', 'r') as f:
    TLD = f.read().split('\n')

http = ('http://www.')#, 'https://www.')


def cart(s):
    yield from product(*( [s] * 10 ), domNamesCommon)

for x in cart(chars):
    t = str(int(time()))[6:]
    x='http://www.'+''.join(x).replace(' ','')
    try:
        print(urllib.request.urlopen(x).getcode() )
        print('Found a website at: '+x)
    except Exception:
        print(t+':  no {}'.format(x))
    else:
        with open('urls.txt', 'a+') as f:
            f.write(x+'\n')