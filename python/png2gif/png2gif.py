from sys import exit, argv
import os
import imageio.v3 as imageio

try:
    droppedFile = argv[1] 
except IndexError:
    print("NO FILE DROPPED")
    input()
    exit()

if not os.path.isdir(droppedFile):
    print("DRAG A FOLDER INSTEAD")
    input()
    exit()


path = os.path.dirname(droppedFile)
gifname = os.path.join( droppedFile, input("new gif name? (hint: dont include .gif) ") + ".gif" )
imagefiles = os.listdir(droppedFile)
fps = int(input("fps? "))


frames = []
for filename in imagefiles:
    filename = os.path.join(droppedFile, filename)
    fileEXT = os.path.splitext(filename)[1]

    if (fileEXT == ".gif"):
        print("HEY! Get that gif out of there. It doesnt matter but it's annoying i had to put this exception in")
        continue

    frames.append(imageio.imread(filename))
    print("Append", filename)

try:
    imageio.imwrite( gifname, frames, plugin="pillow", duration=1000 * 1/fps, mode="RGBA", loop=0, transparency=0, disposal=2 )
except (ValueError): # ERROR WHEN GIF ISNT RGBA::::
    imageio.imwrite( gifname, frames, plugin="pillow", duration=1000 * 1/fps, mode="RGB", loop=0, transparency=0, disposal=2 )

print(f"Done writing {gifname}!")
input()
