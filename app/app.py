from os import path
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from config import Config
# from .models.papel import Papel
from .models.usuario import Usuario
from .resources.labs import Labs
from .resources.usuario import Usuarios
from .resources.listaUsuarios import ListaUsuarios
from .resources.agendamentos import Agendamentos
from .resources.agendamento import Agendamento
from .resources.equipamento import Equipamento
from .resources.experimento import Experimento
from .resources.agendamentoByUsuario import AgendamentoByUsuario
from .resources.agendamentoByLaboratorio import AgendamentoByLaboratorio
from .resources.experimentoByUsuario import ExperimentoByUsuario
from .resources.ConsultaAgendamento import ConsultaAgendamento
from .resources.laboratoriosSolicitacoes import LaboratoriosSolicitacoes
from .resources.instituicao import Instituicao
from .resources.papel import Papel
from .resources.papelById import PapelById
from .resources.convenios import Convenios
from .resources.convenio import Convenio
from .resources.login import Login
from .database import db, db_session
from flask_cors import CORS
def create_app():
    app = Flask("app", instance_relative_config=True)
    CORS(app)
    user_datastore = SQLAlchemyUserDatastore(db_session, Usuario, Papel)
    security = Security(app, user_datastore)

    app.config.from_object(Config)
    api = Api(app)
    api.add_resource(Labs, '/labs/', endpoint='listlabs')
    api.add_resource(Labs, '/labs/<int:lab_id>', endpoint='lab')
    api.add_resource(Usuarios, '/usuario', endpoint="usuario")
    api.add_resource(Usuarios, '/usuario/<string:param_usuario>', endpoint="getUsuario")
    api.add_resource(PapelById, '/usuarios/papeis/<int:id>', endpoint="listpapel")
    api.add_resource(Papel, '/usuarios/papeis/', endpoint="listpapeis")
    api.add_resource(ListaUsuarios, '/usuarios', endpoint="lista_usuario")
    api.add_resource(Experimento, '/experimento', endpoint="experimento")
    api.add_resource(Experimento, '/experimento/<int:experimento_id>', endpoint="experimentoIndividual")
    api.add_resource(ExperimentoByUsuario, '/experimentos/usuario/<int:usuario_id>', endpoint="experimentoByUsuario")
    api.add_resource(Agendamentos, '/agendamentos', endpoint="listaAgendamentos")
    api.add_resource(Agendamento, '/agendamento/', endpoint="setAgendamento")
    api.add_resource(Agendamento, '/agendamento', endpoint="setReserva")
    api.add_resource(Agendamento, '/agendamento/<int:id>', endpoint="getAgendamento")
    api.add_resource(AgendamentoByUsuario, '/agendamento/usuario/<int:usuario_id>', endpoint="getAgendamentoUsuario")
    api.add_resource(AgendamentoByLaboratorio, '/agendamento/laboratorio/<int:lab_id>', endpoint="getAgendamentoLaboratorio")
    api.add_resource(ConsultaAgendamento, '/agendamento/valida_horario/<int:usuario_id>', endpoint="getValidaHorario")
    api.add_resource(Instituicao, '/instituicoes', endpoint="setInstituicao")
    api.add_resource(Instituicao, '/instituicoes/', endpoint="getInstituicoes")
    api.add_resource(Instituicao, '/instituicao/<int:instituicao_id>', endpoint="getInstituicao")
    api.add_resource(Convenios, '/convenios/', endpoint="getConvenios")
    api.add_resource(Convenios, '/convenio/', endpoint="setConvenios")
    api.add_resource(Convenio, '/convenio/<int:convenio_id>', endpoint="setConvenio")
    api.add_resource(LaboratoriosSolicitacoes, '/laboratorios/solicitacoes/', endpoint="solicitacoesLaboratorios")
    api.add_resource(Login, '/login/<string:param_usuario>', endpoint="login")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        # paper = Papel('admin', 'Administrador do sistema')
        # db.session.add(paper)
        # db.session.commit()
#    create_tables()
    migrate = Migrate(app, db)

    return app

application = create_app()
