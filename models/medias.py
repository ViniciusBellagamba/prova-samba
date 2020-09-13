from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime, date
from utils.endpoints_exceptions import endpoint_ex, body_validation

db_user = os.environ.get("DB_USER", "").strip()
db_pass = os.environ.get("DB_PASS", "").strip()
db_host = os.environ.get("DB_HOST", "").strip()
database = os.environ.get("DATABASE", "").strip()

conn = 'mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{port}/{database}'.format(
            db_user=db_user,
            db_pass=db_pass,
            db_host=db_host,
            port=3306,
            database=database
        )

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(512), unique=False, nullable=False)
    url = db.Column(db.String(512), unique=False, nullable=False)
    duration = db.Column(db.Float, unique=False, nullable=False)
    deleted = db.Column(db.Boolean, unique=False, nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.now())


def to_dict(self):
    dic = {
        'id': self.id,
        'name': self.name,
        'url': self.url,
        'duration': self.duration,
        'deleted': self.deleted,
        'upload_data': self.upload_date.isoformat()
    }
    return dic


def create_video_table():
    db.create_all()


@app.route('/medias', methods=['POST', 'OPTIONS'])
def create():
    body = request.json
    body_validation(body)
    video = Video(name=body['name'], url=body['url'], duration=body['duration'], deleted=body['deleted'])
    db.session.add(video)
    db.session.commit()
    return jsonify(to_dict(video)), 200


@app.route('/medias', methods=['GET', 'OPTIONS'])
def get_list():
    result = []
    videos = Video.query.all()
    if videos is not None:
        for video in videos:
            result.append(to_dict(video))
    return jsonify(result), 200


@app.route('/medias/<video_id>', methods=['GET', 'OPTIONS'])
def get(video_id):
    video = Video.query.filter_by(id=video_id).first()
    if video is not None:
        return jsonify(to_dict(video)), 200
    raise endpoint_ex(404, "VIDEO_NOT_FOUND")


@app.route('/medias/<video_id>', methods=['DELETE', 'OPTIONS'])
def delete(video_id):
    video = Video.query.filter_by(id=video_id).first()
    if video is not None:
        db.session.delete(video)
        db.session.commit()
        return jsonify(to_dict(video)), 200
    raise endpoint_ex(404, "VIDEO_NOT_FOUND")


@app.route('/medias/<video_id>', methods=['PUT', 'OPTIONS'])
def update(video_id):
    body = request.json
    body_validation(body)
    video = Video.query.filter_by(id=video_id).first()
    if video is not None:
        video.name = body['name']
        video.url = body['url']
        video.duration = body['duration']
        video.deleted = body['deleted']
        db.session.commit()
        return jsonify(to_dict(video)), 200
    raise endpoint_ex(404, "VIDEO_NOT_FOUND")


@app.route('/')
def hello():
    return "Prova para admissão de desenvolvedor júnior da samba-tech realizada por Vinicius Bellagamba."