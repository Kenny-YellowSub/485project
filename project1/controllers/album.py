from flask import *
from project1.models.Album import Album
from project1.models.Photo import Photo
from project1.models.extensions import IMAGE_PATH, ALLOWED_EXTENSIONS

album = Blueprint('album', __name__, template_folder='views')


@album.route('/album/edit', methods=['POST', 'GET'])
def album_edit_route():
    album_id = request.args.get('albumid')
    options = get_album_info(album_id, True)
    if request.method == 'POST':
        image = request.files['img']
        data = request.form
        Photo.upload_photo(image, album_id, data['caption'])
        return redirect(url_for('album.album_edit_route', albumid=album_id))

    return render_template("album.html", **options)


@album.route('/album')
def album_route():
    album_id = request.args.get('albumid')
    options = get_album_info(album_id, False)
    return render_template("album.html", **options)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_album_info(album_id, edit):
    album_info = Album.get_album_info(album_id)
    photos = Album.get_album_photos(album_id)

    options = {
        "edit": edit,
        "title": album_info[0],
        "created": album_info[1],
        "lastupdated": album_info[2],
        "photos": photos,
        "path": IMAGE_PATH
    }

    return options


