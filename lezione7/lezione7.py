#Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
"""
print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
{'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([]))
{'pari': [], 'dispari': []}
"""


def classifica_numeri(lista: int) -> dict[str:list[int]]:
    numeri: dict={"pari": None, "dispari":None}
    pari=[]
    dispari=[]
    for i in lista:
        if i%2==0:
            pari.append(i)
        else:
            dispari.append(i)
    numeri["pari"]=pari
    numeri["dispari"]=dispari
    return numeri




#Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
"""
For example:
Test 	Result

print(somma_condizionale([1, 2, 3, 6, 12])) 18

print(somma_condizionale([5, 7, 11])) 0
"""
"""
def somma_condizionale(numeri: list[int]) -> int :
    divisibili=[]
    for i in numeri:
        if i%2==0 and i%3==0:
            divisibili.append(i)
    return sum(divisibili)
"""
import copy

#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
#print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) return--->[1, 3, 4]

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    lista2=[]
    pass
    # cancella pass e scrivi il tuo codice
    #for i,j in da_rimuovere.items():
        #if i in lista:
            
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))



    





        
#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

def aggrega_voti(registro: list[dict]) -> dict[str:list[int]]:
    nuovo_registro={}

    for studente in registro:
        nome=studente["nome"]
        voto=studente["voto"]

        if nome in nuovo_registro:
            nuovo_registro[nome].append(voto)
            print(nuovo_registro[nome])
        else:
            nuovo_registro[nome]=[voto]
   
    return nuovo_registro













def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    # cancella pass e scrivi il tuo codice
    prodotti_scontati=copy.deepcopy(prodotti)
    for i,j in prodotti.items():
        if j<20:
            prodotti_scontati.pop(i)
        else:
            prodotti_scontati[i]=(j*10)/100
    return prodotti_scontati

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
            
