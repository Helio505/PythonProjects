import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# /////////////// PARTE PARA: CRIAÇÃO DO BANCO DE DADOS ///////////////////
engine = sqlalchemy.create_engine('sqlite:///db.db', echo=False)
Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    descrição = Column(String(300))
    link = Column(String(100))
    programa = Column(String(100))
    animador = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# /////////////// PARTE PARA: CRIAÇÃO DO BANCO DE DADOS ///////////////////

# //////////////////////// PARTE PARA INSERIR ////////////////////////
session.add_all([
    Character(
            id=1,
            nome="Batman",
            descrição="Justiceiro que se veste de morcego.",
            link="https://personagens.com/imagens/batman.png",
            programa="paint",
            animador="Davi Andrade Melo"
    ),
    Character(
            id=2,
            nome="Jon Snow",
            descrição="Personagem que não sabe de nada.",
            link="https://personagens.com/imagens/john-snow.png",
            programa="Krita",
            animador="Joana Arruda"
    ),
    Character(
            id=3,
            nome="Shrek",
            descrição="Ogro que só quer viver sua vida em paz no seu sitio.",
            link="https://personagens.com/imagens/shrek.png",
            programa="Paint.net",
            animador="Letícia Azevedo"
    ),
    Character(
            id=4,
            nome="Wolverine",
            descrição="Tem poderes de cura elevados, e possui o esqueleto feito de um metal quase indestrutivel.",
            link="https://personagens.com/imagens/wolverine.png",
            programa="Photoshop",
            animador="Leonardo Caetano da Silva"
    ),
])
session.commit()
# //////////////////////// PARTE PARA INSERIR ////////////////////////