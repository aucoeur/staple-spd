import bcrypt
from bson.objectid import ObjectId
from flask import Flask, flash, render_template, url_for, request, session, redirect
# from flask_pymongo import PyMongo
from flask_api import FlaskAPI
import json
import os
from pymongo import MongoClient

app = FlaskAPI(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/staple')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

#used to encode the session (which in theory is just an encrypted cookie)
# app.config['SECRET_KEY'] = secret_key

# mongo = PyMongo(app)
users = db.users    #creates db for users
docs = db.docs      #creates db for documentations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    #return login page
    if request.method == "GET":
        return render_template('login.html')

    #submitting a login request
    login_user = users.find_one({'name' : request.form['username']})    #check to see if theres a user with the same inputted username

    #not sure if we need to the if statement? ask padyn later
    if request.method == "POST":
        if login_user:
            #encrypts user inputted password and see if it matches the encrypted password in the document found earlier
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                #return redirect(url_for('profile')) #do we need a profile page? ask padyn later
                return {'user' : login_user}

    #if invalid login credentials
    flash('Invalid login')
    return redirect(url_for('login'))
    #ideally it says invalid login and then directs you back to the login page
    #return redirect(request.url)       #back to the login page

@app.route('/register', methods=['POST', 'GET'])
def register():
    #return login page
    if request.method == "GET":
        return render_template('register.html')

    #submitting a new user document
    if request.method == 'POST':
        existing_user = users.find_one({'username' : request.form['username']}) #check to see if theres a user with the same inputted username
        
        #if username doesnt exist, register new user
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insertOne({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('login'))           #redirect them to login after registering
        
        #return None if the username exists already
        flash('Username/password exists')
        return None

# @app.route('/profile')
# def profile():
#     return render_template('profile.html', name=users.username)

# @app.route('/view/<api_id>')
# def view():
    
#     return r

@app.route('/create/', methods=['POST', 'GET'])
def create():
    if request.method == "GET":
        #checks to see if the user is logged in before allowing edits
        if session.get("username", None) is not None:
            return render_template('edit.html')
        #redirects to login page if not logged in
        else:
            return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['username'].upper()
        existing_docs = users.find_one({'username' : title})

        #if api doest exist already create new api + docs
        if existing_docs is None:
            doc = {
                'api_name' : title, 
                'documentation': request.form['doc']
            }
            doc_info = docs.insertOne(doc)
            return redirect(url_for('view', doc_info=doc_info))
        
        #return None if the username exists already
        return None

#logout
@app.route('/logout')
def logout():
    #after logging out, return user to the page they were on, 
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))