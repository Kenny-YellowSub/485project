from flask import *
from project1.models.extensions import *
from project1.models import Album

albums = Blueprint('albums', __name__, template_folder='views')


@albums.route('/albums/edit', methods=['GET', 'POST'])
def albums_edit_route():

    username = request.args.get('username')
    options = get_album_info(username, True)
    if not options:
        return render_template("error.html", error_msg='user not found'), 404

    if request.method == 'POST':
        data = request.form
        print data

        if 'op' in data:
            if data['op'] == 'add':
                create_album(username, data, options)
            elif data['op'] == 'delete':
                delete_album(data, options)

            # refresh album list to reflect update
            options['album_list'] = Album.get_albums_by_username(options['user_info']['username'])

    return render_template("albums.html", **options)


@albums.route('/albums')
def albums_route():
    username = request.args.get('username')
    options = get_album_info(username, False)
    if not options:
        return render_template("error.html", error_msg='user not found'), 404
    return render_template("albums.html", **options)


def get_album_info(username, edit):
    sql_check_user = "SELECT firstname, lastname FROM User WHERE username=%s"
    cur = mysql.connection.cursor()
    cur.execute(sql_check_user, (username,))
    user_info = cur.fetchone()
    if user_info is None:
        return None

    options = {
        "edit": edit,
        "user_info": {'firstname': user_info[0], 'lastname': user_info[1], 'username': username},
        "album_list": Album.get_albums_by_username(username),
        "path": IMAGE_PATH,
        "no_cover": NO_COVER_IMAGE
    }
    return options


def create_album(username, data, options):
    options['operation'] = 'add'
    if 'title' not in data:
        options['success'] = False
        options['message'] = 'Please specify valid title'

    else:
        for album in options["album_list"]:
            if album[1] == data['title']:
                options['success'] = False
                options['message'] = 'Title already exists'
                break
        else:
            Album.insert_album(username, data['title'])
            options['success'] = True
            options['message'] = 'Refresh page to see change'


def delete_album(data, options):
    options['operation'] = 'delete'
    if 'albumid' not in data:
        options['success'] = False
        options['message'] = 'Please specify valid album'

    else:
        albumid = data['albumid']
        Album.delete_album(albumid)

