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
        result = cur.fetchone()
        cur.close()
        return result

    @staticmethod
    def get_album_photos(album_id):
        """
        Get all photo information in an album.
        :param album_id: Id of the album.
        :return: A tuple of tuples consist of photo info.
          Each entry will be in the form of (photo_id, cation, file path)
        """
        # (caption, picid, path))
        cur = mysql.connection.cursor()
        sql_get_photos = 'SELECT C.caption, C.picid, P.path FROM Contain C, Photo P WHERE albumid=%s and C.picid=P.picid'
        cur.execute(sql_get_photos, (album_id,))
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def insert_album(username, title):
        """ Insert an album that belongs to <username> with album name as <title>. """
        cur = mysql.connection.cursor()
        sql_insert_album = 'INSERT INTO Album (title, created, lastupdated, username, coverid) ' \
                           'VALUES(%s, %s, %s, %s, NULL)'
        cur.execute(sql_insert_album, (title, str(datetime.now().date()),
                                       str(datetime.now().date()), username))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete_album(albumid):
        """
        Delete an album identified by <albumid>.
        :param albumid: The albumid of the album to delete
        :return: None
        """
        cur = mysql.connection.cursor()
        sql_delete_album = 'DELETE FROM Album WHERE albumid=%s'
        cur.execute(sql_delete_album, (albumid,))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def get_albums_by_username(username):
        """
        Get all album information by <username>. Note: cover photo path is relative path.
        :param username:
        :return: A tuple of tuples consist of album information of a specific user identified by username.
          Each entry will be in the form of (albumid, title, create-time, update-time, cover photo path).
        """
        cur = mysql.connection.cursor()
        sql_album_list = "SELECT A.albumid, A.title, A.created, A.lastupdated, P.path FROM Album A LEFT JOIN Photo P " \
                     "ON A.coverid = P.picid " \
                     "WHERE A.username=%s"
        cur.execute(sql_album_list, (username,))
        result = cur.fetchall()
        cur.close()
        return result
