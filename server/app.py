from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from flask_api import FlaskAPI
import bcrypt

app = FlaskAPI(__name__)

app.config['MONGO_DBNAME'] = 'staple'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/staple'

mongo = PyMongo(app)
users = mongo.db.users    #creates db for users
apis = mongo              #creates db for api 

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
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                #return redirect(url_for('profile')) #do we need a profile page? ask padyn later
                return {'user' : login_user}

    #if invalid login credentials
    return None
    #ideally it says invalid login and then directs you back to the login page
    #return redirect(request.url)       #back to the login page

@app.route('/register', methods=['POST', 'GET'])
def register():
    #return login page
    if request.method == "GET":
        return render_template('register.html')

    #submitting a new user document
    if request.method == 'POST':
        users = mongo.db.users      #get list of all users
        existing_user = users.find_one({'name' : request.form['username']}) #check to see if theres a user with the same inputted username
        
        #if username doest exist
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        #the username exists already, choose another
        return 'That username already exists!'

    
    return render_template('register.html')

# @app.route('/profile')
# def profile():
#     return render_template('profile.html', name=users.username)

# @app.route('/view/<api_id>')
# def view():
#     return render_template('view.html')

# @app.route('/edit/<api_id>/<user_id>')
# def edit():
#    if session.get("username", None) is not None:
#     return render_template('edit.html')
#   else:
#     return redirect(url_for('login'))

#logout
@app.route('/logout')
def logout():
    #after logging out return user to the page they were on, 
    if not 'edit.html':
        return redirect(request.url)
    #unless on an editing page, the redirect to home page
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)