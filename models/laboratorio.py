from sqlalchemy import Table, Column, Integer, String
from database import Base, engine

class Laboratorio(Base):
    __tablename__ = 'laboratorios'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(100))
    host = Column(String(30))
    port = Column(Integer)
    tempo_experimento = Column(Integer)

    def __init__(self, name, description, host, port, tempo_experimento):
        self.name = name
        self.description = description
        self.host = host
        self.port = port
        self.tempo_experimento = tempo_experimento

    def __repr__(self):
        return 'Laboratorio: {} -> {}'.format(self.name, self.description)

# Base.metadata.create_all(engine, [Base.metadata.tables["laboratorios"]])