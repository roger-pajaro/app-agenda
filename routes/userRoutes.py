from flask import Flask, jsonify, request
from flask import Blueprint
from models import Usuario
import controllers.userController as userController

from db import conectar


user_api = Blueprint('user_api', __name__)

@user_api.route("/usuario",methods =['GET'])
def getUsuario():
    parametros = request.args
    email = parametros['email']
    password = parametros['password']
    result = userController.seleccionarUsuario(email,password)
    return jsonify({'result': result})
    