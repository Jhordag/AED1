def quickSort(lista):
    esq = []
    equal = []
    dire = []
    if len(lista)>1:
        pivot = lista[len(lista)//2]
        for i in lista:
            if i<pivot:
                esq.append(i)
            elif i>pivot:
                dire.append(i)
            elif i==pivot:
                equal.append(i)
        return quickSort(esq) + equal + quickSort(dire)
    return lista
