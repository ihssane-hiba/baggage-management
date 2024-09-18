from app.models.parcel import Parcel
from app.utils.db_setup import db

class ParcelService:
    @staticmethod
    def create_parcel(reference, description, status):
        new_parcel = Parcel(reference=reference, description=description, status=status)
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
        db.session.delete(parcel)
        db.session.commit()


    @staticmethod
    def report_lost_item(reference):
        parcel = Parcel.query.filter_by(reference=reference).first()
        if parcel:
            parcel.status = 'lost'
            db.session.commit()
            return f"Le colis avec la référence {reference} a été déclaré perdu."
        else:
            return f"Aucun colis trouvé avec la référence {reference}."    


   
    


