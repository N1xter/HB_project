from string import join

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
		#below is the input-specific parsing algorithm
		# this splits each line into its own list of items
		Mat_item = x.split()
		#print len(Mat_item)
		#this prevents errors from empty lines
		Beer = {"Brewery":None, "Name": None, "Style":None, "ABV":None, "Raw_Package_data":None, "PType(Keg or PKG)": None, "PSize":None, "Distributor":"Matagrano", "UnitCount":None, "Price":None,}
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
			# this prompts for user inputs when the value is None
			Bkeys = Beer.keys()
			for key in Bkeys:
				if Beer[key] == None:
					Prompt_text = "For the Beer:", Beer["Brewery"], Beer["Name"], Beer["Raw_Package_data"], "Please enter the", key, ": "
					Beer[key] = raw_input(Prompt_text)
			Beer_List.append(Beer)

#TESTING This calls the function and prints the result for
Matagrano_Reader("Matagrano_sample.txt")
print Beer_List


	
