from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_staff,
    jwt_required,
    staff_required
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')

@staff_required
@staff_views.route('/staff', methods=['POST'])
def create_staff_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_staff(data['username'], data['password'], data['name'], data['role'])
    return redirect(url_for('staff_views.get_staff_page'))