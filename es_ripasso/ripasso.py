"""
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
For example:

Test	Result
print(list_statistics([1, 2, 3, 4, 5]))
(5, 1, 3.0)

"""

def list_statistics(numbers: list[int]) -> ... :
      return max(numbers),min(numbers),sum(numbers)/len(numbers)

print(list_statistics([1, 2, 3, 4, 5]))

#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
#mantenendo l'ordine originale degli elementi.


def remove_duplicates(lista: list):
    lista2=[]
    for i in lista:
         if i not in lista2:
              lista2.append(i)
    return lista2

print(remove_duplicates([4, 5, 'a', 4, 6]))
print(remove_duplicates(['a', 'b', 'a']))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([]))
         
         
