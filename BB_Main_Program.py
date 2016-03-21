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

"""SORTING (Later:add option'I would like to sort' or 'I would like to look for an exact match'"""
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
"""SELECTION"""
"""(A.) write to CSV"""
#this presents the order to write the fields to csv
field_names = ["Brewery", "Name",  "PType(Keg or PKG)", "PSize", "UnitCount", "Price", "Distributor", "Style", "ABV", "Raw_Package_data", "Extra_Info"]
#can I add a time stamp to the beer list?
with open('Beer_List.csv', 'w') as BL:
    fp = csv.DictWriter(BL, field_names)
    fp.writeheader()
    fp.writerows(Sorted_Beer_List)

"""(B.) SELECTION - User Input"""
#tell ser what to do
print 'Please open "Beer_List.csv" in this directory.'
print'Then, find the row number(s) of beers you would like to order.'

#user opens csv, then chooses the beers they want to order by row number
#the row number -1 will correspond to the index number
print "Type the first row number for the beer you would like to purchase, then press enter"
# set up empty strings and lists to keep the variable global
selection = ''
selection_list = []
#start with Q equaling anything BUT 'n' or 'N' in order for conditional in while loop to be true
Q = "Y"
# call the function that appends the selection list based on UI
# works until the user types 'n' to stop the loop
while Q != "N" and Q !="n":
	selection_list = selection_helper(selection_list)
	Q = raw_input("Would you like to choose another? Y or N: ")
	if Q == "Y" or Q == "y":
		pass

#takes the user input and makes the numbers correlate to the actual index number
index = 0
while index < len(selection_list):
	#this makes the number correlate directly to the index # for the beer in Sorted_Beer_List
	selection_list[index] -= 2
	index += 1

#next line for debug
#print selection_list

#the program then writes the selected beer info to a new list, 1 per distributor
#empty order list
Order_List = []
#empty distributor-specific lists
Art_Buylist = []
Mat_Buylist = []
DBI_Buylist = []
Hen_Buylist = []

for x in selection_list:
	Order_List.append(Sorted_Beer_List[x])

for x in Order_List:
	if x["Distributor"] == "Matagrano":
		Mat_Buylist.append(x)
	elif x["Distributor"] == "Artisan":
		Art_Buylist.append(x)
	elif  x["Distributor"] == "DBI":
		DBI_Buylist.append(x)
	elif  x["Distributor"] == "Henhouse":
		Hen_Buylist.append(x)

print "To order fromn Matagrano: "
print Mat_Buylist
print "To order fromn Artisan: "
print Art_Buylist
print "To order fromn DBI: "
print DBI_Buylist
print "To order fromn Henhouse: "
print Hen_Buylist



#those distributor lists are then formatted into text in a .txt file
# print Beer_List