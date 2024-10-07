from App.database import db
from App.models import User
from werkzeug.security import check_password_hash, generate_password_hash

class Staff(User):
    name =  db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'staff',}

    def __init__(self, username, password, name, role):
        super().__init__(username, password)
        self.name = name
        self.role = role
        
        