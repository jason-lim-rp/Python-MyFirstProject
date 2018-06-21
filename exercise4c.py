import os

where = "C:\\Program Files\\"
#where = "C:\\Program Files (x86)\\"


def searchByName(name):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            if file == name:
                fullname = os.path.join(root, file)
                filesize = os.path.getsize(fullname)
                print ("%6d %s" % (filesize, fullname))
                totalSize += filesize
    return totalSize


total = searchByName("readme.txt")
print ("Total is : %d" % (total))
print ("All done")

