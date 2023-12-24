from flask import Blueprint, render_template, request, flash
# defining this file as the blueprint of the application
# defined the blueprint
auth = Blueprint('auth', __name__)


# This route accepts both get and post requests
@auth.route('/login', methods=["POST", "GET"])
def login():
    # when accessed inside a route it will have info about the request sent to access the route; the form attribute
    data = request.form
    return render_template('login.html', text="testing")


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/sign-up', methods=["POST", "GET"])
def sin_up():
    # if a post request
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Your email is to short, needs to be at least 4 characters", category="error")
        elif len(first_name) < 3:
            flash("First name must be longer than 2 characters", category='error')
        elif password1 != password2:
            flash("Password does not match", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long", category='error')
        else:
            # add user to database
            flash("Account created", category='success')

    return render_template('sign_up.html')

