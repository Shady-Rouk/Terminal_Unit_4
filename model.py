# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import pymongo
import bcrypt
from seller import *
from CarReports import *
from bson.objectid import ObjectId
from car import *

client = pymongo.MongoClient("mongodb+srv://admin:" + os.environ.get('TPASSWORD') + "@cluster0.bguvn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.myFirstDatabase

def get_user(email, password_hash):
    """Creates an instance of a Seller from their email address and password_hash

    Args:
        email (str): The seller's email address to sign in.
        password_hash (Binary): The hashed value for the seller's account password.
    Returns:
        Seller: An instance of the seller who is currently in session.
    """
    sellerDB = db.seller_information
    user = sellerDB.find_one({'email': email})
    person = Seller.from_document(user)
    return person


def sign_up_create(firstname, lastname, email, phone, password_hash):
    """Creates a new Seller object and adds the details to the seller_information collection in the database

    Args:
        firstname (str): The first name of the seller.
        lastname (str): The last name of the seller.
        email (str): The email address of the seller.
        phone (str): The phone number of the seller.
        password_hash (Binary): The hashed form of a seller's account password.
    Returns:
        Seller: An instance of the seller who just created an account.
    """
    sellerDB = db.seller_information
    person = Seller(firstname, lastname, email, phone, password_hash)
    db_format = person.to_document()
    sellerDB.insert_one(db_format)
    return person

def validate(car_id):

    if len(car_id) != 24:
        return False

    for el in car_id:
        if el not in '0123456789ABCDEabcde':
            return False

    return True

def verify_id_exists(car_id):

    carsDB = db.cars
    # car_ids = carsDB.find({}, {'make': 0, 'model':0, 'year':0, 'color':0, 'price':0, 'phone':0, 
    # 'email':0, 'picture':0, 'sold':0, 'verified':0})
    car_exists = carsDB.find_one({'_id': ObjectId(car_id)})
    
    return car_exists != None


# would the object id clash if the id is slightly different.
# how to find the id or what is the id given to the inspector
# when updating the report DB should we put update and add to in the same function or different ones
# _id and id column not the same thing

def new_car_report(car_id, details, features, date):
    #verify id is an int or string

    car_reportDB = db.car_reports
    report_exists = car_reportDB.find_one({'car_id': car_id})

    if len(features) != 0:
        features = features.split(',')
    report_instance = CarReports(car_id, details, features, date)
    is_verified = report_instance.isDetailsVerified()

    if not is_verified:
        # is this information useful to store
        report_instance.getUnverified()

    new_entry = report_instance.to_document()

    if not report_exists:
        car_reportDB.insert_one(new_entry)

    else:
        car_reportDB.update_one({'car_id': car_id}, 
        {'$set': {'details': new_entry['details'], 'features':new_entry['features'], 
        'is_verified': new_entry['is_verified'], 'unverified_details': new_entry['unverified_details'], 'date': new_entry['date']}})

    if new_entry['is_verified']:
        carDB = db.cars
        carDB.update_one({'_id': ObjectId(new_entry['car_id'])}, {'$set': {'verified': True}})


def create_car(new_car):
    """Creates a new Seller object and adds the details to the seller_information collection in the database
    Collects car information from the request and calls the from_form method from the Car class. 
    After a new_car_doc is created with the to_document method and inserted into the database
    Returns:
        Seller: An instance of the seller who just created an account.
    """
    carDB = db.cars
    new_car = Car.from_form(new_car)
    new_car_doc = new_car.to_document()
    carDB.insert_one(new_car_doc)
    return new_car_doc
