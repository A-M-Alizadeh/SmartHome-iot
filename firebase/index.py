# env SMARTHOME_FB_CREDENTIALS
# echo 'export SMARTHOME_FB_CREDENTIALS=/Users/graybook/Documents/Projects/Polito/Secure/smart-home-22113-firebase-adminsdk-1zqx6-9859310965.json' >> ~/.zshenv

import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import os

# cred_obj = firebase_admin.credentials.Certificate(
#     os.environ.get('SMARTHOME_FB_CREDENTIALS'))
# default_app = firebase_admin.initialize_app(cred_obj, {
#     'databaseURL': 'https://smart-home-22113-default-rtdb.firebaseio.com'
# })


#---------------------------------------------------------------------------------Realtime Database
# ref = db.reference("/")
# ref.set({'name':'test'})
# ref.push({'name':'test2'})

# ref.child("users").push({"name":"Morty","age":14})
# ref.child("users").child("-NbswTxKFIIcnUJhL8e3").child("name").set("Mortimer Smith")

# ref.child("buidlings").child("1").child("rooms").child("1").child("devices").child("1").child("name").set("Lamp")



#---------------------------------------------------------------------------------Realtime Database
#---------------------------------------------------------------------------------Firestore Database
# Application Default credentials are automatically created.
cred_obj = credentials.Certificate(
    os.environ.get('SMARTHOME_FB_CREDENTIALS'))
app = firebase_admin.initialize_app(cred_obj)
# db = firestore.client()

# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
# doc_ref = db.collection("users").document("aturing")
# doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

# users_ref = db.collection("users")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")

#---------------------------------------------------------------------------------Firestore Database
#---------------------------------------------------------------------------------Authentication
# user = auth.create_user(
#     email='user@example.com',
#     email_verified=False,
#     phone_number='+15555550100',
#     password='secretPassword',
#     display_name='John Doe',
#     photo_url='http://www.example.com/12345678/photo.png',
#     disabled=False)
# print('Sucessfully created new user: {0}'.format(user.uid))

# user = auth.update_user(
#     uid='fsBFMTQHqThBwOvJ8Oy4sAcpoOZ2',
#     email='user@example.com',
#     phone_number='+15555550100',
#     email_verified=True,
#     password='newPassword',
#     display_name='John Doe',
#     photo_url='http://www.example.com/12345678/photo.png',
#     disabled=True)
# print('Sucessfully updated user: {0}'.format(user.uid))

# user = auth.get_user('fsBFMTQHqThBwOvJ8Oy4sAcpoOZ2')
# print('Successfully fetched user data: {0}'.format(user.email))

#---------------------------------------------------------------------------------Authentication

""""
Users:
-fname
-lname
-email
-password
-username
-created_at
-updated_at
-buidings
  -id
  -name
  -updated_at
  -rooms
    -id
    -name
    -updated_at
    -devices
      -id
      -name
      -type
      -status
      -topic
      -available
      -value_unit
      -updated_at

"""

""""
service registery:
  --what da fawk !!!
  --add all services
  --add all devices

"""
""""
authentification?

"""