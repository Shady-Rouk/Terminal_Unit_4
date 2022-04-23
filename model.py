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
from car import *

client = pymongo.MongoClient("mongodb+srv://admin:" + os.environ.get('TPASSWORD') + "@cluster0.bguvn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.myFirstDatabase

def get_user(email, password_hash):
    sellerDB = db.seller_information
    user = sellerDB.find_one({'email': email})
    person = Seller.from_document(user)
    return person


def sign_up_create(firstname, lastname, email, phone, password_hash):
    sellerDB = db.seller_information
    person = Seller(firstname, lastname, email, phone, password_hash)
    db_format = person.to_document()
    sellerDB.insert_one(db_format)
    return person

def create_car(new_car):
    carDB = db.cars
    new_car = Seller.from_form(new_car)
    new_car_doc = new_car.to_document()
    carDB.insert_one(new_car_doc)
    return new_car_doc