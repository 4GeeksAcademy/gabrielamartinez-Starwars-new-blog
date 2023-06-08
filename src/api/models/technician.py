from api.models.db import db

class Technician(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sur_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    country = db.Column(db.String(40), nullable=False)
    ccaa = db.Column(db.String(40), nullable=False)
    speciality = db.Column(db.String(120), nullable=False)
    num_ropo = db.Column(db.Integer, unique=True)
    user_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    
    
    def __init__(self, name, sur_name, description, phone_number, country, ccaa, speciality, num_ropo, user_id):
        self.name = name
        self.sur_name = sur_name
        self.description = description
        self.phone_number = phone_number
        self.country = country
        self.ccaa = ccaa
        self.speciality = speciality
        self.num_ropo = num_ropo
        self.user_owner = user_id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "sur_name": self.sur_name,
            "description": self.description,
            "phone_number": self.phone_number,
            "country": self.country,
            "ccaa": self.ccaa,
            "speciality": self.speciality,
            "num_ropo": self.num_ropo
        }