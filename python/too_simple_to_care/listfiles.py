import os
import unidecode

with open("output.txt", "w") as a:
    for path, subdirs, files in os.walk(r"F:\blender"):
       for filename in files:
         f = os.path.join(path, filename, getctime, getmtime)
         s = unidecode.unidecode(f)
         a.write(str(s) + os.linesep) 
         # + os.path.getmtime(path) + os.path.getctime(path)
         
        #accented_string = u'Málaga'
        # accented_string is of type 'unicode'
        
        #unaccented_string = unidecode.unidecode(accented_string)
        # unaccented_string contains 'Malaga' and is of type 'str'