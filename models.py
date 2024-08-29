from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "students"

    id=db.Column(db.Integer, primary_key=True)
    client_name=db.Column(db.String())
    created_at=db.Column(db.DateTime())
    created_by=db.Column(db.String())

    def _init__(self, client_name,created_at,created_by):
        self.client_name =client_name
        self.created_at = created_at
        self.created_by= created_by 

       