from models.FormData import FormData
from config.database import db

class FormService:
    @staticmethod
    def save_form_data(data):
        try:
            record = FormData(name=data['name'], email=data['email'], option=data['option'])
            db.session.add(record)
            db.session.commit()

            return {"ok": True, "message": "Data Stored in DB", "data": record}
        except Exception as e:
            db.session.rollback()
            return {"ok": False, "error": e, "message": "Internal Error Server"}

    @staticmethod
    def verify_by_name(name):
        try:
            existing_record = FormData.query.filter_by(name=name).first()
            if existing_record:
                return {"ok": False, "error": "Name already in use", "message": "Name already in use"}

            return {"ok": True, "message": "Name not used", "data": existing_record}
        except Exception as e:
            return {"ok": False, "error": str(e), "message": "Internal Error Server"}

    def verify_by_email(email):
        try:
            existing_record = FormData.query.filter_by(email=email).first()
            if existing_record:
                return {"ok": False, "error": "Email already in use", "message": "Email already in use"}

            return {"ok": True, "message": "Email not used", "data": existing_record}
        except Exception as e:
            return {"ok": False, "error": e, "message": "Internal Error Server"}