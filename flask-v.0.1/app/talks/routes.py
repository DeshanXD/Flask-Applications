from flask import render_template
from . import talks

# We use talks instead of app you see!
@talks.route('/')
def index():
    return render_template('talks/index.html')

@talks.route('/user/<usrname>')
def user(usrname):
    return render_template('talks/user.html', username=usrname)


