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



    #print '\033[42;1;33m'+'Isto eh amarelo negrito com fundo verde'+'\033[0;0m'

def ilustra_cabecalho(file_name):
    print('|' + '=' * 79 + '|')
    print('|' + 'bUNNi'.center(79) + '|')
    print('|' + '=' * 79 + '|')
    print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
    for cati in range(5):
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
    for catig in range(5):
        if file_name == tabela1:
            print('| >>> Inclusão de :' +file_name+' ' * 51 + '|')
        elif file_name == tabela2:
            print('| >>> Inclusão de :' + file_name + ' ' * 50 + '|')
        elif file_name == tabela3:
            print('| >>> Inclusão de :' + file_name + ' ' * 50 + '|')
        elif file_name == tabela4:
            print('| >>> Inclusão de :' + file_name + ' ' * 55 + '|')
        elif file_name == tabela5:
            print('| >>> Inclusão de :' + file_name + ' ' * 51 + '|')
    print('|' + ' ' * 79 + '|')
    print('|' + ' ' * 72 + '(\(\   |')

def ilustra_colunas():
    for coluna in colunas:
        if coluna = colunas[0]:
            if len(coluna) == 22:
                print('|     Insira ' + coluna + ':' + ' ' * 37 + '( -.-) |')
                print('|'+' '*71 + 'c(")(")|')
            elif len(coluna) == 17:
                print('|     Insira ' + coluna + ':' + ' ' * 42 + '( -.-) |')
                print('|' + ' ' * 71 + 'c(")(")|')
            elif len(coluna) == 15 or len(coluna) == 14:
                print('|     Insira ' + coluna + ':' + ' ' * 44 + '( -.-) |')
                print('|' + ' ' * 71 + 'c(")(")|')
            elif len(coluna) == 19:
                print('|     Insira ' + coluna + ':' + ' ' * 40 + '( -.-) |')
                print('|' + ' ' * 71 + 'c(")(")|')
            elif len(coluna) == 20:
                print('|     Insira ' + coluna + ':' + ' ' * 39 + '( -.-) |')
                print('|' + ' ' * 71 + 'c(")(")|')
            elif len(coluna) == 18:
                print('|     Insira ' + coluna + ':' + ' ' * 41 + '( -.-) |')
                print('|' + ' ' * 71 + 'c(")(")|')
        elif len(coluna) == 22:
            print('|     Insira ' + coluna + ':' + ' ' * 44 + '|')
            print('|'+' '*79+'|')
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

73


def criar_novo_registro(file_name): #estudantes
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



