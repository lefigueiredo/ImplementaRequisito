class cor:
    ROXO = '\033[35m'
    CYAN = '\033[96m'
    CYANESC = '\033[36m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[1;93m'
    VERMELHO = '\033[1;41,31m'

    BGBRANCO = '\033[47;30m'

    NEGR = '\033[1m'
    SUBLI = '\033[4m'
    FIM = '\033[0m'


for chave, valor in dicionarioall.items():
    desenho += 1
    if desenho == 2:
        ihu = len(('| ' + chave + ': ' + valor))
        ihaa = 73 - ihu
        print(('| ' + chave + ': ' + valor) + (' ' * ihaa) + ('c(")(")|'))
    else:
        ihu = len(('| ' + chave + ': ' + valor))
        ihaa = 80 - ihu
        print(('| ' + chave + ': ' + valor) + (' ' * ihaa) + ('|'))
    if desenho == 4 or desenho == 5:
        desenho = 1

print('|  ' + cor.BGBRANCO + ' ' * 68 + cor.FIM + ' ' * 9 + '|')
print('|' + ' ' * 79 + '|')