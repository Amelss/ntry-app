from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        firstName = request.form.get('first-name')
        signup_password = request.form.get('signup-password')
        repeat_password = request.form.get('repeat-password')

        if len(firstName) < 2: 
            flash('First name must be greater than 2 characters.', category='error')
        elif signup_password != repeat_password:
            flash('Passwords don\'t match!', category='error')
        elif len(signup_password) < 7:
            flash('Your password must be 7 characters or more.', category='error')
        else:
            flash('Your account has been created!', category='success')
        

    return render_template("signup.html")