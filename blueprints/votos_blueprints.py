from flask import Blueprint
from flask import request

from controllers.votos_controller import VotosController

votos_blueprints = Blueprint('votos_blueprints', __name__)
votos_controller = VotosController()

@votos_blueprints.route("/votos/all", methods=['GET'])
def get_all_votos():
    response = votos_controller.index()
    return response, 200

@votos_blueprints.route("/votos/<string:id_>", methods=['GET'])
def get_votos_by_id(id_):
    response = votos_controller.show(id_)
    return response, 200

@votos_blueprints.route("/votos/insert/candidatos/<string:candidatos_id>/mesas/<string:mesas_id>", methods=['POST'])
def insert_votos(candidatos_id, mesas_id):
    voto = request.get_json()
    response = votos_controller.create(voto, candidatos_id, mesas_id)
    return response, 201

@votos_blueprints.route("/votos/update/<string:id_>", methods=['PATCH'])
def update_votos(id_):
    voto = request.get_json()
    response = votos_controller.update(id_, voto)
    return response, 201

@votos_blueprints.route("/votos/delete/<string:id_>", methods=['DELETE'])
def delete_votos(id_):
    response = votos_controller.delete(id_)
    return response, 204
