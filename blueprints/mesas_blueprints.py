from flask import Blueprint
from flask import request

from controllers.mesas_controller import MesasController

mesas_blueprints = Blueprint('mesas_blueprints', __name__)
mesas_controller = MesasController()

@mesas_blueprints.route("/mesas/all", methods=['GET'])
def get_all_mesas():
    response = mesas_controller.index()
    return response, 200

@mesas_blueprints.route("/mesas/<string:id_>", methods=['GET'])
def get_mesas_by_id(id_):
    response = mesas_controller.show(id_)
    return response, 200

@mesas_blueprints.route("/mesas/insert", methods=['POST'])
def insert_mesas():
    mesa = request.get_json()
    response = mesas_controller.create(mesa)
    return response, 201

@mesas_blueprints.route("/mesas/update/<string:id_>", methods=['PATCH'])
def update_mesas(id_):
    mesa = request.get_json()
    response = mesas_controller.update(id_, mesa)
    return response, 201

@mesas_blueprints.route("/mesas/delete/<string:id_>", methods=['DELETE'])
def delete_mesas(id_):
    response = mesas_controller.delete(id_)
    return response, 204
