from flask import Blueprint, render_template, request, redirect, url_for, flash

index_bp = Blueprint('/index', __name__)

@index_bp.route('/')
def page_index():
    print ('index page')
    return render_template('index.html')
