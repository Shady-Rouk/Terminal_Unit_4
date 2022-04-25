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

    '''
    Checks to see if a potential car_id is in the correct format (length of 16 characters and hexadecimal)

    Args:
        car_id (str): the potential id of a car in the cars collection

    Returns:
        boolean: True if car_id is in the correct format, False if it is not. 
    '''    

    if len(car_id) != 24:
        return False

    for el in car_id:
        if el not in '0123456789ABCDEabcde':
            return False

    return True

def verify_id_exists(car_id):

    '''
    Checks to see if an id for a car is present in the cars collection

    Args:
        car_id (str): the potentital id of a car in the cars collection

    Returns:
        boolean: True if there is a car in the collection with the same id as car_id, False if there is not a car in the 
        collection with the same id.
    '''

    carsDB = db.cars
    car_exists = carsDB.find_one({'_id': ObjectId(car_id)})
    
    return car_exists != None


def new_car_report(car_id, details, features, date):
    '''
    Creates a CarReports instance using the parameters. Uses the passed in attribute values of the object to update the verified,
    unverified_details attributes of the object. Checks whether or not the car's id already exists in the car_reports collection. 
    If the car's id does exist, the fields associated with the car id are updated. If the car's id does not exist in the collection,
    a new entry is inserted into the car_reports collection.

    Args:
        car_id (str): the potentital id of a car in the cars collection.
        details(dict): contains general characteristics about the car (year, make, model, color) as keys,
        and booleans as values.
        features(str): additional features of the car for sale in the collection/database.
        date(str): the date that the report was conducted.

    returns:
        None (void)
        
    '''

    car_reportDB = db.car_reports
    report_exists = car_reportDB.find_one({'car_id': car_id})

    if len(features) != 0:
        features = features.split(',')
    report_instance = CarReports(car_id, details, features, date)
    is_verified = report_instance.isDetailsVerified()

    if not is_verified:
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
