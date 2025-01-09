from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa CORS

from routes.userRoutes import user_api
from routes.contactRoutes import contact_api

app = Flask(__name__)


CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

app.register_blueprint(user_api, url_prefix='/api')
app.register_blueprint(contact_api, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

    
