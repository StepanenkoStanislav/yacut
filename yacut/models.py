from datetime import datetime

from settings import ORIGINAL_MAX_LENGTH, CUSTOM_ID_MAX_LENGTH
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_MAX_LENGTH))
    short = db.Column(db.String(CUSTOM_ID_MAX_LENGTH), unique=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())


db.create_all()
