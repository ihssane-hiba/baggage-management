from app.models.parcel import Parcel
from app.utils.db_setup import db

class ParcelService:
    @staticmethod
    def create_parcel(reference, description, status, date_enregistrement, nom, prenom, type_colis, date_envoi, destination, societe_transport, email):
        new_parcel = Parcel(
            reference=reference,
            description=description,
            status=status,
            date_enregistrement=date_enregistrement,
            nom=nom,
            prenom=prenom,
            type_colis=type_colis,
            date_envoi=date_envoi,
            destination=destination,
            societe_transport=societe_transport,
            email=email
        )
        db.session.add(new_parcel)
        db.session.commit()

    @staticmethod
    def get_all_parcels():
        return Parcel.query.all()

    @staticmethod
    def update_parcel(parcel_id, status):
        parcel = Parcel.query.get(parcel_id)
        if parcel:
            parcel.status = status
            db.session.commit()

    @staticmethod
    def delete_parcel(parcel_id):
        parcel = Parcel.query.get(parcel_id)
        if parcel:
            db.session.delete(parcel)
            db.session.commit()
