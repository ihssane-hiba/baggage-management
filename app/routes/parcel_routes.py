from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.parcel_service import ParcelService

parcel_routes = Blueprint('parcel', __name__)

@parcel_routes.route('/parcels')
def list_parcels():
    parcels = ParcelService.get_all_parcels()
    return render_template('list_parcels.html', parcels=parcels)
