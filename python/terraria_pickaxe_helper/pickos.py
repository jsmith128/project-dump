### SETUP DATA:
import pickCon as pc
from pData import picks, pickNames
from sys import platform
run = True

### /SETUP DATA

### PROGRAM:

print(
'\n\n'
r'$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\                    ' + '\n'
r'$$  __$$\\_$$  _|$$  __$$\ $$ | $$  |                   ' + '\n'
r'$$ |  $$ | $$ |  $$ /  \__|$$ |$$  / $$$$$$\   $$$$$$$\ ' + '\n'
r'$$$$$$$  | $$ |  $$ |      $$$$$  / $$  __$$\ $$  _____|' + '\n'
r'$$  ____/  $$ |  $$ |      $$  $$<  $$ /  $$ |\$$$$$$\  ' + '\n'
r'$$ |       $$ |  $$ |  $$\ $$ |\$$\ $$ |  $$ | \____$$\ ' + '\n'
r'$$ |     $$$$$$\ \$$$$$$  |$$ | \$$\\$$$$$$  |$$$$$$$  |' + '\n'
r'\__|     \______| \______/ \__|  \__|\______/ \_______/ ' + '\n'
+'''_______________________________________________________________
Perfectly Interfaced piCkaxe Kompanion ~Operational~... Silly

pickos.py 0.0.4 (March 19 2020, 2:23 PM) 
[license] on {}
©2020 Steeveeskeleton

Type "help", "copyright", "credit", "license" or "info" for more information.'''.format(platform)
)
while run == True:
    inp = input('>>> ').split(' ') # get input as a list, split by spaces
    pc.chkCmd(inp)
### /PROGRAM