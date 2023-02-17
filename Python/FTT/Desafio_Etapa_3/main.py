import sys, json, textwrap
# textwrap é pera usar dedent, o que estou usando para corrigir...
# formatação bugada de triple quotes dentro de funções.

print(f"""
-- Gerenciador de personagens --
Insira a ação que deseja (1, 2, 0 ou 9):
1. criar personagem
2. visualizar personagens
0. sair
9. configurações""")

# Cria o arquivo JSON, e escreve a estrutura básica necessária:
try:
    with open("file.json", "x") as file:
        file.write("""{"personagens":[]}""")
        file.close()
    print("~~ O arquivo .json foi criado ~~")
except:
    print("", end="")

def ler_json():
        """Lê do banco de dados JSON e retorna o conteúdo manipulavel por python"""
        with open("file.json", "r") as file:
            data = json.load(file)
            file.close()
            return data

def armazenar_em_json(dict: dict):
    """Recebe um argumento que é um dicionário python, e o coloca no banco de dados JSON"""
    with open("file.json", "r") as file:
        data = json.load(file)
        file.close()

    with open("file.json", "w") as file:
        data['personagens'].append(dict)
        json.dump(data, file)
        file.close()
    print(f"~~ personagem: [{dict['nome']}] criado ~~")

def criacao_personagem():
    """Função para criar os personagens"""

    print("\nInsira os dados do personagem:")
    global nome,desc,link,prog,animador
    nome = input("Nome: ")
    desc = input("Descrição: ")
    link = input("Link: ")
    prog = input("Programa: ")
    animador = input("Animador: ")
   
    # Modelo de personagem para colocar no banco de dados:
    personagem = {
        "nome": nome,
        "descrição": desc,
        "link": link,
        "programa": prog,
        "animador": animador
    }

    armazenar_em_json(personagem)

    # Proxima ação:
    choice_input_criar = input(textwrap.dedent(f"""
    -- Proxima ação --
    Insira a ação que deseja (1, 2 ou 0):
    1. criar personagem
    2. visualizar personagens
    0. sair
    Escolha: """))

    if choice_input_criar == "1":
        criacao_personagem()
    elif choice_input_criar == "2":
        visualizar()
    elif choice_input_criar == "0":
        sys.exit()
    else:
        print("~~ Opção inválida, insira 1, 2 ou 0 ~~")
        sys.exit()

def visualizar():
    """Função para visualizar os personagens salvos"""

    print("\nVisualizando todos os personagens salvos:", end="")
    data_unformatted = ler_json()

    for i in data_unformatted['personagens']:
        print(textwrap.dedent(f"""
        Nome: {i['nome']}
        Descrição: ({i['descrição']})
        Link: {i['link']}
        Programa: {i['programa']}
        Animador: {i['animador']}"""))

    # Proxima ação:
    choice_input_visua = input(textwrap.dedent(f"""
    -- Proxima ação --
    Insira a ação que deseja (1, 2 ou 0):
    1. criar personagem
    2. visualizar personagens
    0. sair
    Escolha: """))

    if choice_input_visua == "1":
        criacao_personagem()
    elif choice_input_visua == "2":
        visualizar()
    elif choice_input_visua == "0":
        sys.exit()
    else:
        print("~~ Opção inválida, insira 1, 2 ou 0 ~~")
        sys.exit()

def configs():
    """Função para aprir opções de configurações"""

    choice_input_configs = input(textwrap.dedent(f"""
    -- Proxima ação --
    Insira a ação que deseja (1 ou 0):
    1. limpar banco de dados
    0. sair
    Escolha: """))
    if choice_input_configs == "1":
        with open("file.json", "w") as file:
            file.write("""{"personagens":[]}""")
            file.close()
        print("~~ O banco de dados foi resetado ~~")
    elif choice_input_configs == "0":
        sys.exit()
    else:
        print("~~ Opção inválida ~~")
        sys.exit()

choice_input = input("Escolha: ")

if choice_input == "1":
    criacao_personagem()
elif choice_input == "2":
    visualizar()
elif choice_input == "0":
    sys.exit()
elif choice_input == "9":
    configs()
else:
    print("~~Opção inválida, insira 1, 2, 0 ou 9~~")
    sys.exit()