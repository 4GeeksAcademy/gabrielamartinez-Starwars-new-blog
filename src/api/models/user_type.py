from api.models.db import db

class User_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship("User", back_populates="user_type")
    description = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return  '%r' % self.description #para las relaciones, en lugar de mostrar el id