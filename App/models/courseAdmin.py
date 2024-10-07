from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models import User

class CourseAdmin(User):
     __mapper_args__ = {'polymorphic_identity': 'courseAdmin',}

     def __init__(self, username, password, name):
        super().__init__(username, password, name)
