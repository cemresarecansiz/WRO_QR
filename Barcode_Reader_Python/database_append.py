import json

data_format_prod = {
	'Prod_Name': None, 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}

data_format_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}

data_1_prod = {
	'Prod_Name': "Milk", 'BBD': "24.08.2018", 'Nutrients': ['Protein', 'Fat', 'Lactose', 'Glucose'],
	'Calories': 120, 'Cooked': False, 'Allergens': ['Lactose'], 'Problematic': False,
	'Process': 'Pastorized', 'ED': "02.09.2018"
}

data_2_prod = {
	'Prod_Name': "Chocolate", 'BBD': "28.01.2019", 'Nutrients': ['Lactose', 'Glucose', 'Cocoa'],
	'Calories': 180, 'Cooked': False, 'Allergens': ['Cocoa', 'Lactose'], 'Problematic': False, 'Process': 'None',  'ED': "21.02.2019"
}
data_3_prod = {
	'Prod_Name': "Delitos", 'BBD': "19.12.2018", 'Nutrients': ['Protein', 'Carbohydrate', 'Fibre', 'Soduium', 'Fat', 'Salt'],
	'Calories': 160, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': False,
	'Process': 'Fried', 'ED': "02.09.2018"
}
data_4_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "02.11.2018", 'Nutrients': ['Protein', 'Carbohydrate', 'Fibre', 'Sodium', 'Fat', 'Sugar', 'Salt'],
	'Calories': 439, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': False,
	'Process': 'Baking', 'ED': "08.12.2018"
}
data_5_prod = {
	'Prod_Name': Gluten Free Penne Rigate, 'BBD': 18.02.2019, 'Nutrients': ['Protein', 'Carbohydrate', 'Fiber', 'Sodium', 'Fat', 'Salt'], 'Calories': 359,'Cooked': False 'Allergens': ['Wheat'],
	'Problematic': False, 'Process': 'Klining', 'ED': 18.02.2020
}
data_6_prod = {
	'Prod_Name': EGE Gluten Free Corn Stach, 'BBD': 27.03.2019, 'Nutrients': ['Fat', 'Carbohydrate', 'Protein'], 'Calories': 360,'Cooked': False 'Allergens': ['Corn'],
	'Problematic': False, 'Process': Scalping, 'ED': 20.02.2020
}
data_7_prod = {
	'Prod_Name': Tropical Heat Peanuts, 'BBD': 04.02.2019, 'Nutrients': ['Protein', 'Carbohydrate', 'Sugar', 'Saturated Fat', 'Mono-unsaturated Fat', 'Poly-unsaturated Fat', 'Fibre','Salt'], 'Calories': 602,'Cooked': False 'Allergens': ['Peanuts'],
	'Problematic': False, 'Roasted': None, 'ED': 09.03.2020
}


data_1_proc = {
	'Harvested': {
		'Date': '18.08.2018', 'Location': 'Larson Family',
		'Product': 'Raw Milk'
,'Problematic':False
	},
	'Transport1': {
		'Duration': 9, 'Moved to,from': 'Larson Family-McCarty Family Farms', 'Condition': True,
		'Stopped': True
,'Problematic':True
	}, 'Process': {
		'Location': 'McCarty Family Farms',
		'Processes': 'Reverse Osmosis,Nanofiltration,Ultrafiltration,Microfiltration'
,'Problematic':False
	},
	'Transport2': {
		'Duration': 13, 'Moved to,from': 'McCarty Family Farms-JJX Packaging', 'Condition': True,
		'Stopped': True
,'Problematic':False
	},
	'Packaging': {'Location': 'JJX Packaging', 'Material': 'Carton', 'Cancerogen': False,'Problematic':True}
}

data_2_proc = {
	'Harvested': {
		'Date': '27.01.2018', 'Location': 'India',
		'Product': 'Cocoa','Problematic':True
	},
	'Transport1': {'Duration': 71, 'Moved to,from': 'India-Nestle ', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Nestle', 'Processes': 'Roasting,Pulp,Conching,Moulding','Problematic':False},
	'Transport2': {
		'Duration': 4, 'Moved to,from': 'Nestle-Ulma Packaging', 'Condition': True,
		'Stopped': False,'Problematic':False
	},
	'Packaging': {'Location': 'Ulma Packaging', 'Material': 'Foil', 'Cancerogen': False,'Problematic':False}
}
data_3_proc = {
	'Harvested': {'Date': '06.05.2018', 'Location': 'India', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 19, 'Moved to,from': 'India-Gee Tee Industries', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen': False,'Problematic': False}
}
data_4_proc = {
	'Harvested': {'Date': '14.05.2017', 'Location': 'Turkey', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 23, 'Moved to,from': 'Turkey-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':False},
	'Transport2': {'Duration': 7, 'Moved to,from': 'Galletas Gullon SA-Greif Packaging Spain SA', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Greif Packaging Spain SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_5_proc = {
	'Harvested': {'Date': '15.06.2017', 'Location': 'Russia', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 29, 'Moved to,from': 'Russia-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling ','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_6_proc = {
	'Harvested': {'Date': '16.08.2017', 'Location': 'USA', 'Product': 'Corn','Problematic':False},
	'Transport1': {'Duration': 28, 'Moved to,from': 'USA-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'EGE Gluten Free Food Product Company-Starpak Packaging Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Starpak Packaging Company', 'Material': 'Recyclable Plastic', 'Cancerogen': False,'Problematic':False}
}
data_7_proc = {
	'Harvested': {'Date': '02.04.2018', 'Location': 'Kenya', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 8, 'Moved to,from': 'Kenya-Deepa Industries LTD', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':False},
	'Transport2': {'Duration': 0.5, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': False,'Problematic':False}
}


Products = [data_1_prod, data_2_prod, data_3_prod, data_4_prod,data_5_prod,data_6_prod,data_7_prod]
Processes = [data_1_proc, data_2_proc, data_3_proc,data_4_proc,data_5_proc,data_6_proc,data_7_proc]

for i in range(len(Products)):
	with open('../database/content/Products/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Products[i], outfile)
		outfile.close()


for i in range(len(Processes)):
	with open('../database/content/Processes/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Processes[i], outfile)
		outfile.close()
