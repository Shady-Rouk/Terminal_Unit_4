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
from model import *
from bson.objectid import ObjectId

# -- Initialization section --
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

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

# HOME Route
@app.route('/')
@app.route('/home')
def home():
    if session:
        # return render_template('index.html') with session
        return render_template('index.html')
    else:
        return render_template('index.html')

# SIGN IN Route
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html', valid=True)
    else:
        #set session here
        users = mongo.db.seller_information
        sign_in_user = users.find_one({'email': request.form['email']})
        if not sign_in_user:
            return render_template('sign_in.html', valid=False)
        else:
            db_password = sign_in_user['password_hash']
            input_password = request.form['password'].encode('utf-8')
            if bcrypt.checkpw(input_password, db_password):
                # user_obj = model.get_user(request.form['email'], request.form['password'].encode('utf-8'))
                session['user'] = request.form['email']
                return redirect('/my_listings')
            else:
                return render_template('sign_in.html', valid=False)

# SIGN UP Route
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html', valid=True)
    else:
        #set session here
        users = mongo.db.seller_information
        existing_user = users.find_one({'email': request.form['email']})
        if not existing_user:
            f_name = request.form['firstname']
            l_name = request.form['lastname']
            email = request.form['email']
            phone = request.form['phone']
            password = request.form['password'].encode('utf-8')
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password, salt)
            person_obj = model.sign_up(f_name, l_name, email, phone, password_hash)
            session['user'] = person_obj.email
            return redirect('/my_listings')
        else:
            return render_template('sign_up.html', valid=False)
            

# MY LISTINGS Route
@app.route('/my_listings', methods=['GET', 'POST'])
def my_listings():
    if session:
        if request.method == 'GET':
            #get username from session, do a check for session
            users = mongo.db.seller_information
            curr_user = users.find_one({'email': session['user']})
            user_car_ids = curr_user['cars'] #user_car_ids is a list of car IDs
            cars = [] #list of car documents, should be converted to car objects? with individual attributes
            for car_id in user_car_ids:
                car = mongo.db.cars.find_one({'_id': ObjectId(car_id)})
                cars.append(car)
            # cars = [Car(group[all parameters]) for group in cars]
            return render_template('my_listings.html', my_cars=cars, user=curr_user) #my_cars(for car details) and user(for details) used for jinja in my_listings.html
        else:
            pass
    else:
        return redirect('/sign_in')

# CREATE LISTING Route
@app.route('/create_listing', methods=['GET', 'POST'])
def create_listing():
    if session:
        if request.method == 'GET':
            #get username from session, do a check for session
            return render_template('create_listing.html')
        else:
            pass
    else:
        return redirect('/sign_in')
        
# LOGOUT Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# CARS Route
@app.route('/cars', methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        return render_template('cars.html', session=session)
    else:
        pass

# ABOUT Route
@app.route('/about')
def about():
    return render_template('about.html')

#CAR REPORTS Route
@app.route('/reports/<car_id>', methods=['GET', 'POST'])
def car_report(car_id):
    if request.method == 'GET':
        return render_template("CarReports.html", car_id=car_id)    
    else:

        details = {}
        details['make'] = request.form.get('make', False)
        details['model'] = request.form.get('model', False)
        details['color'] = request.form.get('color', False)
        details['year'] = request.form.get('year', False)
        # if request.form.get('make'): 
        #     details['make'] = True
        features = request.form['features']
        date = request.form['date']

        new_car_report(car_id, details, features, date)

        return render_template("reports.html", valid=True, approved=True)




@app.route('/reports', methods=['GET', 'POST'])
def reports():
    if request.method == "GET":
        return render_template("reports.html", valid=True, approved=False)
    else:
        car_id = request.form['car_id']
        
        valid = validate(car_id)
        if not valid:
            return render_template("reports.html", valid=False, approved=False)
        car_exists = verify_id_exists(car_id)
        if not car_exists:
            return render_template("reports.html", valid=False, approved=False)
        else:
            return redirect('/reports/' + car_id)

