from random import randint, random
from sys import argv
from os import path, system


##### change these

suffix = "-cut"
new_ext = ".mp4"
#suffix = randint(0,1000) # random suffix if that's useful? Low chance of overwriting anything, 
                          # even though ffmpeg double checks you want to overwrite a file

#####


# Try to get the file user dropped
try:
    inFile = argv[1] 
except IndexError:
    print("Drag a video file onto this script!!")
    input("press enter to continue...")

# Get times to cut
print("If something doesn't work, make sure the directory has no spaces, and ffmpeg.exe is here with the script.")
print("You can change the output vido's suffix and file extension at the top of the script.")
print("The output video will be placed in the directory of the input file.")
print('\n\nCutting video: "'+ inFile+'"')
print("Format times as 'ss', 'mm:ss', or 'hh:mm:ss'. It's flexible.")
start_time = input("Start time of cut: ")
end_time = input("End time of cut: ")

# File and path name stuff
scriptPath  = path.dirname(path.realpath(__file__))
fileName    = path.splitext(inFile)[0]
filePath    = path.dirname(inFile)
fileEXT     = path.splitext(inFile)[1]

output= path.join(filePath, fileName+suffix+new_ext)

# Make the command to run
cmd = f'@"{scriptPath}/ffmpeg.exe" -i "{inFile}" -ss {start_time} -to {end_time} "{output}"'
print("\n\n"+cmd+"\n\n")
# Try running the command
try:
    system(cmd)
except Exception as e:
    print(e)

input("\nDone (delete the last line of this script to disable this confirmation)")