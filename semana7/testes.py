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

def atualizar_registro(file_name):
    data = ler_json(file_name)
    ilustra_cabecalho(file_name)

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

