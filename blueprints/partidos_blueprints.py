from flask import Blueprint
from flask import request

from controllers.partidos_controller import PartidosController

partidos_blueprints = Blueprint('partidos_blueprints', __name__)
partidos_controller = PartidosController()

@partidos_blueprints.route("/partidos/all", methods=['GET'])
def get_all_partidos():
    response = partidos_controller.index()
    return response, 200

@partidos_blueprints.route("/partidos/<string:id_>", methods=['GET'])
def get_partidos_by_id(id_):
    response = partidos_controller.show(id_)
    return response, 200

@partidos_blueprints.route("/partidos/insert", methods=['POST'])
def insert_partidos():
    partido = request.get_json()
    response = partidos_controller.create(partido)
    return response, 201

@partidos_blueprints.route("/partidos/update/<string:id_>", methods=['PATCH'])
def update_partidos(id_):
    partido = request.get_json()
    response = partidos_controller.update(id_, partido)
    return response, 201

@partidos_blueprints.route("/partidos/delete/<string:id_>", methods=['DELETE'])
def delete_partidos(id_):
    response = partidos_controller.delete(id_)
    return response, 204
