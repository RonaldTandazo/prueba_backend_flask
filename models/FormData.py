from config.database import db

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    option = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<FormData {self.name}>'