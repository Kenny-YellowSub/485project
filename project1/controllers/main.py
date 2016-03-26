from flask import *

from project1.models.extensions import mysql

main = Blueprint('main', __name__, template_folder='views')


@main.route('/')
def main_route():

        query = "SELECT firstname, lastname, username FROM User"
        cur = mysql.connection.cursor()
        cur.execute(query)
        user_list = []

        for user in cur.fetchall():
            user_list.append((user[0] + ' ' + user[1], url_for('albums.albums_route', username=user[2])))

        return render_template("index.html", user=user_list)
