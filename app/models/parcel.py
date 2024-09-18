from app.utils.db_setup import db
from datetime import datetime

class Parcel(db.Model):
    __tablename__ = 'parcels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reference = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), nullable=True)
    date_enregistrement = db.Column(db.DateTime, default=datetime.utcnow)
