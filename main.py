import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidatos_blueprints import candidatos_blueprints
from blueprints.partidos_blueprints import partidos_blueprints
from blueprints.mesas_blueprints import mesas_blueprints
from blueprints.votos_blueprints import votos_blueprints

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(candidatos_blueprints)
app.register_blueprint(partidos_blueprints)
app.register_blueprint(mesas_blueprints)
app.register_blueprint(votos_blueprints)

#ASÍ LE DIGO QUE HAY UN ENDPOINT CON/
@app.route("/", methods=['GET'])
def home():
    response = {"MESSAGE": "Welcome to the votes microservices for Colombia"}
    return jsonify(response)



def load_file_config():
    with open("config.json", 'r') as config_file:
        data = json.load(config_file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host= data_config.get('url-backend'), port= data_config.get('port'))

