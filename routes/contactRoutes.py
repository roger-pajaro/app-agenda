from flask import Flask, jsonify, request
from flask import Blueprint

import controllers.contactController as contactController

contact_api = Blueprint('contact_api',__name__)

@contact_api.route('/contactos', methods = ['GET'])
def getContactos():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    campo = parametros['campo']
    orden = parametros['orden']
    contactos = contactController.seleccionar_contactos(id_usuario,campo,orden)
    
    return jsonify(contactos)

@contact_api.route('/contacto', methods = ['GET'])
def getContacto():
    parametros = request.args
    id_contacto = parametros['id_contacto']
    contacto = contactController.seleccionar_contacto(id_contacto)
    
    return jsonify(contacto)


@contact_api.route('/contactoStr', methods = ['GET'])
def getContactoStr():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    value = parametros['value']
    contactos = contactController.busqueda_contactos(id_usuario,value)
    
    return jsonify(contactos)


@contact_api.route('/contacto', methods = ['POST'])
def insertContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    nombre = parametros['nombre']
    apellidos = parametros['apellidos']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']
    
    result = contactController.insertar_contacto(id_usuario,nombre,apellidos,direccion,email,telefono)
    
    
    return jsonify({'result': result})


@contact_api.route('/contacto', methods = ['PUT'])
def updateContacto():
    parametros = request.args
    id = parametros['id']
    nombre = parametros['nombre']
    apellidos = parametros['apellidos']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']
    
    result = contactController.actualizar_contacto(id,nombre,apellidos,direccion,email,telefono)
    
    return jsonify({'result': result})


@contact_api.route('/contacto', methods = ['DELETE'])
def deleteContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    id_contacto = parametros['id_contacto']
    
    result = contactController.eliminar_contacto(id_usuario,id_contacto)
    
    return jsonify({'result': result})