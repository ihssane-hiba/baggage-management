from app.utils.db_setup import db
from datetime import datetime

class Parcel(db.Model):
    __tablename__ = 'parcels'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reference = db.Column(db.String(50), unique=True, nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    type_colis = db.Column(db.String(50), nullable=False)
    date_envoi = db.Column(db.Date, nullable=False)
    destination = db.Column(db.String(150), nullable=False)
    societe_transport = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('Annulée', 'Envoyée', 'Rapportée', 'Retardée', 'En Attente', 'lost'), nullable=False)
    date_enregistrement = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Parcel(id={self.id}, reference='{self.reference}')>"
