from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
db = SQLAlchemy(app)
class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    front = db.Column(db.String(80))
    back = db.Column(db.String())
    known = db.Column(db.Integer, nullable = False)
    topic_id = db.Column(db.Intger, db.ForeignKey('topics.id'))
    