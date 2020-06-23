from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from flask_api import FlaskAPI
import bcrypt

app = FlaskAPI(__name__)

app.config['MONGO_DBNAME'] = 'staple'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/staple'

#used to encode the session (which in theory is just an encrypted cookie)
app.config['SECRET_KEY'] = secret_key

mongo = PyMongo(app)
users = mongo.db.users    #creates db for users
docs = mongo.db.docs      #creates db for documentations

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
        existing_user = users.find_one({'username' : request.form['username']}) #check to see if theres a user with the same inputted username
        
        #if username doesnt exist, register new user
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insertOne({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('login'))           #redirect them to login after registering
        
        #return None if the username exists already
        return None


# @app.route('/profile')
# def profile():
#     return render_template('profile.html', name=users.username)

# @app.route('/view/<api_id>')
# def view():
    
#     return r

@app.route('/edit/<api_id>/', methods=['POST', 'GET'])
def edit():
    if request.method == "GET":
        if session.get("username", None) is not None:
            return render_template('edit.html')
        else:
            return redirect(url_for('login'))

    if request.method == 'POST':

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

        #if api doest exist alreayd create new api + docs
        if existing_docs is None:
            docs = {
                'api_name' : title, 
                'documentation': request.form['doc']
            }
            docs.insertOne(docs)
            return redirect(url_for('view', {'info' : docs }))           #redirect them to login after registering
        
        #return None if the username exists already
        return None


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