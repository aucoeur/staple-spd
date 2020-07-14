import os
import bcrypt
from bson.objectid import ObjectId
from flask import Flask, flash, render_template, url_for, request, session, redirect, jsonify
# from flask_pymongo import PyMongo
from flask_api import FlaskAPI, status, exceptions
import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = FlaskAPI(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/staple')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

#used to encode the session (which in theory is just an encrypted cookie)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'changeme')

# mongo = PyMongo(app)
users = db.users    #creates db for users
docs = db.docs      #creates db for documentations

#home (change what to return to?)
# @app.route('/staple')
#home (change what to return to for final integration)
@app.route('/')
def index():
    return render_template('index.html')    #FOR TESTING PURPOSES ONLY, change what to return to for final version

#login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    #return login page
    if request.method == "GET":
        return render_template('login.html')    #FOR TESTING PURPOSES ONLY, change what to return to for final version

    #submitting a login request
    login_user = db.users.find_one({'name' : request.form['username']})    #check to see if theres a user with the same inputted username
    if request.method == "POST":
        if login_user:
            #FIX LATER? encrypts user inputted password and see if it matches the encrypted password in the document found earlier
            #if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:

            #checks to see if password from form matches the found user
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']     #set session user to the logged in user

                #Profile page Feature to be added later #return redirect(url_for('profile'))

                #return {'user' : login_user['password']}#login_user} #return the user object or username? decide later
                return redirect(url_for('index'))    #FOR TESTING ONLY, uncomment above for final
        else:
            return 'Invalid login information'
            #return {'failure': status.HTTP_401_UNAUTHORIZED }
            # render_template('failure.html')    #FOR TESTING ONLY, uncomment above for final

    #if invalid login credentials
    # flash('Invalid login')      
    # return redirect(url_for('login'))
    #ideally it says invalid login and then directs you back to the login page
    #return redirect(request.url)       #back to the login page

#register new user
@app.route('/register', methods=['POST', 'GET'])
def register():
    #return login page
    if request.method == "GET":
        return render_template('register.html')

    #submitting a new user document
    if request.method == 'POST':
        existing_user = db.users.find_one({'name' : request.form['username']}) #check to see if theres a user with the same inputted username
        #maybe put all the below in a loop?
        #if username doesnt exist, register new user
        if existing_user is None:
            #FIX LATER #hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            db.users.insert_one({'name' : request.form['username'], 'password' : request.form['password']})#hashpass})
            session['user'] = request.form['username']
            return redirect(url_for('login'))           #redirect them to login after registering
        
        #return None if the username exists already
        return 'Username/password exists'
    return {'response': status.HTTP_401_UNAUTHORIZED }

#future profile feature
# @app.route('/profile')
# def profile():
#     return render_template('profile.html', name=users.username)

#view a single API's Docs
@app.route('/view/<api_id>', methods=['GET'])
def view():
    return {'response': docs.find_one({'_id': request.args['api_id']})}

#edit an API's doc's
@app.route('/edit/<api_id>', methods=['POST', 'GET'])
def edit():
    if request.method == "GET":
        #if the person isnt logged in
        if session.get("username", None) is not None:
            return render_template('edit.html')
        #person is logged
        else:
            return redirect(url_for('login'))

    if request.method == 'POST':
        existing_docs = docs.find_one({'_id': request.args['api_id']})      #finds documentation you want
        #if api doest exist already create new api + docs
        if existing_docs is None:
            doc = {
                'api_name' : request.form['doc'], 
                'documentation': request.form['doc']
            }
            doc_info = docs.insertOne(doc)
            return redirect(url_for('view', id=doc_info._id))           #redirect them to login after registering
        

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "GET":
        #checks to see if the user is logged in before allowing edits
        if session.get("user", None) is not None:
            return render_template('create.html')
        #redirects to login page if not logged in
        else:
            return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['api_name'].upper()      #make API uppercase
        existing_docs = docs.find_one({'api_name' : title}) #check to see if theere docs with that title already

        #if api doest exist already create new api + docs
        if existing_docs is None:
            #create new dictionary to insert to db
            doc = {
                'api_name' : title, 
                'documentation': request.form['documentation']
            }   
            db.docs.insert_one(doc)      #insert to db#doc_info = db.docs.insert_one(doc)      #insert to db
            #return redirect(url_for('view', id=doc_info._id))           #redirect them to login after registering
            return render_template('index.html')    #FOR TESTING ONLY, uncomment above for final

        
        #return None if the username exists already
        return {'response': status.HTTP_401_UNAUTHORIZED }

#logout
@app.route('/logout')
def logout():
    session.clear()     #clear cookies
    return redirect(url_for('index'))       #after logging out, return user to the page they were on, 

@app.route('/test')
def test():
    # return '{hello: world}'
    return jsonify(hello='hello')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))