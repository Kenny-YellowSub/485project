from flask import Flask

import controllers
from flask_images import Images
from project1.models.extensions import mysql, UPLOAD_FOLDER, ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = 'monkey'
images = Images(app)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'album_website'
app.config['MYSQL_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql.init_app(app)

app.register_blueprint(controllers.album)
app.register_blueprint(controllers.albums)
app.register_blueprint(controllers.pic)
app.register_blueprint(controllers.main)

# comment this out using a WSGI like gunicorn
# if you don't, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)
