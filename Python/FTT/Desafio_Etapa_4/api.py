from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Inicializando banco de dados:
engine = sqlalchemy.create_engine('sqlite:///db.db', echo=False)
Base = declarative_base()

# Criando Entidade Characters:
class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    descrição = Column(String(300))
    link = Column(String(100))
    programa = Column(String(100))
    animador = Column(String(100))

Base.metadata.create_all(engine)

# Inicializando server flask:
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # para deixar em ordem alfabetica as responses em json
api = Api(app)

def not_found():
    """ Simplesmente retorna not found, e o status code 404"""
    return make_response(
        jsonify(
            message="not found"
        ),
        404
    )

@app.route('/characters', methods=['GET'])
def get_all_characters():
    """ Devolve uma lista com todos os personagens. """

    Session = sessionmaker(bind=engine)
    session = Session()

    characters_list = []
    for i in session.query(Character).order_by(Character.id):
        character_json = {
            "id": i.id,
            "nome": i.nome,
            "descrição": i.descrição,
            "link": i.link,
            "programa": i.programa,
            "animador": i.animador
        }
        characters_list.append(character_json)
    
    if characters_list == []:
        return not_found()
    else:
        return make_response(
            jsonify(
                message="Lista com todos os personagens",
                data=characters_list
            ),
            200
        )

@app.route('/characters', methods=['POST'])
def post_one_character():
    """ Insere um personagem no banco de dados. """

    Session = sessionmaker(bind=engine)
    session = Session()

    character_received = request.json

    new_character = Character(
            nome=character_received['nome'],
            descrição=character_received['descrição'],
            link=character_received['link'],
            programa=character_received['programa'],
            animador=character_received['animador']
    )
    
    session.add(new_character)
    session.commit()

    return make_response(
        jsonify(
            message="Personagem inserido no banco de dados"
        ),
        200
    )

@app.route('/characters', methods=['DELETE'])
def delete_all_characters():
    """ Deleta todos os personagens. """

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Character).delete()

    session.commit()

    return make_response(
        jsonify(
            message="Todos os personagens foram deletados",
        ),
        200
    )


class Character_by_id(Resource):
    def get(self, id):
        """ Pega um personagem por id. """

        Session = sessionmaker(bind=engine)
        session = Session()
       
        character_by_id = session.query(Character).filter_by(id=id).first()

        # testando se character_by_id existe:
        if character_by_id == None:
            return not_found()
        else:
            pass
        
        character_by_id_json = {
            "id": character_by_id.id,
            "nome": character_by_id.nome,
            "descrição": character_by_id.descrição,
            "link": character_by_id.link,
            "programa": character_by_id.programa,
            "animador": character_by_id.animador
        }

        return make_response(
            jsonify(
                message="Personagem com o id escolhido",
                data=character_by_id_json
            ),
            200
        )
        
    def put(self, id):
        """ Modifica um personagem por id """
        Session = sessionmaker(bind=engine)
        session = Session()

        character_original = session.query(Character).filter_by(id=id).first()

        if character_original == None:
            return not_found()
        else:
            pass

        character_json = request.json

        character_original.nome = character_json['nome']
        character_original.descrição = character_json['descrição']
        character_original.link = character_json['link']
        character_original.programa = character_json['programa']
        character_original.animador = character_json['animador']

        session.commit()
        
        return make_response(
        jsonify(
            message="Personagem substituido"
        ),
        200
    )
    
    def delete(self, id):
        """ Deleta um personagem por id. """

        Session = sessionmaker(bind=engine)
        session = Session()

        personagem_by_id = session.query(Character).filter_by(id=id).first()

        if personagem_by_id == None:
            return not_found()
        else:
            pass

        session.delete(personagem_by_id)

        session.commit()

        return make_response(
        jsonify(
            message="Personagem deletado"
        ),
        200
    )
api.add_resource(Character_by_id, "/characters/<int:id>")

class Character_query(Resource):
    def get(self):
        """ 
        Busca um personagem por (id,nome,descrição,link,programa,animador)
        """

        Session = sessionmaker(bind=engine)
        session = Session()

        args = request.args

        if "id" in args.keys():
            character_filtered = session.query(Character).filter_by(id=args['id'])
        elif "nome" in args.keys():
            character_filtered = session.query(Character).filter_by(nome=args['nome'])
        elif "descrição" in args.keys():
            character_filtered = session.query(Character).filter_by(descrição=args['descrição'])
        elif "link" in args.keys():
            character_filtered = session.query(Character).filter_by(link=args['link'])
        elif "programa" in args.keys():
            character_filtered = session.query(Character).filter_by(programa=args['programa'])
        elif "animador" in args.keys():
            character_filtered = session.query(Character).filter_by(animador=args['animador'])
        
        # se character_filtered não existir, é class NoneType
        if character_filtered != None:
            if str(type(character_filtered)) == "<class 'sqlalchemy.orm.query.Query'>":# if se for possivel iterar.
                array_elementos_filtrados = []
                for i in character_filtered:
                    character_filtered_json = {
                        "id": i.id,
                        "nome": i.nome,
                        "descrição": i.descrição,
                        "link": i.link,
                        "programa": i.programa,
                        "animador": i.animador
                    }
                    array_elementos_filtrados.append(character_filtered_json)
                if array_elementos_filtrados != []:
                    return make_response(
                        jsonify(
                        message="Elemento(s) encontrado(s) de acordo com a query.",    
                        data=array_elementos_filtrados
                    )
                )
                elif array_elementos_filtrados == []:
                    return not_found()
                
            elif str(type(character_filtered)) == "<class '__main__.Local'>": # if se não for possivel iterar.
                array_elementos_filtrados = []
                character_filtered_json = {
                        "id": character_filtered.id,
                        "nome": character_filtered.nome,
                        "descrição": character_filtered.descrição,
                        "link": character_filtered.link,
                        "programa": character_filtered.programa,
                        "animador": character_filtered.animador
                    }
                array_elementos_filtrados.append(character_filtered_json)
                return make_response(
                    jsonify(
                        message="Um elemento foi encontrado de acordo com a query",    
                        data=array_elementos_filtrados
                    )
                )
        elif character_filtered == None:
            return not_found()
api.add_resource(Character_query, "/characters/")

if __name__ == "__main__":
    app.run(debug=False)