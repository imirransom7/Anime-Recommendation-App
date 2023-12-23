from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# Creating an instance of a Flask web app
app = Flask(__name__)
# All session data is encrytped on the server, secret key is needed to
# decrypt and encrpyt the data
app.secret_key = 'hello'
# initiating an object database
app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite://users.sqlite3'
# Turns off all tracking modifications to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# adds max time for session to last
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)
    gender = db.Column(db.String(20))

    # take the variables that are needed to make new object
    def __init__(self, name, email, password, gender):
        self.name = name
        self.email = email
        self.password = password
        self.gender = gender


# creating the home page
@app.route("/") # adding decorator app.route and define the path to get to this function
def home():
    return render_template('index.html', content=["Anime", 'Most Popular', "Highest Rated", "Recommendation"])


# This need to use both GET and PUSH
@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == "POST":
        # define the session as a permanent session
        session.permanent = True
        user = request.form['nm']
        # Making a dictionary key, storing it in session, session is imported at the top;
        # then set it equal to a value
        session['user'] = user
        flash('Login Successful!')
        return redirect(url_for('user'))
    else:
        # redirect user to user if logged in
        if "user" in session:
            flash('Already Logged In!')
            return redirect(url_for('user'))
        return render_template('login.html')


@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    # Checking if user exist
    if 'user' in session:
        # get the user, valid because we just checked user ^^^
        user = session['user']
        # Checking current method, if post or get
        if request.method == "POST":
            # grabbing the email form the email field
            email = request.form['email']
            # storing the email in a session
            session['email'] = email
            flash("Email was saved!")
        else:
            # if the request.method is a get request
            if 'email' in session:
                email = session['email']
        # if user is logged in it will render the user template from user.html
        return render_template("user.html", email=email)
    # if session does not exist, redirect to the login page
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))


@app.route('/logout')
def logout():
    flash(f'You have been logged out', 'info')
    # removing user information from the session
    session.pop('user', None)
    session.pop('email', None)
    # redirect to the login page; user logged out
    return redirect(url_for('login'))


# This runs the website
if __name__ == '__main__':
    # Create the database if it doesn't exist when we run the program
    db.create_all()
    app.run(debug=True)

