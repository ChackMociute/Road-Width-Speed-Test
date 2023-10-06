from app import db
import pandas as pd

IMAGES_PER_PARTICIPANT = 100


class Participant(db.Model):
    def __init__(self, **kwargs):
        kwargs['images'] = [Response(filename=f)
                            for f in pd.read_csv("../dataset/data.csv", index_col=0).
                            sample(IMAGES_PER_PARTICIPANT).filename.values]
        super().__init__(**kwargs)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    images = db.relationship('Response', backref='participant', lazy=True)


class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(8), nullable=False)
    response = db.Column(db.Float)
    response_time = db.Column(db.Float)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)