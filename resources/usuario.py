from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from models.usuario import Usuario
from sqlalchemy import MetaData, select
from database import engine,db_session
import re

conn = engine.connect()
meta = MetaData(engine, reflect=True)
table = meta.tables['usuarios']
parser = reqparse.RequestParser()

#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('name')
parser.add_argument('nickname')
parser.add_argument('senha')
parser.add_argument('email')

class Usuarios(Resource):

    def get(self, param_usuario):

        print('Parametro do rapaiz: {}'.format(param_usuario))
        email = re.match(r"[^@]+@[^@]+\.[^@]+", param_usuario)
        print('Tratado: {}'.format(email))

        if email is None:
            usuario = Usuario.query.filter_by(id=param_usuario).first()
        else:
            usuario = Usuario.query.filter_by(email=param_usuario).first()

        if usuario is None:
            abort(404, "Usuário {} não está cadastrado".format(usuario))

        retorno = {
            'id':usuario.id,
            'name':usuario.name,
            'nickname': usuario.nickname,
            'email':usuario.email,
            'senha':usuario.senha,
        }
        return jsonify(retorno)


    def post(self):
        response = parser.parse_args()
        usuario_cadastrado = Usuario.query.filter_by(name=response['name']).first()
        print('Usuario cad: {}'.format(usuario_cadastrado))
        if usuario_cadastrado != None:
            return 200
        usuario = Usuario(response['name'], response['nickname'], response['senha'], response['email'])
        if usuario != '':
            print('Usuario cadastrado')
            db_session.add(usuario)
            db_session.commit()
        return 201


    def put(self, usuario_id):
        response = parser.parse_args()
        usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()

        if response.get('name'):
            usuario_selecionado.name = response['name']

        if response.get('nickname'):
            usuario_selecionado.description = response['nickname']

        if response.get('email'):
            usuario_selecionado.host = response['email']

        if response.get('senha'):
            usuario_selecionado.port = response['senha']

        if response:
            db_session.commit()

        return jsonify({'Usuário Atualizado':usuario_selecionado.id})

    def delete(self, usuario_id):
        usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()
        if usuario_selecionado is None:
            abort(404, "Usuário {} não está cadastrado".format(usuario_id))
        db_session.delete(usuario_selecionado)
        db_session.commit()
        return jsonify({'Usuário deletado':usuario_selecionado.name})
