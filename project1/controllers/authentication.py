from flask import Blueprint, request, render_template, session, redirect, url_for
from project1.models.User import Users

authentication = Blueprint('authentication', __name__, template_folder='templates')


@authentication.route('/login', methods=['GET', 'POST'])
def login_route():
    options = {
        'login_fail': False
    }

    if request.method == 'POST':
        next_url = request.args.get('next_url')
        login_data = request.form
        user_info = Users.get_user_info(login_data['username'])

        if user_info is not None and login_data['password'] == user_info['password']:
            session['username'] = login_data['username']
            session.permanent = True
            if next_url is not None:
                return redirect(next_url)
            else:
                return redirect(url_for('main.main_route'))
        else:
            options['login_fail'] = True

    return render_template('signin.html', **options)

