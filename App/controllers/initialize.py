from .staff import create_staff
from .user import create_course_admin
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_staff('bob', 'bobpass', 'Bob', 'Lecturer')
    create_course_admin('chad', 'pass')
