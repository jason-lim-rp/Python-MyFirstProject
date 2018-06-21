import os

where = "C:\\Program Files\\"
#where = "C:\\Program Files (x86)\\"

def searchByName(name):
    for root, dirs, files in os.walk(where):
        for file in files:
            if file == name:
                print (os.path.join(root, file))

searchByName("readme.txt")

