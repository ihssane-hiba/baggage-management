from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.parcel_service import ParcelService

parcel_bp = Blueprint('parcel', __name__)

@parcel_bp.route('/parcels')
def list_parcels():
    print('List parcels in parcel service')
    parcels = ParcelService.get_all_parcels()
    return render_template('list_parcels.html', parcels=parcels)

@parcel_bp.route('/edit_parcel/<int:parcel_id>')
def edit_parcel(parcel_id):
    print(f'Edit parcel with ID {parcel_id} in parcel service')
    return render_template('edit_parcel.html', parcel_id=parcel_id)

@parcel_bp.route('/delete_parcel', methods=['POST'])
def delete_parcel():
    parcel_id = request.form['parcel_id']
    print(f'Delete parcel with ID {parcel_id} in parcel service')
    ParcelService.delete_parcel(parcel_id)
    parcels = ParcelService.get_all_parcels()
    return render_template('list_parcels.html', parcels=parcels)

@parcel_bp.route('/new_parcel')
def new_parcel():
    print('Create new parcel in parcel service')
    return render_template('new_parcel.html')

@parcel_bp.route('/create', methods=['POST'])
def create_parcel():

    reference = request.form['reference'],
    description = request.form['description'],
    status = request.form['status'],
    
    new_parcel = ParcelService.create_parcel(reference, description, status)

    flash('Parcel created successfully!')
    return list_parcels()