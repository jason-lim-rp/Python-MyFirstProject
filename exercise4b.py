import os

where = "C:\\Program Files\\"
#where = "C:\\Program Files (x86)\\"

def searchByName(name):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            if file == name:
                print (os.path.join(root, file))
                totalSize =+ os.path.getsize(os.path.join(root, file))
    return totalSize


total = searchByName("readme.txt")
print ("Total is : %d" % (total))
print ("All done")

