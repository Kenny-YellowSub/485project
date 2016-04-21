from flask import session, render_template, Blueprint

from project1.models.extensions import mysql
from project1.models.User import Users

main = Blueprint('main', __name__, template_folder='views')


@main.route('/')
def main_route():
    options = {
        'user_info': None
    }
    if 'username' in session:
        options['user_info'] = Users.get_user_info(session['username'])

    return render_template("index.html", **options)

