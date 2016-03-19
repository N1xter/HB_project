from string import join
import csv
import re

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
	#regex for bottled products
	Art_RE_ml = re.compile('([a-zA-Z0-9 ]+), ([a-zA-Z0-9 ]+), ([a-zA-Z/ ]+)(\d+\.\d+)% (\d+)x(\d+)ml \$(\d+)')
	Art_RE_oz = re.compile('([a-zA-Z0-9 ]+), ([a-zA-Z0-9 ]+), ([a-zA-Z/ ]+)(\d+\.\d+)% (\d+)x(\d+)oz \$(\d+)')
	Art_RE_cl = re.compile('([a-zA-Z0-9 ]+), ([a-zA-Z0-9 ]+), ([a-zA-Z/ ]+)(\d+\.\d+)% (\d+)x(\d+\.\d+)cl \$(\d+)')
	Art_RE_dash = re.compile('([a-zA-Z0-9 ]+), ([a-zA-Z0-9 ]+), ([a-zA-Z/\- ]+)(\d+\.\d+)% (\d+)x(\d+)oz \$(\d+)')
	#regex for draft products
	Art_RE_K_l = re.compile('([a-zA-Z0-9 ]+), ([a-zA-Z0-9 ]+), ([a-zA-Z/\- ]+)(\d+\.\d+)% (\d+)L ([a-zA-Z]+) \$(\d+)')
	Art_RE_K_bbl = re.compile('([a-zA-Z0-9 ]+), ([a-zA-Z0-9 ]+), ([a-zA-Z/\- ]+)(\d+\.\d+)% (\d\/\d) bbl ([a-zA-Z]+) \$(\d+)')
	with open(filename)as artisan:
		artisan_raw_list = artisan.readlines()
		# I should probably write a function that automates the creation of these for loops based on a list of regex (or maybe a dictionary?)
		for text in artisan_raw_list:
			Beer = {"Brewery":None, "Name": None, "Style":None, "ABV":None, "Raw_Package_data":None, "PType(Keg or PKG)": None, "PSize":None, "Distributor":"Artisan", "UnitCount":None, "Price":None,}
			#These are bottle products
			if Art_RE_ml.search(text) != None:
				Art_line= Art_RE_ml.search(text)
				Beer["Brewery"] = Art_line.group(1)
				Beer["Name"] = Art_line.group(2)
				Beer["Style"] = Art_line.group(3)
				Beer["ABV"] = Art_line.group(4)
				Beer["UnitCount"] = Art_line.group(5)
				Beer["PSize"] = Art_line.group(6)
				Beer["Price"] = Art_line.group(7)
				Beer["PType(Keg or PKG)"] = "PKG"
				Beer["Raw_Package_data"] = Art_line.group(5), "x", Art_line.group(6)
				Beer_List.append(Beer)
			elif Art_RE_oz.search(text) != None:
				Art_line = Art_RE_oz.search(text)
				Beer["Brewery"] = Art_line.group(1)
				Beer["Name"] = Art_line.group(2)
				Beer["Style"] = Art_line.group(3)
				Beer["ABV"] = Art_line.group(4)
				Beer["UnitCount"] = Art_line.group(5)
				Beer["PSize"] = Art_line.group(6)
				Beer["Price"] = Art_line.group(7)
				Beer["PType(Keg or PKG)"] = "PKG"
				Beer["Raw_Package_data"] = Art_line.group(5), "x", Art_line.group(6)
				Beer_List.append(Beer)
			elif Art_RE_cl.search(text) != None:
				Art_line = Art_RE_cl.search(text)
				Beer["Brewery"] = Art_line.group(1)
				Beer["Name"] = Art_line.group(2)
				Beer["Style"] = Art_line.group(3)
				Beer["ABV"] = Art_line.group(4)
				Beer["UnitCount"] = Art_line.group(5)
				Beer["PSize"] = Art_line.group(6)
				Beer["Price"] = Art_line.group(7)
				Beer["PType(Keg or PKG)"] = "PKG"
				Beer["Raw_Package_data"] = Art_line.group(5), "x", Art_line.group(6)
				Beer_List.append(Beer)
			elif Art_RE_dash.search(text) != None:
				Art_line = Art_RE_dash.search(text)
				Beer["Brewery"] = Art_line.group(1)
				Beer["Name"] = Art_line.group(2)
				Beer["Style"] = Art_line.group(3)
				Beer["ABV"] = Art_line.group(4)
				Beer["UnitCount"] = Art_line.group(5)
				Beer["PSize"] = Art_line.group(6)
				Beer["Price"] = Art_line.group(7)
				Beer["PType(Keg or PKG)"] = "PKG"
				Beer["Raw_Package_data"] = Art_line.group(5), "x", Art_line.group(6)
				Beer_List.append(Beer)
			#These are Kegged products
			elif Art_RE_K_bbl.search(text) != None:
				Art_line = Art_RE_K_bbl.search(text)
				Beer["Brewery"] = Art_line.group(1)
				Beer["Name"] = Art_line.group(2)
				Beer["Style"] = Art_line.group(3)
				Beer["ABV"] = Art_line.group(4)
				Beer["UnitCount"] = 1
				Beer["PSize"] = Art_line.group(5)
				Beer["Price"] = Art_line.group(7)
				Beer["PType(Keg or PKG)"] = Art_line.group(6)
				Beer["Raw_Package_data"] = Art_line.group(5), "bbl", Art_line.group(6)
				if Beer["PSize"] == "1/2":
					Beer["PSize"] = "15.5"
				elif Beer["PSize"] == "1/6":
					Beer["PSize"] = "5"
				Beer_List.append(Beer)
			elif Art_RE_K_l.search(text) != None:
				Art_line = Art_RE_K_l.search(text)
				Beer["Brewery"] = Art_line.group(1)
				Beer["Name"] = Art_line.group(2)
				Beer["Style"] = Art_line.group(3)
				Beer["ABV"] = Art_line.group(4)
				Beer["UnitCount"] = 1
				Beer["PSize"] = Art_line.group(5)
				Beer["Price"] = Art_line.group(7)
				Beer["PType(Keg or PKG)"] = Art_line.group(6)
				Beer["Raw_Package_data"] = Art_line.group(5), "L", Art_line.group(6)
				Beer_List.append(Beer)
			else:
				pass





"""old code"""
		# #this splits the raw list into a new list for every line
		# art_item = x.split('\n')
		# #the following removes a consistent extra space that occurs at the end of every line
		# art_item.pop()
					# for text in artisan:
			# 	Art_line= Art_RE_ml.search(text)
			# 	if Art_line == None:
			# 		pass
			# 	else:
			# 		print Art_line.group()
#more old code
			# for text in artisan:
			# 	Art_line = Art_RE_oz.search(text)
			# 	if Art_line == None:
			# 		pass
			# 	else:
			# 		print Art_line.group()
				
			# for text in artisan:
			# 	Art_line = Art_RE_cl.search(text)
			# 	if Art_line == None:
			# 		pass
			# 	else:
			# 		print Art_line.group()

			# for text in artisan:
			# 	Art_line = Art_RE_dash.search(text)
			# 	if Art_line == None:
			# 		pass
			# 	else:
			# 		print Art_line.group()

	# 	artisan_raw_list = artisan.readlines()
	# for x in artisan_raw_list:
	# 	#this skips (presently) unuseful lines
	# 	if x ==' ' or x == '' or x == 'U.S.' or x == 'Belgium':
	# 		pass
	# 	else:
	

	# print artisan_raw_list

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


#next line for testing
# print "Welcome, Beer Buyer"
#This asks the user if they want to upload a Matagrano file, then runs the reader function:
def Mat_Choose_File():
	Mat_Q = raw_input("Would you like to choose a Matragrano file? Y or N: ")
	if Mat_Q == "Y" or Mat_Q == "y":
		Filename = raw_input("Please type the complete filename: ")
		Matagrano_Reader(Filename)
	else:
		pass

#Does the same for DBI
#This asks the user if they want to upload a Matagrano file, then runs the reader function:
def DBI_Choose_File():
	DBI_Q = raw_input("Would you like to choose a DBI file? Y or N: ")
	if DBI_Q == "Y" or DBI_Q == "y":
		Filename = raw_input("Please type the complete filename: ")
		DBI_Reader(Filename)
	else:
		pass

def Art_Choose_File():
	Art_Q = raw_input("Would you like to choose an Artisan file? Y or N: ")
	if Art_Q == "Y" or Art_Q == "y":
		Filename = raw_input("Please type the complete filename: ")
		Artisan_Reader(Filename)
	else:
		pass


def Hen_Choose_File():
	Hen_Q = raw_input("Would you like to choose a Henhouse file? Y or N: ")
	if Hen_Q == "Y" or Hen_Q == "y":
		Filename = raw_input("Please type the complete filename: ")
		Henhouse_Reader(Filename)
	else:
		pass


"""Testing for file choosing below"""
#Mat_Choose_File()
# DBI_Choose_File()