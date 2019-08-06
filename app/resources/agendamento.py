from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.agendamento import ModelAgendamento
from ..database import db, engine

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('horario_inicio')
parser.add_argument('horario_fim')
parser.add_argument('data')
parser.add_argument('observacao')
parser.add_argument('laboratorio_id')
parser.add_argument('usuario_id', required=True)


class Agendamento(Resource):
    def get(self, id=None):
        agendamentos = []
        where = ''
        if id != None:
            where = ' where laboratorio_id = {}'.format(id);

        result = engine.execute('select * from agendamentos {}'.format(where))

        for _row in result:
            print('Result: {}'.format(_row))
            agendamento = {
                'id': _row['id'],
                'periodo_inicio': _row['periodo_inicio'],
                'periodo_fim': _row['periodo_fim'],
                'usuario_id': _row['usuario_id'],
                'observacao': _row['observacao']
            }
            print('Objeto: {}'.format(agendamento))
            agendamentos.append(agendamento)
        print('Agend: {} {}'.format(agendamentos, len(agendamentos)))
        if len(agendamentos) == 0:
            print('Nenhum agendamento')
            return 200

        return jsonify(agendamentos)

    def put(self, id):

        response = parser.parse_args()
        print('Response: {}'.format(response))
        selecionado = ModelAgendamento.query.filter_by(id=id).first()

        if response.get('observacao'):
            selecionado.observacao = response['observacao']

        if response.get('periodo_inicio'):
            selecionado.periodo_inicio = response['periodo_inicio']

        if response.get('periodo_fim'):
            selecionado.periodo_fim = response['periodo_fim']

        # if response.get('port'):
        #     selecionado.port = response['port']

        print('Agendamento: {}'.format(response))
        if response:
            print('Alteração realizada com sucesso!!!')
            db.session.commit()
            return 201

        return 200
        # return jsonify({'Agendamento Atualizado':selecionado.id})

    def delete(self, agendamento_id):
        lab_selecionado = Laboratorio.query.filter_by(id=agendamento_id).first()
        if lab_selecionado is None:
            abort(404, "Laboratório {} não está cadastrado".format(agendamento_id))
        db.session.delete(lab_selecionado)
        db.session.commit()
        return jsonify({'Laboratório deletado':lab_selecionado.name})

    def post(self):
        args = parser.parse_args()
        response = args
        print('Resposta obtida: {}'.format(response))
        where = ' laboratorio_id = {0} and \'{1}\' >= agendamentos.periodo_inicio and \'{1}\' <= agendamentos.periodo_fim'.format(response['laboratorio_id'], response['data']+' '+response['horario_inicio'])
        print('Where: {}'.format(where))
        result = engine.execute('select count(id) as contagendamentos from agendamentos where {}'.format(where))

        for _row in result:
            if _row['contagendamentos'] > 0:
                print('Já existe agendamento no horário solicitado!')
                return 200

        agendamento = ModelAgendamento(response['observacao'],
        response['data']+' '+response['horario_inicio'], response['data']+' '+response['horario_fim'],
        response['laboratorio_id'], response['usuario_id'])
        print('Agendamento inserido: {}'.format(agendamento))
        if agendamento != '':
            db.session.add(agendamento)
            db.session.commit()
            print('Agendamento realizado')
        return 201
