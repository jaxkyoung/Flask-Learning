'''
author: Jack Young
version: 1.0
'''

'''Library imports'''
# file saving and path locating libraries
import os
from werkzeug.utils import secure_filename

# flask library to generate url for function
from flask import url_for

# flask function to load jinja template
from flask import render_template

# for form processing
from flask import request

# for short term screen prompts/messages
from flask import flash

# flask library to redirect to another page
from flask import redirect

# flask libraries to handle user logins and account tracking
from flask_login import login_required, logout_user

from flask import current_app

from flask import current_app, Blueprint, render_template
base = Blueprint('base', __name__)

# error handler for 404 errors
@base.errorhandler(404)
def bar(error):
    # when 404 error, render error template
    return render_template('error.html'), 404


'''Home Page'''
# home page
@base.route('/home')
def goHome():
    return "Home"

# home page, containing default WMGTSS information
@base.route('/')
def home():
    # get first name to show in template
    return render_template('home.html')


