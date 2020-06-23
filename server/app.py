from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'staple'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/staple'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if request.method == "POST":
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('profile'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

# @app.route('/profile')
# def profile():
#     return render_template('profile.html', name=users.username)

# @app.route('/view/api_id')
# def view():
#     return render_template('view.html')

# @app.route('/edit/api_id')
# def edit():
#     return render_template('edit.html')

@app.route('/logout')
def logout():
    if not 'edit.html':
        return redirect(request.url)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)