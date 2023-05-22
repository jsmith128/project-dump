from sys import argv

try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")

fileName    = os.path.basename(droppedFile)
filePath    = os.path.dirname(droppedFile)


cmd = 'ffmpeg -i "{inp}" -vf scale=iw/2:ih/2 "{output}"'.format(
    inp= droppedFile, 
    output= os.path.join(filePath, fileName+"-half.mp4"))

print("\n\n"+cmd+"\n\n")
os.system(cmd)

