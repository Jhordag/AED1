def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário não digitou nenhum valor.\033[m')
            return ''
        else:
            return n

def linha(tam=60):
    return '\033[1;91m-\033[m' * tam


def inteface(txt):
    print(linha())
    print(txt.center(60))
    print(linha())


def menu(lista):
    inteface('\033[1;93mOperações que podem ser feitas na aplicação\033[m')
    aux = 1
    for item in lista:
        print(f'\033[32m{aux}- \033[36m{item}\033[m')
        aux += 1
    print(linha())
    opc = leiaInt('\033[1;37mInforme o Número da Operação que deseja realizar: \033[m')
    return opc
