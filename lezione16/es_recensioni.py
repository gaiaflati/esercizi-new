"""
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film.
 Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, 
il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni 
e richiami il metodo recensione().
"""

class Media:
    
    def __init__(self, title: str) -> None:
        self.title=title
        self.reviews: list[int] =[]

    def set_title(self, title: str):
        self.title=title

    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto):
        if 1<= voto <=5:
            self.reviews.append(voto)
        else:
            return "Voto non valido. Deve essere compreso tra 1 e 5"
    
    def getMedia(self):
        media = sum(self.reviews)/ len(self.reviews)
        return media
    
    
    def getRate(self):
        media=self.getMedia()
        if 0 <= media <= 1:
            return "Giudizio: Terribile"
        elif 1 < media <= 2:
            return "Giudizio: Brutto"
        elif 2 < media <= 3:
            return "Giudizio: Normale"
        elif 3 < media <= 4:
            return "Giudizio: Bello"
        elif 4 < media <= 5:
            return "Giudizio: Grandioso"
    
    def ratePercentage(self, voto):
        conta=self.reviews.count(voto)
        percentuale=conta*100/len(self.reviews)
        return  percentuale
    
    def recensione(self):
        print (f" Titolo del film: {self.title} \n Voto Medio = {self.getMedia()} \n {self.getRate()} \n Terribile: {self.ratePercentage(1)} \n Brutto: {self.ratePercentage(2)} \n Normale: {self.ratePercentage(3)} \n Bello: {self.ratePercentage(4)}  \n Grandioso: {self.ratePercentage(5)}. ")
        
        
        

class Film(Media):

    def __init__(self, title: str) -> None:
        super().__init__(title)
        pass




film_1=Film("Avatar")
film_2=Film("Interstellar")

film_1.aggiungiValutazione(3)
film_1.aggiungiValutazione(4)
film_1.aggiungiValutazione(1)
film_1.aggiungiValutazione(1)
film_1.aggiungiValutazione(2)
film_1.aggiungiValutazione(5)
film_1.aggiungiValutazione(2)
film_1.aggiungiValutazione(2)
film_1.aggiungiValutazione(4)
film_1.aggiungiValutazione(2)
print(film_1.getMedia())
print(film_1.getRate())
print(film_1.ratePercentage(3))

print(film_1.recensione())

"""

Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.


"""

class Contatore:

    def __init__(self) -> None:
        self.conteggio=0

    def setZero(self):
        self.conteggio=0
    
    def add1(self):
        self.conteggio+=1
    
    def sub1(self):
        if self.conteggio==0:
            print ("Non è possibile eseguire la sottrazione")
        else:
            self.conteggio-=1
            if self.conteggio<0:
                self.conteggio=0
    
    def get(self):
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")



