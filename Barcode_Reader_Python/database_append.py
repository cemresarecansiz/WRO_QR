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
	'Prod_Name': "Delitos", 'BBD': "19.12.2018", 'Nutrients': ['Protein', 'Carbohydrate', 'Fibre', 'Soduium', 'Fat', 'Salt'],
	'Calories': 160, 'Cooked': True, 'Allergens': ['Lactose','Gluten', 'Nuts'], 'Problematic': False,
	'Process': 'Fried', 'ED': "02.09.2018"
}
data_2_prod = {
	'Prod_Name': "Delitos" , 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_3_prod = {
	'Prod_Name': "Delitos",, 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_4_prod = {
	'Prod_Name': "Delitos",, 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_5_prod = {
	'Prod_Name': "Delitos",, 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_6_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': "02.11.2018", 'Nutrients': ['Protein', 'Carbohydrate', 'Fibre', 'Sodium', 'Fat', 'Sugar', 'Salt'],
	'Calories': 439, 'Cooked': True, 'Allergens': ['Lactose', 'Wheat', 'Soya'], 'Problematic': False,
	'Process': 'Baking', 'ED': "08.12.2018"
}
data_7_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_8_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_9_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_10_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_11_prod = {
	'Prod_Name': "Gluten Free Penne Rigate", 'BBD': 18.02.2019, 'Nutrients': ['Protein', 'Carbohydrate', 'Fiber', 'Sodium', 'Fat', 'Salt'], 'Calories': 359,'Cooked': False 'Allergens': ['Wheat'],
	'Problematic': False, 'Process': 'Klining', 'ED': 18.02.2020
}
data_12_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_13_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_14_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_15_prod = {
	'Prod_Name': "Gullon Sugar Free Shortbread Biscuits", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_16_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': 27.03.2019, 'Nutrients': ['Fat', 'Carbohydrate', 'Protein'], 'Calories': 360,'Cooked': False 'Allergens': ['Corn'],
	'Problematic': False, 'Process': Scalping, 'ED': 20.02.2020
}
data_17_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_18_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_19_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_20_prod = {
	'Prod_Name': "EGE Gluten Free Corn Starch", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_21_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': 04.02.2019, 'Nutrients': ['Protein', 'Carbohydrate', 'Sugar', 'Saturated Fat', 'Mono-unsaturated Fat', 'Poly-unsaturated Fat', 'Fibre','Salt'], 'Calories': 602,'Cooked': False 'Allergens': ['Peanuts'],
	'Problematic': False, 'Roasted': None, 'ED': 09.03.2020
}
data_22_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_23_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_24_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}
data_25_prod = {
	'Prod_Name': "Tropical Heat Peanuts", 'BBD': None, 'Nutrients': [], 'Calories': 0, 'Cooked': False 'Allergens': [], 'Problematic': False, 'Process': None, 'ED': None
}


data_1_proc = {
	'Harvested': {'Date': '06.05.2018', 'Location': 'India', 'Product': 'Potatoe','Problematic':False},
	'Transport1': {'Duration': 19, 'Moved to,from': 'India-Gee Tee Industries', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Gee Tee Industries', 'Processes': 'Peeling, Slicing, Frying','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': 'Gee Tee Industries-Gee Tee Industries', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Gee Tee Industries', 'Material': 'Polypropylene', 'Cancerogen': False,'Problematic': False}
}
data_2_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_3_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_4_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_5_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}

data_6_proc = {
	'Harvested': {'Date': '14.05.2017', 'Location': 'Turkey', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 23, 'Moved to,from': 'Turkey-Galletas Gullon SA', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Galletas Gullon SA', 'Processes': 'Kneading, Moulding, Baking, Cooling','Problematic':False},
	'Transport2': {'Duration': 7, 'Moved to,from': 'Galletas Gullon SA-Greif Packaging Spain SA', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Greif Packaging Spain SA', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_7_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_8_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_9_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_10_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_11_proc = {
	'Harvested': {'Date': '15.06.2017', 'Location': 'Russia', 'Product': 'Wheat','Problematic':False},
	'Transport1': {'Duration': 29, 'Moved to,from': 'Russia-Barilla', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Barilla', 'Processes': 'Pressing, Moulding, Klining, Ensiling ','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'Barilla-Barilla', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Barilla', 'Material': 'Carton', 'Cancerogen': False,'Problematic':False}
}
data_12_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_13_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_14_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_15_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_16_proc = {
	'Harvested': {'Date': '16.08.2017', 'Location': 'USA', 'Product': 'Corn','Problematic':False},
	'Transport1': {'Duration': 28, 'Moved to,from': 'USA-EGE Gluten Free Food Product Company', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'EGE Gluten Free Food Product Company', 'Processes': 'Cleaning, Maceration, Core Scalping, Bran Scalping, Protein Scalping, Starch Purification','Problematic':False},
	'Transport2': {'Duration': 1, 'Moved to,from': 'EGE Gluten Free Food Product Company-Starpak Packaging Company', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Starpak Packaging Company', 'Material': 'Recyclable Plastic', 'Cancerogen': False,'Problematic':False}
}
data_17_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_18_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_19_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_20_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_21_proc = {
	'Harvested': {'Date': '02.04.2018', 'Location': 'Kenya', 'Product': 'Peanuts','Problematic':False},
	'Transport1': {'Duration': 8, 'Moved to,from': 'Kenya-Deepa Industries LTD', 'Condition': True, 'Stopped': True,'Problematic':False},
	'Process': {'Location': 'Deepa Industries LTD', 'Processes': 'Peeling, Roasting, Salting','Problematic':False},
	'Transport2': {'Duration': 0.5, 'Moved to,from': 'Deepa Industries LTD-Deepa Industries LTD', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': 'Deepa Industries LTD', 'Material': 'Plastic', 'Cancerogen': False,'Problematic':False}
}
data_22_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_23_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_24_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}
data_25_proc = {
	'Harvested': {'Date': '', 'Location': '', 'Product': '','Problematic':False},
	'Transport1': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Process': {'Location': '', 'Processes': '','Problematic':False},
	'Transport2': {'Duration': 0, 'Moved to,from': '-', 'Condition': True, 'Stopped': False,'Problematic':False},
	'Packaging': {'Location': '', 'Material': '', 'Cancerogen': True,'Problematic':False}
}


Products = [data_1_prod, data_2_prod, data_3_prod, data_4_prod, data_5_prod, data_6_prod, data_7_prod, data_8_prod, data_9_prod, data_10_prod, data_11_prod, data_12_prod, data_13_prod, data_14_prod, data_15_prod, data_16_prod, data_17_prod, data_18_prod, data_19_prod, data_20_prod, data_21_prod, data_22_prod, data_23_prod, data_24_prod, data_25_prod]
Processes = [data_1_proc, data_2_proc, data_3_proc, data_4_proc, data_5_proc, data_6_proc, data_7_proc, data_8_proc, data_9_proc, data_10_proc, data_11_proc, data_12_proc, data_13_proc, data_14_proc, data_15_proc, data_16_proc, data_17_proc, data_18_proc, data_19_proc, data_20_proc, data_21_proc, data_22_proc, data_23_proc, data_24_proc, data_25_proc]

for i in range(len(Products)):
	with open('../database/content/Products/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Products[i], outfile)
		outfile.close()


for i in range(len(Processes)):
	with open('../database/content/Processes/'+str(i+1) + '.json', 'w') as outfile:
		json.dump(Processes[i], outfile)
		outfile.close()
