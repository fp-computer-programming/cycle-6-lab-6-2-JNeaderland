#Author: Jacob Neaderland
my_row = ["Naz", "Ryan"]
#I have to replace 1 and 2 because replacing just 2 gave an index error
my_row[1:2] = "Ryan", "Jacob"
my_row2 = my_row[:]
print (my_row2)
del my_row[1]
print (my_row)