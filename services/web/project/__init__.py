import os
from flask import Flask, jsonify, send_from_directory, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_flatpages import FlatPages
import pdb

db = SQLAlchemy()
app = Flask(__name__)
app.debug = True
app.config.from_object("project.config.Config")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['FLATPAGES_ROOT'] = 'content/blog/'
app.config['FLATPAGES_EXTENSION'] = '.md'
db.init_app(app)
flatpages = FlatPages(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return """
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """

@app.route('/blog/<path:path>')
def page(path):
    post = flatpages.get_or_404(f"{path}/index")
    return render_template('page.html', page=post)