import bpy
from os import path

# DOESNT WORK SORRY    !!!
NORMALMODE = False
NORMAL2LINEMODE = False # make a newline for the normal vectors inside each smooth_triangle?

obj = bpy.context.object

filepath = path.dirname(bpy.context.space_data.text.filepath)
outputFile = path.join(filepath, obj.data.name + "_pov.txt")

print("Printing to: " + outputFile)

# make dictionary where key is index and value is vertex
index2vert = {}
for vert in obj.data.vertices:
    index2vert[vert.index] = vert


#wrldspace = bpy.context.object.matrix_world
#print("\n\n")
outLines = []
for tri in obj.data.loop_triangles: 
    if (NORMALMODE):
        outLines.append("smooth_triangle { ")
    else:
        outLines.append("triangle { ")   
    
    # list of this triangle's vertex coordinates in format <x, y, z>
    tri_verts_coords = []
    # list of this triangle's vertex normal coordinates in format <x, y, z>
    tri_norms_coords = []
    for index in tri.vertices:
        # get this vertex's coordinates and normal vectors
        vert_co = index2vert[index].co
        vert_norm = index2vert[index].normal
        
        # format this vertex's coordinates to a list of floats with .0000 accuracy
        coords = [str("{:.4f}".format(coord)) for coord in vert_co]
        # format the list of floats to <x, y, z> a format string. add to list
        tri_verts_coords.append("<" + ", ".join( coords ) + ">")
        
        # same as last 2 lines except for normal coordinates
        if (NORMALMODE):
            normalcoords = [str("{:.4f}".format(coord)) for coord in vert_norm]
            tri_norms_coords.append("<" + ", ".join( coords ) + ">")
    
    
    outLines.append( ", ".join(tri_verts_coords) )
    if (NORMALMODE):
        if (NORMAL2LINEMODE):
            # add a comma, new line, 2 tabulations, and 2 spaces to line up with prev line
            outLines.append( ",\n\t\t  "+", ".join(tri_norms_coords) )
        else:
            # dont add anything but a comma and space
            outLines.append( ", "+ ", ".join(tri_norms_coords) )
    outLines.append(" }\n")   
        




f = open( outputFile, 'w' )
f.writelines( outLines )
f.close()