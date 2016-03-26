from flask import *

from project1.models.extensions import mysql
from project1.models.extensions import IMAGE_PATH

pic = Blueprint('pic', __name__, template_folder='views')


@pic.route('/pic')
def pic_route():
    picid = request.args.get('picid')

    sql_get_path = "SELECT path FROM Photo WHERE picid = %s"
    cur = mysql.connection.cursor()
    cur.execute(sql_get_path, (picid,))
    data = cur.fetchone()
    if data is None:
        return render_template('error.html', error_msg='No picture found'), 404

    pic_info = {
        "url": url_for('static', filename=IMAGE_PATH + data[0])
    }

    return render_template("pic.html", **pic_info)
