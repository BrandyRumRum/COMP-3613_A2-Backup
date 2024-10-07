from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views
from .user import login_required
from App.controllers import (
    create_course,
    jwt_required,
    course_admin_required,
    view_course_staff
)

course_admin_views = Blueprint('course_admin_views', __name__, template_folder='../templates')

@course_admin_required
@course_admin_views.route('/courses', methods=['POST'])
def create_course_action():
    data = request.form
    flash(f"User {data['name']} created!")
    create_course(data['name'], data['description'])
    return redirect(url_for('course_views.get_course_page'))

@course_admin_views.route('/course_staff/<course_name>', methods=['GET'])
def get_course_staff_view(course_name):
    staff = view_course_staff(course_name)
    return jsonify(staff)