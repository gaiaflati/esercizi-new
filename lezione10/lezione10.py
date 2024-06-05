"""
from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso():

        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome= nome 

    def verso(self):
        return print("Bau!")
    
cane__1: Cane = Cane(nome="Pluto")
cane__1.verso()

class Gatto(AbcAnimal):
    
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome=nome
    
    def verso(self):
        return print("Miao!")

gatto: Gatto= Gatto(nme="micio")
gatto.verso()


class ContoBancario:

    total_accounts=0

    def __init__(self, iban, saldo, nome) -> None:
        self.iban= iban
        self.saldo= saldo
        self.nome= nome

        ContoBancario.total_accounts += 1
    
    def deposito(self, importo):
        self.saldo += importo
        print(f"{importo} depositato. il nuovo saldo è {self.saldo}")
    
    def prelievo(self, importo):
        self.saldo -= importo
        print(f"{importo} prelevato. il nuovo saldo è {self.saldo}")

    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")

    @classmethod
    def get_type(cls):
        print(f"type: {cls.definizione}")

    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        
account1= ContoBancario(123456789, 0, "Alice")
account2= ContoBancario(9876543210, 1000, "Bob")

account1.deposito(500)
account2.prelievo(200)

ContoBancario.get_total_accounts()
"""




#Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione.
#Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
#Classi:
# Film: Rappresenta un film con titolo e durata.
 
# Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

#Metodi:
# prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
# posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
# Cinema: Gestisce le operazioni legate alla gestione delle sale.

#Metodi:
#aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
# prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

#Test case:

#Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
# Un cliente sceglie un film e prenota un certo numero di posti.
#Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, titolo: str, durata: int) -> None:
        self.titolo=titolo
        self.durata=durata

class Sala:
    def __init__(self, numero_sala: int, film: Film, posti_totali: int) -> None:
        self.numero_sala= numero_sala
        self.film= film
        self.posti_totali=posti_totali
        self.posti_prenotati=0
        self.disponibili=posti_totali
    
    def prenota_posti(self, num_posti): 
        if self.posti_prenotati<self.posti_totali and ((self.posti_totali-self.posti_prenotati)> num_posti):
            self.posti_prenotati+=num_posti
        else:
            return "Non ci sono posti disponibili"

    
    def posti_disponibili(self):
        if self.posti_prenotati==self.posti_totali:
            return "Non ci sono più posti disponibili"
        else:
            self.disponibili=self.posti_totali - self.posti_prenotati
            return self.disponibili
    

class Cinema:
    def __init__(self, sala: Sala, film: Film) -> None:
        self.sala=sala
        self.film=film
        self.sale: list[Sala] = []
    
    def aggiungi_sala(self, sala: Sala):
        if sala  and isinstance (sala, Sala) and sala not in self.sale:
            self.sale.append(sala)
           

    def prenota_film(self, titolo_film: str, num_posti):
        if titolo_film == self.film.titolo:
            self.sala.prenota_posti(num_posti)
            return f"posti prenotati: {num_posti}, buona visione"
        else:
            return "Film non in programmazione"
        
cartone: Film= Film(titolo="nemo", durata=160)
sala_1: Sala= Sala(numero_sala=21,film=cartone, posti_totali=23)
lucciola: Cinema=Cinema(sala=sala_1, film=cartone)

film1 = Film("Matrix", 120)
sala1 = Sala(1, film1, 100)
cinema = Cinema(sala1,film1) 
cinema.aggiungi_sala(sala1)
print(cinema.prenota_film("Matrix", 10))  
print(cinema.prenota_film("Matrix", 95))  
print(cinema.prenota_film("Inception", 10))




#Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
#cercare prodotti per nome e verificare la disponibilità di un prodotto.

#Definisci una classe Prodotto con i seguenti attributi:
# nome (stringa)
# quantità (intero)
 
#Definisci una classe Magazzino con i seguenti metodi:
# aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 #Test case:
    #Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    #Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    #Il sistema verifica la disponibilità dei prodotti in inventario.

class Prodotto:
    def __init__(self, nome: str, quantità: int) -> None:
        self.nome=nome
        self.quantità=quantità

class Magazzino:
    def __init__(self, prodotto: Prodotto) -> None:
        self.prodotto=prodotto
        self.prodotti: list[Prodotto]= []
    
    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto and isinstance (prodotto, Prodotto) and prodotto not in self.prodotti:
            self.prodotti.append(prodotto)
            prodotto.quantità+=1
            return self.prodotti

    def cerca_prodotto(self, nome: str):
        for i in self.prodotti:
            if nome==i.nome:
                return nome
        else:
            return "prodotto non nel magazzino"

    def verifica_disponibilità(self, nome: str):
        for i in self.prodotti:
            if i.nome==nome:
                return "prodotto disponibile"
            
            else:
                return "prodotto non disponibile"

prodotto1=Prodotto("fagioli", 2)
prodotto2=Prodotto("ceci", 1)
Magazzino1=Magazzino(prodotto1)
print(Magazzino1.aggiungi_prodotto(prodotto2))
print(Magazzino1.cerca_prodotto("ceci"))
print(Magazzino1.verifica_disponibilità('ceci'))



#Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
#Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

#Classe:
# MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

#Metodi:
# add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record.
# Se il regista esiste, la sua lista di film viene aggiornata.

# remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#list_directors(): Elenca tutti i registi presenti nel catalogo.

# get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

# search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
#Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.


class MovieCatalog:
    
    def __init__(self, director_name: str, ) -> None:
        pass

    def add_movie(self, director_name: str, movies: int):
        pass

    def remove_movie(self, director_name, movie_name):
        pass

    def list_directors(self):
        pass

    def get_movies_by_director(self, director_name):
        pass

    def search_movies_by_title(self, title):
        pass


