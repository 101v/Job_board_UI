from .. import db
from sqlalchemy.sql import func
from datetime import datetime


class JobTweet(db.Model):
    __tablename__ = "lv_jobtweet"
    id = db.Column(db.String(200), primary_key=True)
    value = db.Column(db.String(2000))
    text = db.Column(db.String(2000))
    author_id = db.Column(db.String(2000))
    createddatetimeutc = db.Column(db.DateTime, default=datetime.utcnow)
    confidence = db.Column(db.Integer)
    keywords = db.Column(db.String(2000))
