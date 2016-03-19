from BBFunctions import *

print "Welcome, Beer Buyer"

Mat_Choose_File()

Hen_Choose_File()

DBI_Choose_File()

Art_Choose_File()


# Henhouse_Reader("Henhouse_Sample.csv")
# DBI_Reader("DBI_Sample_list.csv")

print "What portion of the list would you like to see?" 
print "for all: press 1,"
print "for keg only, press 2"
print "for bottle/can only, press 3"
filter_resp = raw_input("enter your selection: ")
if filter_resp != "1" or filter_resp != "2" or filter_resp != "3":
	filter_resp = raw_input("ERROR, please enter a valid selection: ")
elif filter_resp == "1":
	#for BEER in Beer_List:
		#do stuff
	pass
elif filter_resp == "2":
	#for BEER in Beer_List:
		#do stuff
	pass
elif filter_resp == "3":
	#for BEER in Beer_List:
		#do stuff
	pass

Filtered_Beer_List = []

print "How would you like to sort the list?"
print "by Distributor, press 1"
print "by Brewery, press 2"
print "by ABV, press 3"
print "by Package Size, press 4"
print "by Style, press 5"
print "by Price, press 6"
print "by Package Type (keg or bottle/can), press 7"
sort_resp = raw_input("enter your selection: ")
if filter_resp != "1" or filter_resp != "2" or filter_resp != "3"or filter_resp != "4" or filter_resp != "5"or filter_resp != "6" or filter_resp != "7":
	filter_resp = raw_input("ERROR, please enter a valid selection: ")
elif filter_resp == "1":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass
elif filter_resp == "2":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass
elif filter_resp == "3":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass
elif filter_resp == "4":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass
elif filter_resp == "5":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass
elif filter_resp == "6":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass
elif filter_resp == "7":
	#for BEER in Filtered_Beer_List:
		#do stuff
	pass



# have modified beer list written to a csv
#user opens csv, then chooses the beers they want to order by row number
#the row number -1 will correspond to the index number
#the program then writes the selected beer info to a new list, 1 per distributor
#those distributor lists are then formatted into text in a .txt file
print Beer_List