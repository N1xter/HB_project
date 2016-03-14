#adding a comment to test git
from string import join

# creates a function to read a sample matagrano doc
# def Matagrano_Reader(filename):
# 	#open the file
# 	with open(filename) as matagrano:
# 		#create a raw list of the contents of the file
# 		matagrano_raw_list =  matagrano.readlines()
# 		y = 1
# 		for x in matagrano_raw_list:
# 			if x == '\n':
# 				#how do I make a list name increment?





# 			if x[-1] != "1" and if x[-1] != "2" and if x[-1] != "3" and if x[-1] != "4" and if x[-1] != "5" and if x[-1] != "6" and if x[-1] != "7" and if x[-1] != "8" and if x[-1] != "9" and if x[-1] != "0":
# 				BREWERY = x
# 			#how do I split the list every time there is a '/n'???
# 			else: #write the dictionary for item X.


				# how do I automate the new variables???
				# do I need variables if

				

# How do I split the list?
# how do I create an automated counter that allows multiple lists to be made?


# """ Use to test"""
Beer_List = []
def Matagrano_Reader(filename):
	#open the file
	with open(filename)as matagrano:
		matagrano_raw_list = matagrano.readlines()
	# print matagrano_raw_list
	# print Beer["Brewery"]
	for x in matagrano_raw_list:
		#this is a template dictionary to be added to the full list. 
		#will be the same for all 4  inputs.
		Beer = {"Brewery":None, "Name": None, "Style":None, "ABV":None, "Raw_Package_data":None, "PType(Keg or PKG)": None, "PSize":None, "Distributor":"Matagrano", "UnitCount":None, "Price":None,}
		#below is the input-specific parsing algorithm
		# this splits each line into its own list of items
		Mat_item = x.split()
		#print len(Mat_item)
		#this prevents errors from empty lines
		if len(Mat_item) <1:
		 	pass
		#all beers end in a price, but all breweries end in a letter, so...
		elif Mat_item[-1].isdigit() == False:
			BREW = join(Mat_item," ")
			#print Beer["Brewery"]
		else:
			Beer["Brewery"] = BREW
			Beer["Price"] = float(Mat_item.pop())
			#print Beer["Price"]
			
			Beer["Raw_Package_data"] = Mat_item.pop()
			#print Mat_item
			#print Beer["Raw_Package_data"]
					# Beer["Name"] = Mat_item[0]
			Beer["Name"] = join(Mat_item," ")
			#print Beer["Name"]
			#This 
			Beer_List.append(Beer)
Matagrano_Reader("Matagrano_sample.txt")
print Beer_List


# 	"""this prompts for user inputs when the value is None"""
# 	Bkeys = Beer.keys()
# 	for key in Bkeys:
# 		if Beer[key] == None:
# 			Prompt_text = "For the Beer:", Beer["Brewery"], Beer["Name"], Beer["Raw_Package_data"], "Please enter the", key, ": "
# 			Beer[key] = raw_input(Prompt_text)
# 	print Beer
