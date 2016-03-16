from string import join
import csv

Beer_List = []

#This function uses various parsing techniques to create a list of dictionaries. Each dictionary is one beer.
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
			# print Beer["Raw_Package_data"]
			if Beer["Raw_Package_data"] == '5-':
				Beer["UnitCount"] = 1
				Beer["PSize"] = "5"
				Beer["PType(Keg or PKG)"] = "KEG"
			elif Beer["Raw_Package_data"] == '13.2-':
				Beer["UnitCount"] = 1
				Beer["PSize"] = "13.2"
				Beer["PType(Keg or PKG)"] = "KEG"
			elif Beer["Raw_Package_data"] == '15.5-':
				Beer["UnitCount"] = 1
				Beer["PSize"] = "15.5"
				Beer["PType(Keg or PKG)"] = "KEG"
			elif Beer["Raw_Package_data"] == '4/6-':
				Beer["PSize"] = "12"
				Beer["UnitCount"] = 24
				Beer["PType(Keg or PKG)"] = "PKG"
			elif Beer["Raw_Package_data"] == '12/22oz-':
				Beer["UnitCount"] = 12
				Beer["PSize"] = "22"
				Beer["PType(Keg or PKG)"] = "PKG"
			Beer["Name"] = join(Mat_item," ")
			print Beer["Name"]
			""" this prompts for user inputs when the value is None"""
			Bkeys = Beer.keys()
			for key in Bkeys:
				if Beer[key] == None:
					Prompt_text = "For the Beer:", Beer["Brewery"], Beer["Name"], Beer["Raw_Package_data"], "Please enter the", key, ": "
					Beer[key] = raw_input(Prompt_text)
			Beer_List.append(Beer)


# This function parses using Regular Expressions
def Artisan_Reader(filename):
	with open(filename)as artisan:
		artisan_raw_list = artisan.readlines()
	for x in artisan_raw_list:
		#this splits the raw list into a new list for every line
		art_item = x.split('\n')
		#the following removes a consistent extra space that occurs at the end of every line
		art_item.pop()
		#this skips (presently) unuseful lines
		if x ==' ' or x == '' or x == 'U.S.' or x == 'Belgium':
			pass
		else:
			#how can I make it use different regular expressions above and below draft?
			pass


#This Function parses information from a CSV file
def Henhouse_Reader(filename): #sTILL NEED TO REMOVE BLANKS FROM BEER LIST
	with open(filename) as henhouse:
		henhouse_csv = csv.reader(henhouse)
		for row in henhouse_csv:
			Beer = {"Brewery":None, "Name": None, "Style":None, "ABV":None, "Raw_Package_data":None, "PType(Keg or PKG)": None, "PSize":None, "Distributor":None, "UnitCount":None, "Price":None,}
			if row[1] == '':
				BREW = row[0]
			else:
				Beer["Name"] = row[0]
				Beer["ABV"] = row[1]
				Beer["Style"] = row[2]
				Beer["Extra_Info"] = row[3]
				Beer["PSize"] = row[4]
				Beer["Price"] = row[5]
				Beer["Brewery"] = BREW
				Beer["Distributor"] = "Henhouse"
				Beer["PType(Keg or PKG)"] = "KEG"
				Beer["Raw_Package_data"] = Beer["PSize"]
				Beer["UnitCount"] = 1
				Bkeys = Beer.keys()
				for key in Bkeys:
					if Beer[key] == None:
						Prompt_text = "For the Beer:", Beer["Brewery"], Beer["Name"], Beer["Raw_Package_data"], "Please enter the", key, ": "
						Beer[key] = raw_input(Prompt_text)
				Beer_List.append(Beer)
	
#THis function adds dictionaries to the beer list from a CSV, and changes certain values for uniformity
def DBI_Reader(filename):
	with open(filename) as DBI:
		DBI_CSV = csv.reader(DBI)
		for row in DBI_CSV:
			Beer = {"Brewery":None, "Name": None, "Style":None, "ABV":None, "Raw_Package_data":None, "PType(Keg or PKG)": None, "PSize":None, "Distributor":None, "UnitCount":None, "Price":None,}
			if row[3] == '':
				UNIT = row[4]
			else:
				UNIT = int(row[3])*int(row[4])

			if row[1] == 'ANC':
				Beer["Brewery"] = "Anchor"
			elif row[1] == 'BP':
				Beer["Brewery"] = "Ballast Point"
			else: #this will prompt the user with the distributor's brewery code and the beer name for the actual brewery name for unrecognized items
				Prompt_text = "For the Beer:", row[1], row[2], "Please enter the Brewery Name: "
				Beer["Brewery"] = raw_input(Prompt_text)
			if row[6] == "CAN" or row[6] == 'BTL':
				Beer["PType(Keg or PKG)"] = "PKG"
			else:
				Beer["PType(Keg or PKG)"] = row[6]
			#below correlate directly to a column in the csv
			Beer["Name"] = row[2]
			Beer["Style"] = row[2]
			Beer["Extra_Info"] = row[0]
			Beer["PSize"] = row[5]
			Beer["Price"] = row[7]
			Beer["Distributor"] = "DBI"
			Beer["Raw_Package_data"] = " "
			Beer["UnitCount"] = UNIT
			#below asks for user input for fields still marked "None"
			Bkeys = Beer.keys()
			for key in Bkeys:
				if Beer[key] == None:
					Prompt_text = "For the Beer:", Beer["Brewery"], Beer["Name"], Beer["Raw_Package_data"], "Please enter the", key, ": "
					Beer[key] = raw_input(Prompt_text)
			#adds the dictionary to the list before moving to the next line
			Beer_List.append(Beer)



"""
TESTING 
These call the function(s) and prints the results 
(DO NOT run in Sublimne as user input is required!)
"""

# Matagrano_Reader("Matagrano_sample.txt")
# Artisan_Reader("Artisan_Sample_List.txt")
# Henhouse_Reader("Henhouse_Sample.csv")
# DBI_Reader("DBI_Sample_list.csv")
# print Beer_List