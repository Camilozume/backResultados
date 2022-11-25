from flask import Blueprint
from flask import request

from controllers.candidatos_controller import CandidatosController

candidatos_blueprints = Blueprint('candidatos_blueprints', __name__)
candidatos_controller = CandidatosController()

@candidatos_blueprints.route("/candidatos/all", methods=['GET'])
def get_all_candidatos():
    response = candidatos_controller.index()
    return response, 200

@candidatos_blueprints.route("/candidatos/<string:id_>", methods=['GET'])
def get_candidatos_by_id(id_):
    response = candidatos_controller.show(id_)
    return response, 200

@candidatos_blueprints.route("/candidatos/insert", methods=['POST'])
def insert_candidatos():
    candidato = request.get_json()
    response = candidatos_controller.create(candidato)
    return response, 201

@candidatos_blueprints.route("/candidatos/update/<string:id_>", methods=['PATCH'])
def update_candidatos(id_):
    candidato = request.get_json()
    response = candidatos_controller.update(id_, candidato)
    return response, 201

@candidatos_blueprints.route("/candidatos/<string:candidatos_id>/partidos/<string:partidos_id>", methods=['PUT'])
def assign_partidos(candidattos_id, partidos_id):
    response = candidatos_controller.partidos_assign(candidattos_id, partidos_id)
    return response, 201

@candidatos_blueprints.route("/candidatos/delete/<string:id_>", methods=['DELETE'])
def delete_candidatos(id_):
    response = candidatos_controller.delete(id_)
    return response, 204
