from console import fg, bg
from pData import picks, pickNames
#.replace(',', '\n').replace('{','').replace('}','')

m = 0 # m is for iteration number
print('Name===================: Power\n')
for i in pickNames:
    print( bg.darkGreen(i), end='') #print pickaxe name[i] but do not create a new line
    for _ in range(23 - len(i)): #23 = len of longest name + 1
        # \/ print '-'s or '='s to make all next values at the same collumn. 
        # switches every other line
        if (m % 2) == 0:
            print(fg.lightBlue('-'), end='')
        else:
            print(fg.green('='), end='')
    
    print(': ', end='') 
    print(picks[m].power, end='')
    print('\n') #double new line, second is from the default value of " end='\n' "
    m += 1 # see above