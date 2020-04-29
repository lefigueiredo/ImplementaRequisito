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

def ler_registro(file_name):
    data = ler_json(file_name)
    registro = None
    identificador = None
    sim = True

    while sim:
        print('|     Digite o Id:' + coluna + ':' + ' ' * 32 + '( -.-) |')
        print('|' + ' ' * 72 + 'c(")(")|')
        identificador = input('|')
        if identificador in data.keys():
            registro = data[identificador]
            for chave, valor in registro:

            if len(identificador) == 1:
                print('|' + ' '*2 + '|' + cor.BGBRANCO + file_name + ':' + identificador + ' '*53 + + '|' + cor.FIM + ' '* 9 + '|'  )
            elif len(identificador) == 2:
                print('|' + ' ' * 2 + '|' + cor.BGBRANCO + file_name + ':' + identificador + ' ' * 52 + + '|' + cor.FIM+ ' ' * 9 + '|' )
            print('|' + ' ' * 2 + cor.SUBLI + '|' + chave + cor.FIM + ' ' * 10 + '|')

        def fazer_tabela(file_name):
            colunas = eval(file_name)
            for coluna in colunas:
                if len(coluna) == 15 or len(coluna) == 14:
                    print('|' + ' ' * 2 + cor.SUBLI + chave + ' '*10  + '|' + valor * 51 + '|')
                elif len(coluna) == 17:
                    print('|     Insira ' + coluna + ':' + ' ' * 49 + '|')
                elif len(coluna) == 18:
                    print('|     Insira ' + coluna + ':' + ' ' * 48 + '|')
                elif len(coluna) == 19:
                    print('|     Insira ' + coluna + ':' + ' ' * 47 + '|')
                elif len(coluna) == 20:
                    print('|     Insira ' + coluna + ':' + ' ' * 46 + '|')
                elif len(coluna) == 22:
                    print('|     Insira ' + coluna + ':' + ' ' * 44 + '|')

            # print('|' + ' ' * 2 + cor.BGBRANCO + 'Matrícula: ' + '10' + ' ' * 57 + cor.FIM + ' ' * 7 + '|')
            # print('|' + ' ' * 4 + 'Matrícula do estudante: 1234')
            # print('|' + ' ' * 4 + 'Matrícula do estudante: 1234')
            # print('|' + ' ' * 79 + '|')
            # print('|' + ' ' * 2 + 'Substituir lalalalalalalalalallalal:' + ' ' * 41 + '|')
            # print('|' + ' ' * 3 + cor.SUBLI + ' ' * 66 + cor.FIM + ' ' * 10 + '|')










            print('Registro =', registro)


            sim = False
        else:
            print('ID sem registro!')
            resposta = input('Deseja buscar outro ID? (s/n)').lower()
            if 'n' in resposta:
                sim = False

    return registro, identificador


























def atualizar_registro(file_name):
    data = ler_json(file_name)
    ilustra_cabecalho(file_name)
    if file_name == tabela1:
        print('| >>> Atualização de ' +file_name+' ' * 49 + '|')
    elif file_name == tabela2:
        print('| >>> Atualização de ' + file_name + ' ' * 48 + '|')
    elif file_name == tabela3:
        print('| >>> Atualização de ' + file_name + ' ' * 48 + '|')
    elif file_name == tabela4:
        print('| >>> Atualização de ' + file_name + ' ' * 53 + '|')
    elif file_name == tabela5:
        print('| >>> Atualização de ' + file_name + ' ' * 49 + '|')
    print('|' + ' ' * 72 + '(\(\   |')

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

