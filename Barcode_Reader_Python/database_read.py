import pyrebase

config = {
  "apiKey": "AIzaSyD3bXRjLxEAVOKtj8hpjO4iI3Nn32F7agU",
  "authDomain": "foodcloud-f6eb1.firebaseapp.com",
  "databaseURL": "https://foodcloud-f6eb1.firebaseio.com/",
  "storageBucket": "foodcloud-f6eb1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

user = auth.sign_in_with_email_and_password('yigitcolakohlu@gmail.com', 'FoodWro2018')

db = firebase.database()

database_content = db.child("Products").get().val()

def getDate(product):
  return str((database_content[int(product)]['BBD']))

