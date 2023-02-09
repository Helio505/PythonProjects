import sys

print(f"""
Insira a ação que deseja (1, 2 ou 0):
1. criar personagem
2. visualizar personagens
0. sair
""")

try:
    with open("file.txt", "x") as file:
        file.close()
    print("~~O arquivo .txt foi criado~~")
except:
    print("", end="")

def criacao_personagem():
    """Função para criar os personagens"""

    print("Insira os dados do personagem")
    global nome,desc,link,prog,animador
    nome = input("Nome: ")
    desc = input("Descrição: ")
    link = input("Link: ")
    prog = input("Programa: ")
    animador = input("Animador: ")
   
    with open("file.txt", "a") as file:
        file.write(f"""{nome}\n({desc})\n{link}\n{prog}\n{animador}\n""")
        file.close()
     
    choice_input_criar = input("""\nInsira a ação que deseja (1, 2 ou 0):
    1. criar personagem
    2. visualizar personagens
    0. sair
    Escolha: """)

    if choice_input_criar == "1":
        criacao_personagem()
    elif choice_input_criar == "2":
        visualizar()
    elif choice_input_criar == "0":
        sys.exit()
    else:
        print("~~Opção inválida, insira 1, 2 ou 0~~")
        sys.exit()


def visualizar():
    """Função para visualizar os personagens salvos"""

    print("Visualizando todos os personagens salvos:")

    # pega o conteúdo do arquivo e transforma em array:
    with open("file.txt", "r") as file:
        conteudo_file = file.readlines()
        if conteudo_file == []:
            print("~~Nenhum personagem salvo~~")
        file.close()

    # para visualizar os personagens:
    count=0
    for i in conteudo_file:
        print(i, end="")
        count+=1
        if count % 5 == 0:
            print("\n")

    choice_input_visua = input("""\nInsira a ação que deseja (1, 2 ou 0):
    1. criar personagem
    2. visualizar personagens
    0. sair
    Escolha: """)

    if choice_input_visua == "1":
        criacao_personagem()
    elif choice_input_visua == "2":
        visualizar()
    elif choice_input_visua == "0":
        sys.exit()
    else:
        print("~~Opção inválida, insira 1, 2 ou 0~~")
        sys.exit()

choice_input = input("Escolha: ")

if choice_input == "1":
    criacao_personagem()
elif choice_input == "2":
    visualizar()
elif choice_input == "0":
    sys.exit()
else:
    print("~~Opção inválida, insira 1, 2 ou 0~~")
    sys.exit()