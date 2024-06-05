import copy
def list_statistics(numbers: list[int]) -> ... :
    # cancella ... e definisci il tipo del dato di ritorno, successivamente cancella pass e scrivi il tuo codice
        print (max(numbers))
        print(min(numbers))
        print(sum(numbers)/len(numbers))
out=list_statistics([1,2,3,4,5])
        
def list_statistics(numbers: list[int]) -> ... :
    # cancella ... e definisci il tipo del dato di ritorno, successivamente cancella pass e scrivi il tuo codice
    print (max(numbers),min(numbers),sum(numbers)/len(numbers))
out=list_statistics([1,2,3,4,5])

#scivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

def remove_duplicates(lista: list):
    
    for i in lista:
        if lista.count(i)>1:
            lista.remove(i)
    print(lista)
out=remove_duplicates([4, 5, 'a', 4, 6])

def rotate_left(elements: list, k: int) -> list:
    # cancella pass e scrivi il tuo codice
    x=(k-(len(elements)))
   
    if k> len(elements):
        slice_elements=elements[x:len(elements)]+ elements[:k]
    else:
        slice_elements=elements[k:len(elements)]+ elements[:k]
    return slice_elements
print(rotate_left([1, 2, 3, 4, 5], 8))