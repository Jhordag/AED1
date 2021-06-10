from insertionsort import insertionsort
from mergesort import mergesort
from quicksort import quickSort
from leitura_arquivo import Arquivo
import time
import matplotlib.pyplot as plt
import numpy as np
from estilo import *

def opcao1():
    nome_arquivo = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    arquivo = Arquivo(nome_arquivo)
    lista = arquivo.lerArquivo()
    lista_insert = lista.copy()
    lista_merge = lista.copy()
    lista_quick = lista.copy()
    tamanho_arquivo = len(lista)
    
    #Tempo QuickSort
    quick_start = time.time()
    quickSort(lista_quick)
    quick_end = time.time()
    
    # Tempo InsertionSort
    insert_start = time.time()
    insertionsort(lista_insert)
    insert_end = time.time()
    
    # Tempo MergeSort
    merge_start = time.time()
    mergesort(lista_merge)
    merge_end = time.time()
    
    print(f'\n\033[1;32mOrdenação do arquivo:{nome_arquivo}\033[m')
    print(f'\033[1;37mTempo de Operação Insertion de {tamanho_arquivo-1}: {round(insert_end-insert_start)}\033[m')
    print(f'\033[1;37mTempo de Operação Merge de {tamanho_arquivo-1}: {round(merge_end-merge_start)}\033[m')
    print(f'\033[1;37mTempo de Operação Quick de {tamanho_arquivo-1}: {round(quick_end-quick_start)}\033[m\n')

    data = [round(quick_end-quick_start,3), round(merge_end-merge_start,3), round(insert_end-insert_start,3)]
    labels = ['Quicksort', 'Merge', 'Insertion']

    xs = [i+0.1 for i, _ in enumerate(labels)]
    plt.bar(xs,data )
    plt.ylabel = ('Tempo(s)')
    plt.title(f'\033[1;32mOrdenado {tamanho_arquivo} elementos do arquivo {nome_arquivo} com os três metodos de ordenação\033[m')
    plt.xticks([i+0.1for i, _ in enumerate(labels)],labels)
    for i in range(len(data)):
        plt.annotate(str(data[i]), xy=(xs[i]-0.1,data[i]), size = 10)
    plt.show()

def opcao2():
    nome_arquivo_1 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_2 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_3 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome =[nome_arquivo_1,nome_arquivo_2,nome_arquivo_3]
    times = []

    for i in range(0,3):
        typArq = []
        nome_arquivo = nome[i]
        typArq.append(nome_arquivo)
        arquivo = Arquivo(nome_arquivo)
        lista = arquivo.lerArquivo()
        lista_insert = lista.copy()
        lista_merge = lista.copy()
        lista_quick = lista.copy()
        tamanho_arquivo = len(lista)
        typArq.append(tamanho_arquivo)
        aux = 0
        #Tempo QuickSort
        if aux == 0:
            typArq.append('Quick')
            quick_start = time.time()
            typArq.append(quick_start)
            quickSort(lista_quick)
            quick_end = time.time()
            typArq.append(quick_end)
            aux += 1
        
        if aux == 1:
            # Tempo InsertionSort
            typArq.append('Insertion')
            insert_start = time.time()
            typArq.append(insert_start)
            insertionsort(lista_insert)
            insert_end = time.time()
            typArq.append(insert_end)
            aux += 1
        
        if aux == 2:
            # Tempo MergeSort
            typArq.append('Merge')
            merge_start = time.time()
            typArq.append(merge_start)
            mergesort(lista_merge)
            merge_end = time.time()
            typArq.append(merge_end)

        times.append(typArq)
        
    data = []
    for Type in times:
        print(f'\n\033[1;32mOrdenação do arquivo:{Type[0]}\033[m')
        print(f'Tempo de Operação {Type[2]} de {Type[1]-1}: {round(Type[4]-Type[3])}')
        print(f'Tempo de Operação {Type[5]} de {Type[1]-1}: {round(Type[7]-Type[6])}')
        print(f'Tempo de Operação {Type[8]} de {Type[1]-1}: {round(Type[10]-Type[9])}\n')
        auxdata = [Type[0],round(Type[4]-Type[3],3), round(Type[7]-Type[6],3), round(Type[10]-Type[9],3)]
        data.append(auxdata)   
    labels = [data[0][0],data[1][0],data[2][0]]
    quick =[data[0][1],data[1][1],data[2][1]]
    insert =[data[0][2],data[1][2],data[2][2]]
    merge =[data[0][3],data[1][3],data[2][3]]
    x = np.arange(len(labels))  
    width = 0.25 
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, insert, width, label='Insert')
    rects2 = ax.bar(x + width/2, quick, width, label='Quick')
    rects3 = ax.bar(x + 1.5*width, merge, width, label='Merge')
    
    ax.set_ylabel('Tempo(s)')
    ax.set_title(f'Ordenção de Três DB de {typArq[1]} elementos em comparação com os três metodos de ordenação')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    
    def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width()/2, height),
                            xytext=(0, 3),  
                            textcoords="offset points", size=10,
                            ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    
    fig.tight_layout()
    
    plt.show()
       
def opcao3():
    nome_arquivo_1 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_2 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_3 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome =[nome_arquivo_1,nome_arquivo_2,nome_arquivo_3]
    times = []

    for i in range(0,3):
        typArq = []
        nome_arquivo = nome[i]
        typArq.append(nome_arquivo)
        arquivo = Arquivo(nome_arquivo)
        lista = arquivo.lerArquivo()
        lista_insert = lista.copy()
        tamanho_arquivo = len(lista)
        typArq.append(tamanho_arquivo)
        
        # Tempo InsertionSort
        typArq.append('Insertion')
        insert_start = time.time()
        typArq.append(insert_start)
        insertionsort(lista_insert)
        insert_end = time.time()
        typArq.append(insert_end)
        

        times.append(typArq)
    data = []
    for Type in times:
        print(f'\n\033[1;32mOrdenação do arquivo:{Type[0]}\033[m')
        print(f'\033[1;37mTempo de Operação {Type[2]} de {Type[1]-1}: {round(Type[4]-Type[3])}\033[m')
        auxdata = [Type[0],round(Type[4]-Type[3],3)]
        data.append(auxdata)

    insert = [data[0][1],data[1][1],data[2][1]]
    labels = [data[0][0],data[1][0],data[2][0],]

    xs = [i+0.1 for i, _ in enumerate(labels)]
    plt.bar(xs,insert )
    plt.ylabel = ('Tempo(s)')
    plt.title(f'Ordenado elementos com Insertion')
    plt.xticks([i+0.1for i, _ in enumerate(labels)],labels)
    for i in range(len(insert)):
        plt.annotate(str(insert[i]), xy=(xs[i]-0.1,insert[i]), size = 10)
    plt.show()

def opcao4():
    nome_arquivo_1 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_2 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_3 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome =[nome_arquivo_1,nome_arquivo_2,nome_arquivo_3]
    times = []

    for i in range(0,3):
        typArq = []
        nome_arquivo = nome[i]
        typArq.append(nome_arquivo)
        arquivo = Arquivo(nome_arquivo)
        lista = arquivo.lerArquivo()
        lista_merge = lista.copy()
        tamanho_arquivo = len(lista)
        typArq.append(tamanho_arquivo)        
        
        # Tempo MergeSort
        typArq.append('Merge')
        merge_start = time.time()
        typArq.append(merge_start)
        mergesort(lista_merge)
        merge_end = time.time()
        typArq.append(merge_end)
        

        times.append(typArq)

    data = []
    for Type in times:
        print(f'\n\033[1;32mOrdenação do arquivo:{Type[0]}\033[m')
        print(f'\033[1;37mTempo de Operação {Type[2]} de {Type[1]-1}: {round(Type[4]-Type[3])}\033[m')
        auxdata = [Type[0],round(Type[4]-Type[3],3)]
        data.append(auxdata)

    merge = [data[0][1],data[1][1],data[2][1]]
    labels = [data[0][0],data[1][0],data[2][0],]

    xs = [i+0.1 for i, _ in enumerate(labels)]
    plt.bar(xs,merge )
    plt.ylabel = ('Tempo(s)')
    plt.title(f'Ordenado elementos com Merge')
    plt.xticks([i+0.1for i, _ in enumerate(labels)],labels)
    for i in range(len(merge)):
        plt.annotate(str(merge[i]), xy=(xs[i]-0.1,merge[i]), size = 10)
    plt.show()

def opcao5():
    nome_arquivo_1 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_2 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome_arquivo_3 = input('\n\033[1;37mInforme o Nome do Arquivo com a extenção .dat: \033[m')
    nome =[nome_arquivo_1,nome_arquivo_2,nome_arquivo_3]
    times = []

    for i in range(0,3):
        typArq = []
        nome_arquivo = nome[i]
        typArq.append(nome_arquivo)
        arquivo = Arquivo(nome_arquivo)
        lista = arquivo.lerArquivo()
        lista_quick = lista.copy()
        tamanho_arquivo = len(lista)
        typArq.append(tamanho_arquivo)

        #Tempo QuickSort
        typArq.append('Quick')
        quick_start = time.time()
        typArq.append(quick_start)
        quickSort(lista_quick)
        quick_end = time.time()
        typArq.append(quick_end)        

        times.append(typArq)


    data = []
    for Type in times:
        print(f'\n\033[1;32mOrdenação do arquivo:{Type[0]}\033[m')
        print(f'\033[1;37mTempo de Operação {Type[2]} de {Type[1]-1}: {round(Type[4]-Type[3])}\033[m')
        auxdata = [Type[0],round(Type[4]-Type[3],3)]
        data.append(auxdata)

    quick = [data[0][1],data[1][1],data[2][1]]
    labels = [data[0][0],data[1][0],data[2][0],]

    xs = [i+0.1 for i, _ in enumerate(labels)]
    plt.bar(xs,quick )
    plt.ylabel = ('Tempo(s)')
    plt.title(f'Ordenado elementos com o Quick')
    plt.xticks([i+0.1for i, _ in enumerate(labels)],labels)
    for i in range(len(quick)):
        plt.annotate(str(quick[i]), xy=(xs[i]-0.1,quick[i]), size = 10)
    plt.show()
    

   
if __name__ == '__main__':
    while True:
        list = ['Comparação dos 3 metodos de ordenção usando uma base de dados',
                'Comparação dos 3 metodos de ordenção usando as 3 base de dados',   
                'Comparação do InsertionSort com as 3 bases de dados',
                'Comparação do MergeSort com as 3 bases de dados',
                'Comparação do QuickSort com as 3 bases de dados'
                'Sair da Aplicação']
        operacao = menu(list)
        
        if  operacao == '1':
            opcao1()
            
        elif  operacao == '2':
            opcao2()
        
        elif  operacao == '3':
            opcao3()
        
        elif  operacao == '4':
            opcao4()
        
        elif  operacao == '5':
            opcao5()

        elif  operacao == '0':
            print('Saindo da aplicação')
            break
            
        else:
            print('\nDigite um Número Valido.')

    
    
