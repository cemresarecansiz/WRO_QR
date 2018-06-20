import pyrebase

config = {
  "apiKey": "AIzaSyD3bXRjLxEAVOKtj8hpjO4iI3Nn32F7agU",
  "authDomain": "foodcloud-f6eb1.firebaseapp.com",
  "databaseURL": "https://foodcloud-f6eb1.firebaseio.com/",
  "storageBucket": "foodcloud-f6eb1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

user = auth.sign_in_with_email_and_password('yigitcolakohlu@gmail.com', 'Ygtclksbl1')

db = firebase.database()


data_format_prod = {'Prod_Name':None, 'BBD':None,'Nutrients':[],'Calories':0,'Allergens':[],'Problematic':False,'Process':None, 'ED':None}
data_format_proc = {'Harvested':{'Date':'','Location':'','Product':''},'Transport1':{'Duration':0,'Moved to,from':'-','Condition':True,'Stopped':False},'Process':{'Location':'','Processes':''},'Transport2':{'Duration':0,'Moved to,from':'-','Condition':0,'Stopped':False},'Packaging':{'Location':'','Material':'','Cancerogen':True}}

data_2_prod = {'Prod_Name':"Chocolate", 'BBD':"28.01.2019",'Nutrients':['Lactose','Glucose','Cocoa'],'Calories':180,'Cooked':False,'Allergens':[""],'Problematic':False,'Process':''}
data_1_prod = {'Prod_Name':"Milk", 'BBD':"24.08.2018",'Nutrients':['Protein','Fat','Lactose','Glucose'],'Calories':120,'Cooked':False,'Allergens':['Lactose'],'Problematic':False,'Process':'Pastorized'}
data_2_proc = {'Harvested':{'Date':'24.04.2018','Location':'','Product':''},'Transport1':{'Duration':0,'Moved to,from':'-','Condition':0,'Stopped':False},'Process':{'Location':'','Processes':''},'Transport1':{'Duration':0,'Moved to,from':'-','Condition':0,'Stopped':False},'Packaging':{'Location':'','Material':'','Cancerogen':''}}
database_content = db.child("Products").get().val()

def getDate(product):
  return str((database_content[int(product)]['BBD']))




#db.child("Products").child("1").set(data_1_prod)
#db.child("Products").child("2").set(data_2_prod)

