from extensions import mysql
from datetime import datetime


class Album:
    def __init__(self):
        pass

    @staticmethod
    def get_album_info(album_id):
        # (title, created-date, lastupdate-date)
        cur = mysql.connection.cursor()
        sql_album_info = 'SELECT title, created, lastupdated FROM Album WHERE albumid=%s'
        cur.execute(sql_album_info, (album_id,))
        return cur.fetchone()

    @staticmethod
    def get_album_photos(album_id):
        # (caption, picid, path))
        cur = mysql.connection.cursor()
        sql_get_photos = 'SELECT C.caption, C.picid, P.path FROM Contain C, Photo P WHERE albumid=%s and C.picid=P.picid'
        cur.execute(sql_get_photos, (album_id,))
        return cur.fetchall()

    @staticmethod
    def insert_album(username, title):
        cur = mysql.connection.cursor()
        sql_insert_album = 'INSERT INTO Album (title, created, lastupdated, username, coverid) ' \
                           'VALUES(%s, %s, %s, %s, NULL)'
        cur.execute(sql_insert_album, (title, str(datetime.now().date()),
                                       str(datetime.now().date()), username))
        mysql.connection.commit()

    @staticmethod
    def delete_album(albumid):
        cur = mysql.connection.cursor()
        sql_delete_album = 'DELETE FROM Album WHERE albumid=%s'
        cur.execute(sql_delete_album, (albumid,))
        mysql.connection.commit()

    @staticmethod
    def get_albums_by_username(username):
        cur = mysql.connection.cursor()
        sql_album_list = "SELECT A.albumid, A.title, A.created, A.lastupdated, P.path FROM Album A LEFT JOIN Photo P " \
                     "ON A.coverid = P.picid " \
                     "WHERE A.username=%s"
        cur.execute(sql_album_list, (username,))
        return cur.fetchall()
