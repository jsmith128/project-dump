import pyqrcode
import sys
print('type "exit" to stop')
print('How many QRs to be generated? (nothing=100): ', end='')
loops = 0
times = input()
if times=='': times = 100
while loops<int(str(times)):
    print('Type word to QR-ify: ', end='')
    inp = input()
    if inp=='exit': sys.exit()
    print('name: ', end='')
    name = input()

    im = pyqrcode.create(inp)
    im.png("/home/jon/Desktop/python/"+name+".png", scale=6)
    loops+=1