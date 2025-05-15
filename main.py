from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
from services.FormService import FormService
from config.settings import PGSQL_URL
from config.database import db
import asyncio 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = PGSQL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

optionsSelect = ["Agent", "Main Corp", "Accounting"]
STORE_FOLDER = "store"

@app.route("/get-options", methods=['GET'])
def get_options():
    #Modifica el codigo para que devuelva las opciones declaradas arriba en optionsSelect
    return jsonify({"data": optionsSelect, "status": 200})

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()

    if not os.path.exists(STORE_FOLDER):
        os.makedirs(STORE_FOLDER)
    
    json_filename = os.path.join(STORE_FOLDER, "formulario_data.json")

    try:
        verify_by_name = FormService.verify_by_name(data['name'])
        if not verify_by_name.get("ok", False):
            raise Exception(verify_by_name.get('message', 'Name already in use'))

        verify_by_email = FormService.verify_by_email(data['email'])
        if not verify_by_email.get("ok", False):
            raise Exception(verify_by_email.get('message', 'Email already in use'))

        if os.path.exists(json_filename) and os.path.getsize(json_filename) > 0:
            with open(json_filename, 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.append(data)

        with open(json_filename, 'w') as f:
            json.dump(existing_data, f, indent=4)

        store = FormService.save_form_data(data)
        if not store.get("ok", False):
            raise Exception(store.get('message', 'Form service error'))

        record = {
            "name": store.get('data').name,
            "email": store.get('data').email,
            "option": store.get('data').option
        }

        return jsonify({"message": store.get('message'), "data": record, "status": 200})
    except Exception as e:
        print(e)
        return jsonify({"message": str(e), "error": str(e), "status": 500})


@app.route('/')
def index():
    return "All Good"      

if __name__ == '__main__':
    app.run(debug=True)