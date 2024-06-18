def mergesort(lista: list) ->list:

    if len(lista) == 1:
        return lista

    mid_point: int = len(lista)//2

    list_1 : list= mergesort(lista=lista[:mid_point])
    list_2 : list= mergesort(lista=lista[mid_point:])

    return merge(list_1, list_2)


def merge(list_1: list[int], list_2: list[int]) ->list[int]:
    
    i,j = 0, 0

    result: list[int]=[None for _ in range(len(list_1 + list_2))]

    for k in range(len(result)):

        if list_1[i] > list_2[j]:

            result[k] = list_2[j]
            j += 1
        
        else:

            result[k] = list_1[i]
            i += 1






if __name__ == "__main__":

    lista: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]

    mergesort(lista=lista)


