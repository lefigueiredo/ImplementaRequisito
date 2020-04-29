import json
from time import sleep

# CORES classe para efeito em print
class cor:
    ROXO = '\033[95m'
    CYAN = '\033[96m'
    CYANESC = '\033[36m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[1;93m'
    VERMELHO = '\033[1;91m'

    BGBRANCO = '\033[47;30m'

    NEGR = '\033[1m'
    SUBLI = '\033[4m'
    FIM = '\033[0m'


def cabecalho(a, texto = ""):
    print(f'{"="*40}\n\033[1m{str(a+texto).center(40)}\033[0;0m\n{"="*40}\n')

# PRINTS logo bUNNi
def logo():
    print()
    print(' =======================')
    print(' |    BEM VINDO AO     |')
    print(' |  SISTEMA ACADÊMICO (\(\ ')
    print(' |        bUNNi       ( -.-)')
    print(' ==================== c(")(")')


# PRINTS Layout menu inicial
def layout_menu():
    print('|'+'='*79+'|')
    print('|'+'bUNNi'.center(79)+'|')
    print('|'+'='*79+'|')
    print('|'+cor.SUBLI+' '*79+cor.FIM+'|')
    print('|'+cor.SUBLI+cor.BGBRANCO+'HOME'.center(12)+cor.FIM+'|'+cor.SUBLI+'ESTUDANTES'.center(12)+cor.FIM+'|'+cor.SUBLI+'PROFESSORES'.center(13)+cor.FIM+'|'+cor.SUBLI+'DISCIPLINAS'.center(13)+cor.FIM+'|'+cor.SUBLI+'TURMAS'.center(12)+cor.FIM+'|'+cor.SUBLI+'MATRÍCULAS'.center(12)+cor.FIM+'|')
    print('|'+' '*79+'|')
    print('| Selecione o menu desejado:' + ' ' * 52 + '|')
    print('|'+' '*79+'|')
    print('|     ('+ cor.NEGR +'1'+ cor.FIM +') Estudantes' + ' ' * 60 + '|')
    print('|     ('+ cor.NEGR +'2'+ cor.FIM +') Professores' + ' ' * 59 + '|')
    print('|     ('+ cor.NEGR +'3'+ cor.FIM +') Disciplinas' + ' ' * 59 + '|')
    print('|     ('+ cor.NEGR +'4'+ cor.FIM +') Turmas' + ' ' * 64 + '|')
    print('|     ('+ cor.NEGR +'5'+ cor.FIM +') Matrículas' + ' ' * 53 + '(\(\   |')
    print('|     ('+ cor.NEGR +'0'+ cor.FIM +') Sair' + ' ' * 59 + '( -.-) |')
    print('|' +cor.SUBLI+' '*72+cor.FIM+'c(")(")|')


# PRINTS Layout menu inicial com tela de erro
def layout_menu_erro():
    print('|'+'='*79+'|')
    print('|'+'bUNNi'.center(79)+'|')
    print('|'+'='*79+'|')
    print('|'+cor.SUBLI+' '*79+cor.FIM+'|')
    print('|'+cor.SUBLI+cor.BGBRANCO+'HOME'.center(12)+cor.FIM+'|'+cor.SUBLI+'ESTUDANTES'.center(12)+cor.FIM+'|'+cor.SUBLI+'PROFESSORES'.center(13)+cor.FIM+'|'+cor.SUBLI+'DISCIPLINAS'.center(13)+cor.FIM+'|'+cor.SUBLI+'TURMAS'.center(12)+cor.FIM+'|'+cor.SUBLI+'MATRÍCULAS'.center(12)+cor.FIM+'|')
    print('|'+' '*79+'|')
    print('| Selecione o menu desejado:' + ' ' * 52 + '|')
    print('|'+' '*45+cor.SUBLI+cor.AMARELO+' '*18+cor.FIM+' '*16+'|')
    print('|     ('+ cor.NEGR +'1'+ cor.FIM +') Estudantes' +' '*25+cor.AMARELO+'|'+cor.VERMELHO+'      AVISO!!     '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
    print('|     ('+ cor.NEGR +'2'+ cor.FIM +') Professores' +' '*24+cor.AMARELO+'|'+cor.VERMELHO+'  Opção inválida! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
    print('|     ('+ cor.NEGR +'3'+ cor.FIM +') Disciplinas' +' '*24+cor.AMARELO+'|'+cor.VERMELHO+' Tente Novamente! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
    print('|     ('+ cor.NEGR +'4'+ cor.FIM +') Turmas' +' '*29+cor.AMARELO+'|'+cor.SUBLI+' '*18+cor.FIM+cor.AMARELO+'|'+cor.FIM+' '*15+'|')
    print('|     ('+ cor.NEGR +'5'+ cor.FIM +') Matrículas' + ' ' * 53 + '(\(\   |')
    print('|     ('+ cor.NEGR +'0'+ cor.FIM +') Sair' + ' ' * 59 + '( -.-) |')
    print('|' +cor.SUBLI+' '*72+cor.FIM+'c(")(")|')
    sleep(3)


# PRINTS layout CATEGORIAS do menu
def categorias(tabela):

    def estudantes():
        print('|' + '=' * 79 + '|')
        print('|' + 'bUNNi'.center(79) + '|')
        print('|' + '=' * 79 + '|')
        print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
        print('|' + ' ' * 79 + '|')
        print('| O que deseja realizar:' + ' ' * 56 + '|')
        print('|' + ' ' * 79 + '|')
        print('|     ('+ cor.NEGR +'1'+ cor.FIM +') Criar novo estudante' + ' ' * 50 + '|')
        print('|     ('+ cor.NEGR +'2'+ cor.FIM +') Atualizar um estudante' + ' ' * 48 + '|')
        print('|     ('+ cor.NEGR +'3'+ cor.FIM +') Excluir um estudante' + ' ' * 50 + '|')
        print('|     ('+ cor.NEGR +'4'+ cor.FIM +') Buscar um estudante' + ' ' * 51 + '|')
        print('|     ('+ cor.NEGR +'5'+ cor.FIM +') Listar estudantes' + ' ' * 46 + '(\(\   |')
        print('|     ('+ cor.NEGR +'0'+ cor.FIM +') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')

    def professores():
        print('|' + '=' * 79 + '|')
        print('|' + 'bUNNi'.center(79) + '|')
        print('|' + '=' * 79 + '|')
        print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
        print('|' + ' ' * 79 + '|')
        print('| O que deseja realizar:' + ' ' * 56 + '|')
        print('|' + ' ' * 79 + '|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar novo professor' + ' ' * 50 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar um professor' + ' ' * 48 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir um professor' + ' ' * 50 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar um professor' + ' ' * 51 + '|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar professores' + ' ' * 45 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')

    def disciplinas():
        print('|' + '=' * 79 + '|')
        print('|' + 'bUNNi'.center(79) + '|')
        print('|' + '=' * 79 + '|')
        print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI + cor.BGBRANCO +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
        print('|' + ' ' * 79 + '|')
        print('| O que deseja realizar:' + ' ' * 56 + '|')
        print('|' + ' ' * 79 + '|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar nova disciplina' + ' ' * 49 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar uma disciplina' + ' ' * 46 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir uma disciplina' + ' ' * 48 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar uma disciplina' + ' ' * 49 + '|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar disciplinas' + ' ' * 45 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')

    def turmas():
        print('|' + '=' * 79 + '|')
        print('|' + 'bUNNi'.center(79) + '|')
        print('|' + '=' * 79 + '|')
        print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
        print('|' + ' ' * 79 + '|')
        print('| O que deseja realizar:' + ' ' * 56 + '|')
        print('|' + ' ' * 79 + '|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar nova turma' + ' ' * 54 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar uma turma' + ' ' * 51 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir uma turma' + ' ' * 53 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar uma turma' + ' ' * 54 + '|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar turmas' + ' ' * 50 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')

    def matrículas():
        print('|' + '=' * 79 + '|')
        print('|' + 'bUNNi'.center(79) + '|')
        print('|' + '=' * 79 + '|')
        print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
        print('|' + ' ' * 79 + '|')
        print('| O que deseja realizar:' + ' ' * 56 + '|')
        print('|' + ' ' * 79 + '|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar nova matrícula' + ' ' * 50 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar uma matrícula' + ' ' * 47 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir uma matrícula' + ' ' * 49 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar uma matrícula' + ' ' * 50 + '|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar matrículas' + ' ' * 46 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')

    if tabela == tabela1:
        estudantes()
    if tabela == tabela2:
        professores()
    if tabela == tabela3:
        disciplinas()
    if tabela == tabela4:
        turmas()
    if tabela == tabela5:
        matrículas()


# PRINTS layout cabecalhos menus de categorias
def ilustra_cabecalho(file_name):
    print('|' + '=' * 79 + '|')
    print('|' + 'bUNNi'.center(79) + '|')
    print('|' + '=' * 79 + '|')
    print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
    if file_name == tabela1:
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
    elif file_name == tabela2:
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
    elif file_name == tabela3:
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI + cor.BGBRANCO +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
    elif file_name == tabela4:
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
    elif file_name == tabela5:
        print('|' +
              cor.SUBLI +
              'HOME'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'ESTUDANTES'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI +
              'PROFESSORES'.center(13) +
              cor.FIM + '|'
              + cor.SUBLI +
              'DISCIPLINAS'.center(13) +
              cor.FIM + '|' +
              cor.SUBLI +
              'TURMAS'.center(12) +
              cor.FIM + '|' +
              cor.SUBLI + cor.BGBRANCO +
              'MATRÍCULAS'.center(12) +
              cor.FIM + '|')
    print('|' + ' ' * 79 + '|')

    if file_name == tabela1:
        print('| >>> Inclusão de: ' +file_name+' ' * 51 + '|')
    elif file_name == tabela2:
        print('| >>> Inclusão de: ' + file_name + ' ' * 50 + '|')
    elif file_name == tabela3:
        print('| >>> Inclusão de: ' + file_name + ' ' * 50 + '|')
    elif file_name == tabela4:
        print('| >>> Inclusão de: ' + file_name + ' ' * 55 + '|')
    elif file_name == tabela5:
        print('| >>> Inclusão de: ' + file_name + ' ' * 51 + '|')
    print('|' + ' ' * 79 + '|')
    print('|' + ' ' * 72 + '(\(\   |')


# PRINTS layout inputs menus de categorias



# JSON escreve
def escrever_json(data, file_name):
    with open(file_name + '.json', 'w') as f:
        json.dump(data, f, indent=4)
        f.close()


# JSON ler json e guardar na memoria
def ler_json(file_name):
    data = {}
    try:
        with open(file_name + '.json', 'r') as f:
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        escrever_json(data, file_name)
        return data


# JSON cria novo registro
# def criar_novo_registro(file_name):
#     data = ler_json(file_name)
#     novo = {}
#     id = '1'
#     ids = [int(k) for k in data.keys()]
#     if len(ids) != 0:
#         id = str(max(ids) + 1)
#     colunas = eval(file_name)
#     cabecalho("Inclusão de ",file_name)
#     for coluna in colunas:
#         print(f'Insira {coluna}: ')
#         valor = input()
#         novo[coluna] = valor
#     data[id] = novo
#     escrever_json(data, file_name)
def criar_novo_registro(file_name):
    def ilustra_colunas():

        if coluna == colunas[0]:
            if len(coluna) == 22:
                print('|     Insira ' + coluna + ':' + ' ' * 37 + '( -.-) |')
                print('|' + ' ' * 72 + 'c(")(")|')
            elif len(coluna) == 17:
                print('|     Insira ' + coluna + ':' + ' ' * 42 + '( -.-) |')
                print('|' + ' ' * 72 + 'c(")(")|')
            elif len(coluna) == 15 or len(coluna) == 14:
                print('|     Insira ' + coluna + ':' + ' ' * 44 + '( -.-) |')
                print('|' + ' ' * 72 + 'c(")(")|')
            elif len(coluna) == 19:
                print('|     Insira ' + coluna + ':' + ' ' * 40 + '( -.-) |')
                print('|' + ' ' * 72 + 'c(")(")|')
            elif len(coluna) == 20:
                print('|     Insira ' + coluna + ':' + ' ' * 39 + '( -.-) |')
                print('|' + ' ' * 72 + 'c(")(")|')
            elif len(coluna) == 18:
                print('|     Insira ' + coluna + ':' + ' ' * 41 + '( -.-) |')
                print('|' + ' ' * 72 + 'c(")(")|')
        elif len(coluna) == 22:
            print('|     Insira ' + coluna + ':' + ' ' * 44 + '|')
            print('|' + ' ' * 79 + '|')
        elif len(coluna) == 17:
            print('|     Insira ' + coluna + ':' + ' ' * 49 + '|')
            print('|' + ' ' * 79 + '|')
        elif len(coluna) == 15 or len(coluna) == 14:
            print('|     Insira ' + coluna + ':' + ' ' * 51 + '|')
            print('|' + ' ' * 79 + '|')
        elif len(coluna) == 19:
            print('|     Insira ' + coluna + ':' + ' ' * 47 + '|')
            print('|' + ' ' * 79 + '|')
        elif len(coluna) == 20:
            print('|     Insira ' + coluna + ':' + ' ' * 46 + '|')
            print('|' + ' ' * 79 + '|')
        elif len(coluna) == 18:
            print('|     Insira ' + coluna + ':' + ' ' * 48 + '|')
            print('|' + ' ' * 79 + '|')

        # print('|     ('+ cor.NEGR +'0'+ cor.FIM +') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        # print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')
    data = ler_json(file_name)
    novo = {}
    id = '1'
    ids = [int(k) for k in data.keys()]
    if len(ids) != 0:
        id = str(max(ids) + 1)
    colunas = eval(file_name)

    ilustra_cabecalho(file_name)

    for coluna in colunas:
        ilustra_colunas()
        valor = input()
        novo[coluna] = valor
    data[id] = novo
    escrever_json(data, file_name)


# JSON le registros
def ler_registro(file_name):
    data = ler_json(file_name)
    registro = None
    identificador = None
    sim = True
    while sim:
        identificador = input('Entre com o ID: ')
        if identificador in data.keys():
            registro = data[identificador]
            print('Registro =', registro)
            sim = False
        else:
            print('ID sem registro!')
            resposta = input('Deseja buscar outro ID? (s/n)').lower()
            if 'n' in resposta:
                sim = False

    return registro, identificador


# JSON atualiza um registro a partir de um ID
def atualizar_registro(file_name):
    data = ler_json(file_name)
    cabecalho("Atualização de ",file_name)
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro não pode ser nulo!')
        finalizar_programa()
    colunas = eval(file_name)
    for coluna in colunas:
        valor = input(f'Informe {coluna}: ')
        registro[coluna] = valor
    data[identificador] = registro
    escrever_json(data, file_name)
    print(f'Registro {identificador} alterado!')


# JSON remove regitro a partir do ID
def remover_registro(file_name):
    data = ler_json(file_name)
    cabecalho("Exclusão de ",file_name)
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro não pode ser nulo!')
    else:
        print('Confirma a remoção do ID:', identificador, '? (s/n)\n'
                                                          'OBS: Essa operação não pode ser desfeita!')
        confirma = input().lower()
        if 's' in confirma:
            data.pop(identificador)
            escrever_json(data, file_name)
            print('Registro', identificador, 'removido!')
        else:
            print('A remoção do registro:', identificador, 'foi cancelada!')


# JSON busca registro a partir de texto
def buscar_por_coluna(file_name):
    data = ler_json(file_name)
    cabecalho("Buscando ",file_name)
    if len(data) == 0:
        print('Base vazia!')
    else:
        while True:
            resultados = {}
            texto = input('Entre com o termo que deseja buscar: ').lower()
            for identificador, registro in data.items():
                for coluna, valor in registro.items():
                    if texto in valor.lower():
                        resultados[identificador] = registro
                        continue
            print(resultados)
            refazer = input('Deseja buscar por outro termo? (s/n)')
            if 's' not in refazer:
                break


# JSON lista registros
def listar_registro(file_name):
    data = ler_json(file_name)
    cabecalho("Listagem de ")
    if len(data) == 0:
        print('Base vazia!')

    else:
        for id, dicionario in data.items():
            print(f'\nId = {id}')
            for chave, valor in dicionario.items():
                print(f'{chave}: {valor}')

    input('\nTecle uma tecla para continuar ...')


# Finaliza o programa
def finalizar_programa():
    print('Finalizando o programa...')
    exit(0)

# PRINTS Limpa a tela
def limpar_tela():
    print('\n' * 100)

# MENU chama prints de menus
def operacao(tabela):
    opcoes = ['1', '2', '3', '4', '5', '0']
    ativo = True
    while ativo:
        limpar_tela()
        categorias(tabela)

        opcao = input().lower()

        if opcao not in opcoes:
            input('Opção inválida! Tente novamente ...: ')
        else:
            limpar_tela()
            if opcao == '1':
                criar_novo_registro(tabela)

            if opcao == '2':
                atualizar_registro(tabela)

            if opcao == '3':
                remover_registro(tabela)

            if opcao == '4':
                buscar_por_coluna(tabela)

            if opcao == '5':
                listar_registro(tabela)

            elif opcao == '0':
                ativo = False


# MENU menu principal
def menu():
    opcoes = ['1', '2', '3', '4', '5', '0']
    ativo = True
    while ativo:
        limpar_tela()
        layout_menu()
        opcao = input()

        if opcao in opcoes:
            if opcao == '1':
                operacao(tabela1)
            elif opcao == '2':
                operacao(tabela2)
            elif opcao == '3':
                operacao(tabela3)
            elif opcao == '4':
                operacao(tabela4)
            elif opcao == '5':
                operacao(tabela5)
            elif opcao == '0':
                ativo = False
        else:
            limpar_tela()
            layout_menu_erro()

    finalizar_programa()


if __name__ == '__main__':
    estudantes = ['Matrícula do estudante', 'Nome do estudante', 'Sobrenome do estudante']
    tabela1 = 'estudantes'  # nome da tabela deve ser o mesmo nome da variável

    professores = ['Codigo do professor', 'Nome do professor', 'Sobrenome do professor']
    tabela2 = 'professores'

    disciplinas = ['Codigo da disciplina', 'Nome da disciplina']
    tabela3 = 'disciplinas'

    turmas = ['Codigo da turma', 'Codigo do professor', 'Codigo da disciplina']
    tabela4 = 'turmas'

    matriculas = ['Codigo da turma', 'Codigo do estudante']
    tabela5 = 'matriculas'

    logo()      #printa logo
    sleep(3)    # espera 3 segundos
    menu()      #chama o menu