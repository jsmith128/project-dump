from sys import argv
from os import path, system


dir_path = path.dirname(path.realpath(__file__))
newExt = ".mp4" #default value

# get file's name, extension, and path from sys.argv (aka dropped file or first argument)
def getFile(argv):
    try:
        droppedFile = argv[1] 
    except IndexError:
        print("No file dropped")
        input("")

    fileName    = path.splitext(argv)[0]
    fileExt     = path.splitext(argv)[1]
    filePath    = path.dirname(argv)

    return fileName, fileExt, filePath 


def convert(argv, newExt):
    fileName, fileExt, filePath = getFile(argv)

    print(fileName, filePath, fileExt)

    # build the ffmpeg command
    cmd = dir_path + './ffmpeg.exe -i "{inp}" "{output}"'.format(
        inp= argv, 
        output= path.join(filePath, fileName+newExt)
    )
    
    # print cmd for debugging
    print("\n\n\n"+cmd+"\n\n\n")
    # run cmd
    system(cmd)