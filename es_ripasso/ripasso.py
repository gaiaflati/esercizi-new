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
         

#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
#For example:

#print(sum_above_threshold([15, 5, 25], 20))  25

def sum_above_threshold(numbers: list[int], threshold) -> int:
    # prima cancella ... e definisci parametro e tipo per il dato mancante
    # successivamente cancella pass e scrivi il tuo codice
    somma=[]
    for i in numbers:
         if i > threshold:
              somma.append(i)
    return sum(somma)

print(sum_above_threshold([1, 10, 20, 30], 10))
print(sum_above_threshold([15, 5, 25], 20))
print(sum_above_threshold([3, 5, 8], 10))
print(sum_above_threshold([50, 60, 70], 25))
print(sum_above_threshold([2, 5, 1], 1))



#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". 
#Un numero magico è definito come un numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:
     
    num= str(num)
    if "7" in num:
        return True
    else:
        return False

print(is_magic_number(70))
print(is_magic_number(123))
print(is_magic_number(1729))
print(is_magic_number(250))


"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale 
viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni 
sia maggiore della lunghezza della lista.

For example

print(rotate_left([1, 2, 3, 4, 5], 2))

[3, 4, 5, 1, 2]

"""

def rotate_left(elements: list, k: int) -> list:
    if k<= len(elements):
        slice_elements=elements[k: len(elements)]+elements[:k]

    else:
        slice_elements= elements[k-len(elements):len(elements)]+ elements[:k-len(elements)]
    
    return slice_elements

print(rotate_left([1, 2, 3, 4, 5], 2))
print(rotate_left([1, 2, 3, 4, 5], 1))
print(rotate_left([1, 2, 3, 4, 5], 5))
print(rotate_left([1, 2, 3, 4, 5], 8))
print(rotate_left(['a', 'b', 'c', 'd'], 3))



#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre 
#c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:

    check = [0,0]

    for i in expression:
        if i=="(":
            check[0]+=1
        elif i==")" and (check[0]>check[1]):
            check[1]+=1
    if check[0]==check[1]:
        return True
    else:
        return False
    
print(check_parentheses("()()"))
print(check_parentheses("(()))("))
print(check_parentheses("((()))"))
print(check_parentheses(")("))
print(check_parentheses("(())"))



#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

#For example:


#print(count_isolated([1, 2, 2, 3, 3, 3, 4]))    2
#print(count_isolated([1, 2, 3, 4, 5]))        5

def count_isolated(numbers: list) -> int:
    count=[]
    for i in numbers:
        a=(numbers.index(i)+1)
        b=(numbers.index(i)-1)


        if b<0 and i!= numbers[a]:
            count.append(i)
        elif a>=len(numbers) and i!=numbers[b]:
            count.append(i)
        elif (b>=0 and a<=len(numbers)) and (i!=numbers[b] and i!=numbers[a]):
            count.append(i)
    print(count)
    return len(count)

 	

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 1, 2, 2, 3, 4, 4]))
print(count_isolated([1, 2, 3, 4, 5]))



#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

#For example:

#print(remove_elements({5, 6, 7}, [7, 8, 9]))     {5, 6}


def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    check=[]
    for i in original_set:
        if i not in elements_to_remove:
            check.append(i)
    check=set(check)
    return check


print(remove_elements({1, 2, 3, 4}, [2, 3]))
print(remove_elements({5, 6, 7}, [7, 8, 9]))
print(remove_elements({1, 2}, [3]))
print(remove_elements(set(), [1, 2, 3]))
print(remove_elements({10, 20, 30}, []))


#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

#print(merge_dictionaries({'x': 5}, {'x': -5}))    {'x': 0}

#print(merge_dictionaries({}, {'a': 10, 'b': 20}))   {'a': 10, 'b': 20}

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
   
    for keys in dict2:
        if keys in dict1:
            dict1[keys]=dict1[keys]+dict2[keys]
            
        else:
            dict1[keys]=dict2[keys]
        
    return dict1
        
 	

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))









