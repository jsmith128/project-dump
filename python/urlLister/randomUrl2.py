from urllib import parse
import urllib.request
from time import time
from os import chdir, path
from sys import argv

chdir(path.dirname(argv[0]))

with open('domains.txt', 'r') as f:
    TLD = f.read().split('\n')
http = ('http://www.')#, 'https://www.')


normal_chars = 'abcdefghijklmnopqrstuvwxyz1234567890- '
chars = []
for i in normal_chars:
    chars.append(ord(i))
print(chars)


user_url = input('url: ')
user_url_name = ''.join(user_url.split('.')[0])
user_url_domN = ''.join(user_url.split('.')[:0])
user_url_domN = ''.join(['.',str(user_url_domN)])


url_ord = []
for i in user_url_domN: 
    url_ord.append(ord(i))

for i in url_ord:
    print(chr(i))