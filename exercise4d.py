import os

where = "C:\\Program Files\\"
#where = "C:\\Program Files (x86)\\"


def searchBySize(size):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            filesize = os.path.getsize(fullname)
            if filesize > size:
                print ("%6d %s" % (filesize, fullname))
                totalSize =+ filesize
    return totalSize


total = searchBySize(100000000)
print ("Total is : %d" % (total))
print ("All done")

