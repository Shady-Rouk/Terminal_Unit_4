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

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect, session
from flask_pymongo import PyMongo
import os
import bcrypt
import model

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:" + os.environ.get('TPASSWORD') + "@cluster0.bguvn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)
# mongo.db.create_collection('cars')
# mongo.db.create_collection('seller_information')
# mongo.db.create_collection('car_reports')


# -- Routes section --
# SEED Route
@app.route('/seed')
def seed():
    return redirect('/')

# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# SIGN IN Route
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
        #set session here
        users = mongo.db.seller_information
        sign_in_user = users.find_one({'email': request.form['email']})
        if not sign_in_user:
            return "invalid email/password combo"
        else:
            db_password = sign_in_user['password_hash']
            input_password = request.form['password'].encode('utf-8')
            if bcrypt.checkpw(input_password, db_password):
                session['user'] = model.sign_in(request.form['email'], request.form['password'].encode('utf-8'))
                return redirect('/')
            else:
                return "invalid email/password combo"

# SIGN UP Route
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        #set session here
        pass

# MY ACCOUNT Route
# @app.route('myaccount', methods=['GET', 'POST'])
# def my_account():
#     if request.method == 'GET':
#         #get username from session, do a check for session
#         return render_template('my_account.html')
#     else:
#         pass

# MY LISTINGS Route
@app.route('/my_listings', methods=['GET', 'POST'])
def my_listings():
    if request.method == 'GET':
        #get username from session, do a check for session
        return render_template('my_listings.html')
    else:
        pass

# CREATE LISTING Route
@app.route('/create_listing', methods=['GET', 'POST'])
def create_listing():
    if request.method == 'GET':
        #get username from session, do a check for session
        return render_template('create_listing.html')
    else:
        pass
