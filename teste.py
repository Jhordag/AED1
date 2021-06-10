import time
import numpy as np

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

list =[]
with open('ordenado_100mil.dat') as f:
    for line in f:
        if(line.strip() != ''): 
            line_spl = line.split(' ') 
            cols = line_spl[:] 
            list.append([cols[2].strip(),cols[0],cols[1]]) 

quick_start = time.time()
np.sort(list, kind = 'quick sort')
quick_end = time.time()
print(quick_end-quick_start)

quick_start = time.time()
np.sort(list,kind = 'merge sort')
quick_end = time.time()
print(quick_end-quick_start)


quick_start = time.time()
a =quickSort(list)
quick_end = time.time()

print(quick_end-quick_start)
