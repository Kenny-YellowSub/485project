import os
from datetime import datetime
from extensions import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, mysql

class Photo:
    def __init__(self):
        pass

    @staticmethod
    def upload_photo(image, album_id, caption):
        if Photo.allowed_file(image.filename):
            picid = Photo.get_hash_name(image.filename)
            extension = image.filename.rsplit('.', 1)[1]
            path = str(picid) + '.' + extension

            image.save(os.path.join(UPLOAD_FOLDER, path))
            Photo.insert_photo(picid, extension.upper(), path, str(datetime.now().date()))
            Photo.put_photo_into_album(picid, album_id, caption)

    @staticmethod
    def insert_photo(picid, extension, path, date):
        sql_insert_photo = 'INSERT INTO Photo VALUES(%s, %s, %s, %s)'
        cur = mysql.connection.cursor()
        cur.execute(sql_insert_photo, (str(picid), path, extension, date))
        mysql.connection.commit()

    @staticmethod
    def put_photo_into_album(picid, albumid, caption):
        cur = mysql.connection.cursor()
        sql_connect = 'INSERT INTO Contain(albumid, picid, caption) VALUES(%s, %s, %s)'
        cur.execute(sql_connect, (albumid, picid, caption))
        mysql.connection.commit()

    @staticmethod
    def get_hash_name(filename):
        return abs(hash(filename) + hash(datetime.now()))

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS