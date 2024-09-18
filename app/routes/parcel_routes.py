from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.parcel_service import ParcelService

parcel_bp = Blueprint('parcel', __name__)

# Liste des colis
@parcel_bp.route('/parcels')
def list_parcels():
    print('Listing all parcels')
    parcels = ParcelService.get_all_parcels()
    return render_template('list_parcels.html', parcels=parcels)

# Page d'édition d'un colis
@parcel_bp.route('/edit_parcel/<int:parcel_id>')
def edit_parcel(parcel_id):
    print(f'Editing parcel with ID {parcel_id}')
    # Récupérer les détails du colis pour les afficher sur la page d'édition (vous devrez implémenter la méthode get_parcel_by_id)
    parcel = ParcelService.get_parcel_by_id(parcel_id)
    return render_template('edit_parcel.html', parcel=parcel)

# Suppression d'un colis
@parcel_bp.route('/delete_parcel', methods=['POST'])
def delete_parcel():
    parcel_id = request.form['parcel_id']
    print(f'Deleting parcel with ID {parcel_id}')
    ParcelService.delete_parcel(parcel_id)
    return redirect(url_for('parcel.list_parcels'))

# Page de création d'un nouveau colis
@parcel_bp.route('/new_parcel')
def new_parcel():
    print('Creating new parcel')
    return render_template('new_parcel.html')

# Création d'un nouveau colis
@parcel_bp.route('/create', methods=['POST'])
def create_parcel():
    reference = request.form['reference']
    description = request.form.get('description', '')
    status = request.form['status']
    date_enregistrement = request.form['date_enregistrement']
    nom = request.form['nom']
    prenom = request.form['prenom']
    type_colis = request.form['type_colis']
    date_envoi = request.form['date_envoi']
    destination = request.form['destination']
    societe_transport = request.form['societe_transport']
    email = request.form['email']

    # Création du colis avec les nouvelles données
    ParcelService.create_parcel(
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

    flash('Parcel created successfully!')
<<<<<<< HEAD
    return list_parcels()

@parcel_bp.route('/report_lost')
def report_lost():
    print('Report lost item form')
    return render_template('report_lost.html')

@parcel_bp.route('/submit_lost', methods=['POST'])
def submit_lost():
    reference = request.form['reference']
    
    
    # Assuming there's a method in ParcelService to handle lost items
    ParcelService.report_lost_item(reference )
    
    flash('Lost item reported successfully!')
    return render_template('report_lost.html')

@parcel_bp.route('/update_parcel/<int:parcel_id>', methods=['POST'])
def update_parcel(parcel_id):
    reference = request.form['reference']
    status = request.form['status']
    
    # Update parcel details in the ParcelService
    ParcelService.update_parcel(parcel_id, reference,  status)
    
    flash('Parcel updated successfully!')
    return render_template('new_parcel.html')
=======
    return redirect(url_for('parcel.list_parcels'))
>>>>>>> 13b85523c13be008ba3b7d2c701dfd01131f5efd
