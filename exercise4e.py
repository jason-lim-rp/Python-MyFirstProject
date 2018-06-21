import os

where = "C:\\Program Files\\"
#where = "C:\\Program Files (x86)\\"


def searchByExtension(ext):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            filesize = os.path.getsize(fullname)
            if file.endswith(ext):
                print ("%6d %s" % (filesize, fullname))
                totalSize += filesize
    return totalSize


total = searchByExtension("jpg")
print ("Total is : %d" % (total))
print ("All done")

