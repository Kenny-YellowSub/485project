from extensions import mysql


class Users:
    def __init__(self):
        pass

    @staticmethod
    def get_user_info(username):
        sql_get_user_info = "SELECT username, firstname, lastname, password, email, avatar FROM User WHERE username=%s"
        cursor = mysql.connection.cursor()
        cursor.execute(sql_get_user_info, (username,))
        result = cursor.fetchone()
        if result is None:
            return None
        user_info = {
            'username': result[0],
            'firstname': result[1],
            'lastname': result[2],
            'password': result[3],
            'email': result[4],
            'avatar_id': result[5]
        }

        return user_info

