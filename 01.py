def print_Title(name):
    print ("%10s %20s %10s" % ("$$$$","ABC Super mart","$$$$"))
    print ("9 Woodlands Ave 9".center(40, " "))
    print (name.center(40," "), "\n\n")

a = 1000.50
b = -12.50
word = "Pineapple"
word2 = "Luna colour pencil"
print_Title("Mary")
print ("%-20s $%10s $%10s" % ("Item","Price", "With GST") )
print ("===============================================")
print ("%-20s $%10.2f %+10.2f" % (word, a, a * 1.07))
print ("%-20s $%10.2f %+10.2f" % (word2, b, b * 1.07))
