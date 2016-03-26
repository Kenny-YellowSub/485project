from flask.ext.mysqldb import MySQL

mysql = MySQL()

IMAGE_PATH = 'images/'
UPLOAD_FOLDER = 'static/' + IMAGE_PATH
NO_COVER_IMAGE = 'no-cover-image.jpg'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])