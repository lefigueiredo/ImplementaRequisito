import json
from time import sleep


# CORES classe para efeito em print
class cor:
    AMARELO = '\033[1;93m'
    VERMELHO = '\033[1;91m'

    BGBRANCO = '\033[47;30m'

    NEGR = '\033[1m'
    SUBLI = '\033[4m'

    FIM = '\033[0m'


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


# PRINTS layout CATEGORIAS do menu com tela de erro
def categorias_erro(tabela):

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
        print('|'+' '*45+cor.SUBLI+cor.AMARELO+' '*18+cor.FIM+' '*16+'|')
        print('|     ('+ cor.NEGR +'1'+ cor.FIM +') Criar novo estudante' + ' ' * 15+cor.AMARELO+'|'+cor.VERMELHO+'      AVISO!!     '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     ('+ cor.NEGR +'2'+ cor.FIM +') Atualizar um estudante' + ' ' * 13+cor.AMARELO+'|'+cor.VERMELHO+'  Opção inválida! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     ('+ cor.NEGR +'3'+ cor.FIM +') Excluir um estudante' + ' ' * 15 +cor.AMARELO+'|'+cor.VERMELHO+' Tente Novamente! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     ('+ cor.NEGR +'4'+ cor.FIM +') Buscar um estudante' + ' ' * 16+cor.AMARELO+'|'+cor.SUBLI+' '*18+cor.FIM+cor.AMARELO+'|'+cor.FIM+' '*15+'|')
        print('|     ('+ cor.NEGR +'5'+ cor.FIM +') Listar estudantes' + ' ' * 46 + '(\(\   |')
        print('|     ('+ cor.NEGR +'0'+ cor.FIM +') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')
        sleep(3)

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
        print('|'+' '*45+cor.SUBLI+cor.AMARELO+' '*18+cor.FIM+' '*16+'|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar novo professor' + ' ' * 15+cor.AMARELO+'|'+cor.VERMELHO+'      AVISO!!     '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar um professor' + ' ' * 13+cor.AMARELO+'|'+cor.VERMELHO+'  Opção inválida! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir um professor' + ' ' * 15 +cor.AMARELO+'|'+cor.VERMELHO+' Tente Novamente! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar um professor' + ' ' * 16+cor.AMARELO+'|'+cor.SUBLI+' '*18+cor.FIM+cor.AMARELO+'|'+cor.FIM+' '*15+'|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar professores' + ' ' * 45 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')
        sleep(3)

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
        print('|'+' '*45+cor.SUBLI+cor.AMARELO+' '*18+cor.FIM+' '*16+'|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar nova disciplina' + ' ' * 14+cor.AMARELO+'|'+cor.VERMELHO+'      AVISO!!     '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar uma disciplina' + ' ' * 11+cor.AMARELO+'|'+cor.VERMELHO+'  Opção inválida! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir uma disciplina' + ' ' * 13 +cor.AMARELO+'|'+cor.VERMELHO+' Tente Novamente! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar uma disciplina' + ' ' * 14+cor.AMARELO+'|'+cor.SUBLI+' '*18+cor.FIM+cor.AMARELO+'|'+cor.FIM+' '*15+'|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar disciplinas' + ' ' * 45 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')
        sleep(3)

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
        print('|'+' '*45+cor.SUBLI+cor.AMARELO+' '*18+cor.FIM+' '*16+'|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar nova turma' + ' ' * 19+cor.AMARELO+'|'+cor.VERMELHO+'      AVISO!!     '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar uma turma' + ' ' * 16+cor.AMARELO+'|'+cor.VERMELHO+'  Opção inválida! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir uma turma' + ' ' * 18 +cor.AMARELO+'|'+cor.VERMELHO+' Tente Novamente! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar uma turma' + ' ' * 19+cor.AMARELO+'|'+cor.SUBLI+' '*18+cor.FIM+cor.AMARELO+'|'+cor.FIM+' '*15+'|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar turmas' + ' ' * 50 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')
        sleep(3)

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
        print('|'+' '*45+cor.SUBLI+cor.AMARELO+' '*18+cor.FIM+' '*16+'|')
        print('|     (' + cor.NEGR + '1' + cor.FIM + ') Criar nova matrícula' + ' ' * 15+cor.AMARELO+'|'+cor.VERMELHO+'      AVISO!!     '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '2' + cor.FIM + ') Atualizar uma matrícula' + ' ' * 12+cor.AMARELO+'|'+cor.VERMELHO+'  Opção inválida! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '3' + cor.FIM + ') Excluir uma matrícula' + ' ' * 14 +cor.AMARELO+'|'+cor.VERMELHO+' Tente Novamente! '+cor.AMARELO+'|'+cor.FIM+ ' ' * 15 + '|')
        print('|     (' + cor.NEGR + '4' + cor.FIM + ') Buscar uma matrícula' + ' ' * 15+cor.AMARELO+'|'+cor.SUBLI+' '*18+cor.FIM+cor.AMARELO+'|'+cor.FIM+' '*15+'|')
        print('|     (' + cor.NEGR + '5' + cor.FIM + ') Listar matrículas' + ' ' * 46 + '(\(\   |')
        print('|     (' + cor.NEGR + '0' + cor.FIM + ') Voltar ao menu inicial' + ' ' * 41 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM + 'c(")(")|')
        sleep(3)

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
5def criar_novo_registro(file_name):
    # PRINTS layout inputs menus de categorias
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

    data = ler_json(file_name)
    novo = {}
    id = '1'
    ids = [int(k) for k in data.keys()]
    if len(ids) != 0:
        id = str(max(ids) + 1)
    colunas = eval(file_name)

    ilustra_cabecalho(file_name)
    if file_name == tabela1:
        print('| >>> Inclusão de ' +file_name+' ' * 52 + '|')
    elif file_name == tabela2:
        print('| >>> Inclusão de ' + file_name + ' ' * 51 + '|')
    elif file_name == tabela3:
        print('| >>> Inclusão de ' + file_name + ' ' * 51 + '|')
    elif file_name == tabela4:
        print('| >>> Inclusão de ' + file_name + ' ' * 56 + '|')
    elif file_name == tabela5:
        print('| >>> Inclusão de ' + file_name + ' ' * 52 + '|')
    print('|' + ' ' * 72 + '(\(\   |')

    for coluna in colunas:
        ilustra_colunas()
        valor = input("| ")
        novo[coluna] = valor
    data[id] = novo
    escrever_json(data, file_name)


# JSON le registros
def ler_registro(file_name):
    data = ler_json(file_name)
    registro = None
    identificador = None
    sim = True
    titulo = file_name

    while sim:
        print('|     Digite o Id:' + ' ' * 55 + '( -.-) |')
        print('|' + ' ' * 72 + 'c(")(")|')
        identificador = input('| ')
        if identificador in data.keys():
            registro = data[identificador]
            if len(identificador) == 1:
                print('|' + ' '*2 + cor.BGBRANCO + 'Id: ' + identificador + ' '*65 + cor.FIM + ' '* 7 + '|'  )

            elif len(identificador) > 1:
                print('|' + ' '*2 + cor.BGBRANCO + 'Id: ' + identificador + ' '*64 + cor.FIM + ' '* 7 + '|'  )

            for chave, valor in registro.items():
                print('|' + ' ' * 4 + chave + ': ' + valor)
            print('|  '+cor.BGBRANCO+' '*70+ cor.FIM+' '*7+'|')
            print('|'+' '*79+'|')
            sim = False

        else:
            print('|' + ' ' * 30 + cor.SUBLI + cor.AMARELO + ' ' * 20 + cor.FIM + ' ' * 29 + '|')
            print('|' + ' ' * 29 + cor.AMARELO + '|' + cor.VERMELHO + ' Id não cadastrado! ' + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print('|' + ' ' * 29 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 20 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print('|' + ' ' * 79 + '|')

            print('|'+' '*4+'Deseja buscar outro ID? (s/n)')
            resposta = input("|").lower()
            if resposta == 'n':
                sim = False

    return registro, identificador


# JSON atualiza um registro a partir de um ID
def atualizar_registro(file_name):
    data = ler_json(file_name)
    ilustra_cabecalho(file_name)

    if file_name == tabela1:
        print('| >>> Atualização de ' + file_name + ' ' * 49 + '|')
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
        print('|' + ' ' * 29 + cor.SUBLI + cor.AMARELO + ' ' * 23 + cor.FIM + ' ' * 27 + '|')
        print(
            '|' + ' ' * 28 + cor.AMARELO + '|' + cor.VERMELHO + ' Impossível continuar! ' + cor.AMARELO + '|' + cor.FIM + ' ' * 26 + '|')
        print(
            '|' + ' ' * 28 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 23 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 26 + '|')
        print('|' + ' ' * 79 + '|')
        finalizar_programa()

    colunas = eval(file_name)
    for coluna in colunas:
        valor = input(f'|  Informe {coluna}: ')
        registro[coluna] = valor
    data[identificador] = registro
    escrever_json(data, file_name)

    print('|'+' '*31+cor.AMARELO+cor.SUBLI+' '*17+cor.FIM+' '*31+'|')
    print('|'+' '*30+cor.AMARELO+'|'+cor.VERMELHO+'  Dado alterado  '+cor.AMARELO+'|'+cor.FIM+' '*30+'|')
    print('|' + ' ' * 30 + cor.AMARELO + '|' + cor.VERMELHO + '   com sucesso!  ' + cor.AMARELO + '|' + cor.FIM + ' ' * 30 + '|')
    print('|' + ' ' * 30 + cor.AMARELO + '|' + cor.SUBLI + ' '*17+cor.FIM+cor.AMARELO+ '|' + cor.FIM + ' ' * 30 + '|')
    print('|'+cor.SUBLI+' '*79+cor.FIM+'|')
    sleep(3)


# JSON remove regitro a partir do ID
def remover_registro(file_name):
    data = ler_json(file_name)
    ilustra_cabecalho(file_name)

    if file_name == tabela1:
        print('| >>> Remoção de ' + file_name + ' ' * 53 + '|')
    elif file_name == tabela2:
        print('| >>> Remoção de ' + file_name + ' ' * 52 + '|')
    elif file_name == tabela3:
        print('| >>> Remoção de ' + file_name + ' ' * 52 + '|')
    elif file_name == tabela4:
        print('| >>> Remoção de ' + file_name + ' ' * 57 + '|')
    elif file_name == tabela5:
        print('| >>> Remoção de ' + file_name + ' ' * 53 + '|')
    print('|' + ' ' * 72 + '(\(\   |')

    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('|' + ' ' * 29 + cor.SUBLI + cor.AMARELO + ' ' * 23 + cor.FIM + ' ' * 27 + '|')
        print(
            '|' + ' ' * 28 + cor.AMARELO + '|' + cor.VERMELHO + ' Impossível continuar! ' + cor.AMARELO + '|' + cor.FIM + ' ' * 26 + '|')
        print(
            '|' + ' ' * 28 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 23 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 26 + '|')
        print('|' + ' ' * 79 + '|')
        finalizar_programa()

    else:
        if len(identificador) == 1:
            print('|  Confirma a remoção do ID: '+ identificador + ' (s/n)?'+' ' * 43 + '|')
        elif len(identificador) > 1:
            print('|  Confirma a remoção do ID: '+ identificador + ' (s/n)?'+' ' * 42 + '|')

        print('|'+' '*79+'|')
        print('|    '+cor.AMARELO+ 'OBS: '+ cor.VERMELHO+'Essa operação não pode ser desfeita!'+cor.FIM+ ' '*34+'|')
        confirma = input('| ').lower()
        if 's' in confirma:
            data.pop(identificador)
            escrever_json(data, file_name)

            print('|' + ' ' * 30 + cor.SUBLI + cor.AMARELO + ' ' * 20 + cor.FIM + ' ' * 29 + '|')
            print(
                '|' + ' ' * 29 + cor.AMARELO + '|' + cor.VERMELHO + '    Id removido     ' + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print(
                '|' + ' ' * 29 + cor.AMARELO + '|' + cor.VERMELHO + '    com sucesso!    ' + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print(
                '|' + ' ' * 29 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 20 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print('|' + ' ' * 79 + '|')
            sleep(3)

        else:
            print('|' + ' ' * 30 + cor.SUBLI + cor.AMARELO + ' ' * 20 + cor.FIM + ' ' * 29 + '|')
            print(
                '|' + ' ' * 29 + cor.AMARELO + '|' + cor.VERMELHO + '  A remoção do Id   ' + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print(
                '|' + ' ' * 29 + cor.AMARELO + '|' + cor.VERMELHO + '   foi cancelada!   ' + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print(
                '|' + ' ' * 29 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 20 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 28 + '|')
            print('|' + ' ' * 79 + '|')
            sleep(3)


# JSON busca registro a partir de texto
def buscar_por_coluna(file_name):
    data = ler_json(file_name)
    ilustra_cabecalho(file_name)

    if len(data) == 0:
        print('|' + ' ' * 31 + cor.SUBLI + cor.AMARELO + ' ' * 15 + cor.FIM + ' ' * 33 + '|')
        print(
            '|' + ' ' * 30 + cor.AMARELO + '|' + cor.VERMELHO + '  Base vazia!  ' + cor.AMARELO + '|' + cor.FIM + ' ' * 32 + '|')
        print(
            '|' + ' ' * 30 + cor.AMARELO + '|' + cor.VERMELHO + ' Insira dados! ' + cor.AMARELO + '|' + cor.FIM + ' ' * 25 + '(\(\   |')
        print(
            '|' + ' ' * 30 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 15 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 25 + '( -.-) |')
        print('|' + cor.SUBLI + ' ' * 72 + cor.FIM +  'c(")(")|')

    else:
        while True:
            resultados = {}
            lista = []
            print('| >>> Busca por termo' + ' ' * 59 + '|')
            print('|' + ' ' * 72 + '(\(\   |')
            print('|     Digite o termo que deseja buscar:' + ' ' * 34 + '( -.-) |')
            print('|' + ' ' * 72 + 'c(")(")|')

            texto = input('| ').lower()

            for identificador, registro in data.items():
                for coluna, valor in registro.items():
                    lista.append((identificador,coluna, valor))
                    if texto in valor.lower():
                        resultados[identificador] = registro
                        continue

            for id, dicionarioall in resultados.items():
                if len(id) == 1:
                    print('|' + ' ' * 2 + cor.BGBRANCO + 'Id: ' + id + ' ' * 63 + cor.FIM + ' '*9 + '|')
                    for chave, valor in dicionarioall.items():
                        ihu = len(('|    ' + chave + ': ' + valor))
                        ihaa = 80 - ihu
                        print(('|    ' + chave + ': ' + valor)+(' ' * ihaa) + ('|'))

                    print('|  ' + cor.BGBRANCO + ' ' * 68 + cor.FIM +' '*9+ '|')
                    print('|' + ' ' * 79 + '|')
                    print('|' + ' ' * 79 + '|')

                elif len(id) > 1:

                    print('|' + ' ' * 2 + cor.BGBRANCO + 'Id: ' + id + ' ' * 62 + cor.FIM + ' '*9 + '|')
                    for chave, valor in dicionarioall.items():
                        ihu = len(('|    ' + chave + ': ' + valor))
                        ihaa = 80 - ihu
                        print(('|    ' + chave + ': ' + valor) + (' ' * ihaa) + ('|'))

                    print('|  ' + cor.BGBRANCO + ' ' * 68 + cor.FIM + ' ' * 9 + '|')
                    print('|' + ' ' * 79 + '|')
                    print('|' + ' ' * 79 + '|')

            print('|' + ' ' * 79 + '|')
            refazer = input('|    Deseja buscar por outro termo (s/n)?'+' '*39+'|')
            if 'n' in refazer:
                break


# JSON lista registros
def listar_registro(file_name):
    data = ler_json(file_name)
    ilustra_cabecalho(file_name)

    print('| >>> Listagem completa' + ' ' * 50 + '(\(\   |')
    print('|' + ' ' * 72 + '( -.-) |')
    print('|' + ' ' * 72 + 'c(")(")|')

    if len(data) == 0:
        print('|' + ' ' * 31 + cor.SUBLI + cor.AMARELO + ' ' * 15 + cor.FIM + ' ' * 33 + '|')
        print(
            '|' + ' ' * 30 + cor.AMARELO + '|' + cor.VERMELHO + '  Base vazia!  ' + cor.AMARELO + '|' + cor.FIM + ' ' * 32 + '|')
        print(
            '|' + ' ' * 30 + cor.AMARELO + '|' + cor.VERMELHO + ' Insira dados! ' + cor.AMARELO + '|' + cor.FIM + ' ' * 32 + '|')
        print(
            '|' + ' ' * 30 + cor.AMARELO + '|' + cor.SUBLI + ' ' * 15 + cor.FIM + cor.AMARELO + '|' + cor.FIM + ' ' * 32 + '|')
        print('|' + ' ' * 79 + '|')


    else:
        for id, dicionario in data.items():
            if len(id) == 1:
                print('|' + ' ' * 2 + cor.BGBRANCO + 'Id: ' + id + ' ' * 63 + cor.FIM + ' ' * 9 + '|')
                for chave, valor in dicionario.items():
                    ihu = len(('|    ' + chave + ': ' + valor))
                    ihaa = 80 - ihu
                    print(('|    ' + chave + ': ' + valor) + (' ' * ihaa) + ('|'))

                print('|  ' + cor.BGBRANCO + ' ' * 68 + cor.FIM + ' ' * 9 + '|')
                print('|' + ' ' * 79 + '|')
                print('|' + ' ' * 79 + '|')

            elif len(id) > 1:

                print('|' + ' ' * 2 + cor.BGBRANCO + 'Id: ' + id + ' ' * 62 + cor.FIM + ' ' * 9 + '|')
                for chave, valor in dicionario.items():
                    ihu = len(('|    ' + chave + ': ' + valor))
                    ihaa = 80 - ihu
                    print(('|    ' + chave + ': ' + valor) + (' ' * ihaa) + ('|'))

                print('|  ' + cor.BGBRANCO + ' ' * 68 + cor.FIM + ' ' * 9 + '|')
                print('|' + ' ' * 79 + '|')
                print('|' + ' ' * 79 + '|')


    input('|    Tecle uma tecla para continuar ...'+' '*41+'|')




# Finaliza o programa
def finalizar_programa():
    print('|' + '=' * 79 + '|')
    print('|' + 'bUNNi'.center(79) + '|')
    print('|' + '=' * 79 + '|')
    print('|' + cor.SUBLI + ' ' * 79 + cor.FIM + '|')
    print('|' + cor.SUBLI + cor.BGBRANCO + 'HOME'.center(12) + cor.FIM + '|' + cor.SUBLI + 'ESTUDANTES'.center(
        12) + cor.FIM + '|' + cor.SUBLI + 'PROFESSORES'.center(13) + cor.FIM + '|' + cor.SUBLI + 'DISCIPLINAS'.center(
        13) + cor.FIM + '|' + cor.SUBLI + 'TURMAS'.center(12) + cor.FIM + '|' + cor.SUBLI + 'MATRÍCULAS'.center(
        12) + cor.FIM + '|')
    print('|' + ' ' * 79 + '|')
    print('| >>> Finalizando o programa...' + ' ' * 49 + '|')
    print('|' + ' ' * 79 + '|')
    print('|' + ('=' * 23).center(79) + '|')
    print('|' + ('|  SISTEMA ACADÊMICO  |').center(79) + '|')
    print('|' + ' ' * 28 + '|        bUNNi       (\(\ ' + ' ' * 25 + '|')
    print('|' + ' ' * 28 + '|      ATÉ BREVE     ( -.-)' + ' ' * 24 + '|')
    print('|' + ' ' * 28 + '==================== c(")(")' + ' ' * 23 + '|')
    print('|' + ' ' * 79 + '|')
    print('|' + ' ' * 79 + '|')
    print('|' + cor.SUBLI + ' ' * 64 + cor.FIM + '(⌐■_■) GG EASY|')
    sleep(3)
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
            categorias_erro(tabela)
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