from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
db = SQLAlchemy(app)
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    topic_name = db.Column(db.String(80))
    cards = db.relationship('Card', backref = 'topics', lazy = True)