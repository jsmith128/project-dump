import csv
import os

# TAKES THE STRUCTURE EXPORT OUTPUT FROM CUBIOMES VIEWER ANALYSIS
# AND TURNS IT INTO A WAYPOINT FILE FOR XAEROS MINI/WORLDMAP

infile = "example_in.txt"
outfile = "example_out.txt"

#default state, true/false (this is the option for disabling waypoints in-game)
disabled = "true"

# https://minecraft.fandom.com/wiki/Formatting_codes
colors = {
    'default' : 0,
    'village' : 14,
    'monument' : 7,
    'ocean_ruin' : 9,
    'shipwreck' : 6,
    'treasure' : 6,
    'mineshaft' : 15,
    'outpost' : 7,
    'ruined_portal' : 4,
    
    'ancient_city' : 7,

    'fortress' : 12,
    'bastion' : 4,
    'ruined_portal (nether)' : 4,
    
    'end_city' : 8,
    'end_gateway' : 8,
}

disabled_structs = {
    'village' : False,
    'monument' : False,
    'ocean_ruin' : False,
    'shipwreck' : False,
    'treasure' : False,
    'mineshaft' : True, # LOTS of these
    'outpost' : False,
    'ruined_portal' : False,
    
    # 99% probably wont work
    'ancient_city' : True,

    'fortress' : True,
    'bastion' : True,
    'ruined_portal (nether)' : True,
    
    'end_city' : True,
    'end_gateway' : True,
}




skipcounter = 6
linecounter = 0
with open(infile) as f:
    with open(outfile, "w") as o:
        for line in csv.reader(f, delimiter=";"):
            if skipcounter < 0:
                linecounter +=1
                #seed;structure;x;z;details
                struct_type = line[1]
                initial = struct_type[0]
                struct_x = line[2]
                struct_y = "~"
                struct_z = line[3]
                
                if (struct_type in disabled_structs.keys()): # this check might not be required
                    if (disabled_structs[struct_type] == True):
                        continue

                if (struct_type in colors.keys()):
                    color = colors[struct_type]
                else:
                    color = colors['default']

                print(struct_type, struct_x, struct_z, color)
                # waypoint:name:initials:x:y:z:color:disabled:type:set:rotate_on_tp:tp_yaw:visibility_type
                o.write("waypoint:{wpname}:{initial}:{x}:{y}:{z}:{color}:{disabled}:0:gui.xaero_default:false:0:0\n".format(
                    wpname = struct_type + str(linecounter),
                    initial = initial,
                    x = struct_x,
                    y = struct_y,
                    z = struct_z,
                    color = color,
                    disabled = disabled
                ))
            else:        
                skipcounter -= 1
            