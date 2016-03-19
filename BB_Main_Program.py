"""IMPORT SUPPORTING FILES"""
from BBFunctions import *

"""WELCOME"""

print "Welcome, Beer Buyer"

"""CHOOSE FILES"""
#call all 4 choose and read functions
Mat_Choose_File()
Hen_Choose_File()
DBI_Choose_File()
Art_Choose_File()


"""FILTERING"""
#tell the user what to do
print "What portion of the list would you like to see?" 
print "for all: press 1,"
print "for keg only, press 2"
print "for bottle/can only, press 3"
#call the function and save the return value
Filtered_Beer_List = Beer_List_Filter(Beer_List)
# print Filtered_Beer_List

"""SORTING"""
#tell the user what to do
print "How would you like to sort the list?"
print "by Distributor, press 1"
print "by Brewery, press 2"
print "by ABV, press 3"
print "by Package Size, press 4"
print "by Style, press 5"
print "by Price, press 6"
print "by Beer Name, press 7"
print "by Package Type (keg or bottle/can), press 8"
#call the function and save the return value
Sorted_Beer_List = Beer_List_Sort(Filtered_Beer_List)


# have modified beer list written to a csv
#user opens csv, then chooses the beers they want to order by row number
#the row number -1 will correspond to the index number
#the program then writes the selected beer info to a new list, 1 per distributor
#those distributor lists are then formatted into text in a .txt file
# print Beer_List