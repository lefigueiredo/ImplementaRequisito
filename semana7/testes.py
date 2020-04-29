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

def opcoes(tabela):

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
    tabelinha = tabela
    if tabelinha == tabela1:
        estudantes()
    if tabelinha == tabela2:
        professores()
    if tabelinha == tabela3:
        disciplinas()
    if tabelinha == tabela4:
        turmas()
    if tabelinha == tabela5:
        matrículas()




def operacao(tabela):
    opcoes = ['1', '2', '3', '4', '5', '0']
    ativo = True
    while ativo:
        limpar_tela()
        print('O que você deseja fazer na base', tabela, ':\n\n'
                                                         '(1) Criar novo registro.\n'
                                                         '(2) Atualizar um registro.\n'
                                                         '(3) Excluir um registro.\n'
                                                         '(4) Buscar registros.\n'
                                                         '(5) Listar registros.\n'
                                                         '(0) Voltar menu.\n\n'
                                                         'Faça sua escolha: ')
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















def menu():
    opcoes = ['1', '2', '3', '4', '5', '9']
    ativo = True
    while ativo:
        limpar_tela()
        opcao = input('Selecione a opção desejada:\n\n'
                      '(1) Gerenciar estudantes.\n'
                      '(2) Gerenciar professores.\n'
                      '(3) Gerenciar disciplinas.\n'
                      '(4) Gerenciar turmas.\n'
                      '(5) Gerenciar matrículas.\n'
                      '(9) Sair.\n\n'
                      'Faça sua escolha: ').lower()
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
            elif opcao == '9':
                ativo = False
            else:
                print('Opção inválida! Tente novamente.')

    finalizar_programa()