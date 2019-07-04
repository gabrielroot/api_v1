from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from models.laboratorio import Laboratorio
from sqlalchemy import MetaData, select
from database import engine,db_session

conn = engine.connect()
meta = MetaData(engine, reflect=True)
table = meta.tables['laboratorios']

parser = reqparse.RequestParser()
parser.add_argument('lab')

class Labs(Resource):
    def get(self, lab_id=None):
        print('Id do moço: ', lab_id);

        if lab_id is None:
            labs = []
            res = conn.execute('select * from laboratorios')
            for _row in res:
                labs.append(dict(_row))
            return jsonify(labs);
        else:
            laboratorio = Laboratorio.query.filter_by(id=lab_id).first()

            if laboratorio is None:
                abort(404, "Laboratório {} não está cadastrado".format(lab_id))

            retorno = {
                'id':laboratorio.id,
                'name':laboratorio.name,
                'description': laboratorio.description,
                'host':laboratorio.host,
                'port':laboratorio.port,
                'tempo': laboratorio.tempo_experimento
            }
            return jsonify(retorno)

    def put(self, lab_id):
        args = parser.parse_args()
        response = request.form
        print('Response: {}'.format(response['name']))
        selecionado = Laboratorio.query.filter_by(id=lab_id).first()

        if response.get('name'):
            selecionado.name = response['name']

        if response.get('description'):
            selecionado.description = response['description']

        if response.get('host'):
            selecionado.host = response['host']

        if response.get('port'):
            selecionado.port = response['port']

        if response:
            db_session.commit()

        return jsonify({'lab Atualizado':selecionado.id})

    def delete(self, lab_id):
        lab_selecionado = Laboratorio.query.filter_by(id=lab_id).first()
        if lab_selecionado is None:
            abort(404, "Laboratório {} não está cadastrado".format(lab_id))
        db_session.delete(lab_selecionado)
        db_session.commit()
        return jsonify({'Laboratório deletado':lab_selecionado.name})

    def post(self):
        args = parser.parse_args()
        response = request.form
        laboratorio_cadastrado = Laboratorio.query.filter_by(name=response['name']).first()
        if laboratorio_cadastrado != None:
            return jsonify({'Laboratório já cadastrado':response['name']})
        laboratorio = Laboratorio(response['name'], response['description'],response['host'], response['port'])
        if laboratorio != '':
            db_session.add(laboratorio)
            db_session.commit()
        return jsonify({'Laboratorio':response['name']})
