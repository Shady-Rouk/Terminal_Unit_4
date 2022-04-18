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
from flask import request, redirect
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "<replace_with_real_mongodb_url>"

#Initialize PyMongo
mongo = PyMongo(app)

# -- Routes section --
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
        pass

# SIGN UP Route
@app.route('sign_up', methods=['GET', 'POST'])
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
@app.route('my_listings', methods=['GET', 'POST'])
def my_listings():
    if request.method == 'GET':
        #get username from session, do a check for session
        return render_template('my_listings.html')
    else:
        pass

# CREATE LISTING Route
@app.route('create_listing', methods=['GET', 'POST'])
def create_listing():
    if request.method == 'GET':
        #get username from session, do a check for session
        return render_template('create_listing.html')
    else:
        pass