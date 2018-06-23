import json

data_format_prod = {
	'Prod_Name': None, 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Allergens': [],
	'Problematic': False, 'Process': None, 'ED': None
}

data_format_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': ''},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False},
	'Process': {'Location': '', 'Processes': ''},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': 0, 'Stopped': False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True}
}

data_1_prod = {
	'Prod_Name': "Milk", 'BBD': "24.08.2018", 'Nutrients': ['Protein', 'Fat', 'Lactose', 'Glucose'],
	'Calories': 120, 'Cooked': False, 'Allergens': ['Lactose'], 'Problematic': False,
	'Process': 'Pastorized'
}

data_2_prod = {
	'Prod_Name': "Chocolate", 'BBD': "28.01.2019", 'Nutrients': ['Lactose', 'Glucose', 'Cocoa'],
	'Calories': 180, 'Cooked': False, 'Allergens': [""], 'Problematic': False, 'Process': ''
}

data_1_proc = {
	'Harvested': {
		'Date': '18.08.2018', 'Location': 'Larson Family',
		'Product': 'Raw Milk'
	},
	'Transport1': {
		'Duration': 9, 'Moved to,from': 'Larson Family-McCarty Family Farms', 'Condition': True,
		'Stopped': True
	}, 'Process': {
		'Location': 'McCarty Family Farms',
		'Processes': 'Reverse Osmosis,Nanofiltration,Ultrafiltration,Microfiltration'
	},
	'Transport2': {
		'Duration': 13, 'Moved to,from': 'McCarty Family Farms-JJX Packaging', 'Condition': True,
		'Stopped': True
	},
	'Packaging': {'Location': 'JJX Packaging', 'Material': 'Carton', 'Cancerogen': False}
}

data_2_proc = {
	'Harvested': {
		'Date': '27.01.2018', 'Location': 'India',
		'Product': 'Cocoa'
	},
	'Transport1': {'Duration': 71, 'Moved to,from': 'India-Nestle ', 'Condition': True, 'Stopped': True},
	'Process': {'Location': 'Nestle', 'Processes': 'Roasting,Pulp,Conching,Moulding'},
	'Transport2': {
		'Duration': 4, 'Moved to,from': 'Nestle-Ulma Packaging', 'Condition': True,
		'Stopped': False
	},
	'Packaging': {'Location': 'Ulma Packaging', 'Material': 'Foil', 'Cancerogen': False}
}

Products = [data_1_prod, data_2_prod]
Processes = [data_1_proc, data_2_proc]

for i in range(len(Products)):
	with open('../database/content/Products/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Products[i], outfile)
		outfile.close()


for i in range(len(Processes)):
	with open('../database/content/Processes/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Processes[i], outfile)
		outfile.close()