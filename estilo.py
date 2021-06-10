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
    return '-' * tam


def inteface(txt):
    print(linha())
    print(txt.center(60))
    print(linha())


def menu(lista):
    inteface('\033[33mOperações que podem ser feitas na aplicação\033[m')
    aux = 1
    for item in lista:
        print(f'\033[32m{aux}- \033[34m{item}\033[m')
        aux += 1
    print(linha())
    opc = leiaInt('Informe o Número da Operação que deseja realizar: ')
    return opc
