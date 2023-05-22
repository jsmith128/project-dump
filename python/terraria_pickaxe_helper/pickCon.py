from pData import pickNames, picks, l2s
def err(e):
    if e == '1':
        print('Unknown command')


helptxt = '''\
note: do NOT type the "="s or " '' "s or even the ":"s and ";"s, EVER...
...Unless specified otherwise...

Commands:
  =help  : You know.
      help names                    : List all supported names of items.
      help names pickaxe            : List all supported pickaxe names
  =copyright, credit, license, info : Self-explanitory.

  =list; ls  : List all pickaxes and their stats.
      list [ores]       : list all pickaxes that can be crafted with listed ores.
      list [ores] -ex   : same as above, but shows ONLY pickaxes that can be
                          crafted with listed ores. Rather than including types such 
                          as cactus.
                NOTE! Make sure to create a list using regular python syntax
                ex: list ['crimtane', 'lead', 'platinum'] 
                  (tip: you can even use non-variable ingredients and ores like chlorophyte and souls!
                  To use souls, write ['sFL','sLI','sNI','sMI','sSI','sFR'], in order of:
                  Flight, Light, Night, Might, Sight and Fright.)
                  Type "help names" to see a list of all acceptable names for the [ores] option.

  =craft; cr  : Show how to craft all pickaxes.
      craft "pickaxe name"  : Show how to craft specified pickaxe.
                                Type "help names pickaxe" to show all supported pickaxe names.'''
                                
def chkCmd(cmd):
    if cmd[0] == 'list' or cmd[0] == 'ls':
        if cmd[1] == 'pickaxes':
            for pickN in pickNames:
                print(pickN)

    elif cmd[0] == 'help':
        if len(cmd) >= 2:
            if cmd[1] == 'names':
                if len(cmd) >= 3:
                    if cmd[2] == 'pickaxes':
                        for pickN in pickNames:
                            print(pickN)
                    else: err('1')
                else: print('Item names')
            else: err('1')
        else: print(helptxt)
    else: err('1')

### /PROGRAM
