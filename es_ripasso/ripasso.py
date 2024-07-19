#LEZIONE 5


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


#LEZIONE 7

"""
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

For example:

print(classifica_numeri([1, 2, 3, 4, 5, 6])) 

	

{'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([]))

	

{'pari': [], 'dispari': []}

"""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    pari_dispari={}
    pari=[]
    dispari=[]
    for i in lista:
        if i%2 == 0:
            pari.append(i)
        else:
            dispari.append(i)
    pari_dispari["pari"]= pari
    pari_dispari["dispari"]= dispari
    return pari_dispari

print(classifica_numeri([1, 2, 3, 4, 5, 6]))
print(classifica_numeri([2, 4, 6, 8, 10]))
print(classifica_numeri([]))
print(classifica_numeri([1, 3, 5]))
print(classifica_numeri([0, 1, -2, 3, -4]))


"""
Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.

For example:

print(somma_condizionale([1, 2, 3, 6, 12]))     18

print(somma_condizionale([5, 7, 11]))   0         
"""

def somma_condizionale(numeri: list[int]) -> int :
    divisibili=[]
    for i in numeri:
        if i%2 ==0 and i%3==0:
            divisibili.append(i)
    
    return sum(divisibili)

print(somma_condizionale([1, 2, 3, 6, 12]))     
print(somma_condizionale([5, 7, 11])) 



"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi 
e il numero di volte che devono essere rimossi come valori.

For example:

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))        [1, 3, 4]

print(rimuovi_elementi([], {2: 1}))             []
"""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for i in lista:
        
        if i in da_rimuovere.keys() and da_rimuovere[i]>0:
            lista.remove(i)
            da_rimuovere[i]-=1
    return lista

        
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) 
print(rimuovi_elementi([], {2: 1}))   
print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))

"""

Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

For example:

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))  {'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([]))   {}

"""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    new_dict={}
    for i in voti:
        if i['nome'] not in new_dict.keys():
            new_dict[i["nome"]]=[i["voto"]]
        else:
            new_dict[i["nome"]].append(i['voto'])
    return new_dict
        


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])) 

        
    

    
"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti 
che hanno un prezzo superiore a 20, scontati del 10%.
For example:

Test	Result
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
{}
"""


def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    newprod={}
    for i,j in prodotti.items():
        if j>20:
            newprod[i]=j-(j*10/100)
    return newprod

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))	
print(filtra_e_mappa({'Tavolo': 120.0, 'Sedia': 85.0}))
print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))

    


"""
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare,
 e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

esempio:
contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

{'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
{'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}

"""


def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    dictionary={"name": name, "email": email, "telefono": telefono}
    return dictionary


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    dictionary["name"]=name 
    if email!= None:
        dictionary["email"]= email
    if telefono!= None:
        dictionary["telefono"]= telefono
    return dictionary
        
    


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))


"""
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo).
L'accesso è consentito solo se il nome utente è admin", la password corrisponde a "12345" e l'account è attivo, 
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
For example:
print(check_access ("admin",
"12345", True))
print (check_access ("admin", "54321", True))
Accesso consentito
Accesso negato
"""

def check_access(username: str, password: int, is_active: bool) -> str:
    if (username=="admin") and (password== 12345) and is_active:
        return "Accesso consentito"
    else:
        return "Accesso negato"

print(check_access ("admin", "12345", True))
print(check_access ("admin", "54321", True))

"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando 
tutte le lettere originali esattamente una volta.

For example:

Test	Result
print(anagram("anagram","nagaram"))
True

"""

def anagram(s: str, t: str) -> bool:
    s_lower=s.lower()
    t_lower=t.lower()
    for i in s_lower:
        if i in t_lower and len(s)==len(t):
            return True
        else:
            return False

print(anagram("anagram","nagaram"))




