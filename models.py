from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    deadline = db.Column(db.String(20), nullable=True)
    completed = db.Column(db.Boolean, default=False)
