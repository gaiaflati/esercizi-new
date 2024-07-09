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

"""
 Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti.
Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

Classe:
- RecipeManager: Gestisce tutte le operazioni legate alle ricette.
Metodi:
create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore 
se l'ingrediente esiste già o la ricetta non esiste.
remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata.
 Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
list_recipes(): Elenca tutte le ricette esistenti.
list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta.
 Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
 Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

"""

class RecipeManager:

    def __init__(self) -> None:
        self.recipe: dict={}

    def create_recipe(self, name: str, ingredients: list):
        if name in self. recipe:
            return "Ricetta già presente"
        self.recipe[name]=ingredients
        return self.recipe
        
    
    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipe:
            return "Ricetta inesistente"
        elif recipe_name in self.recipe and ingredient not in self.recipe[recipe_name]:
            self.recipe[recipe_name].append(ingredient)
            return self.recipe
        else:
            return "Ingrediente già presente nella ricetta"
        

    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipe and ingredient in self.recipe[recipe_name]:
            self.recipe[recipe_name].remove(ingredient)
            return self.recipe
        elif recipe_name in self.recipe and ingredient not in self.recipe[recipe_name]:
            return "Ingrediente non presente"
        else: 
            return "Ricetta inesistente"

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name in self.recipe and old_ingredient in self.recipe[recipe_name]:
            self.recipe[recipe_name].remove(old_ingredient)
            self.recipe[recipe_name].append(new_ingredient)
            return self.recipe    
        elif recipe_name in self.recipe and old_ingredient not in self.recipe[recipe_name]:
            return "Ingrediente non presente"
        else: 
            return "Ricetta inesistente"

    def list_recipes(self):
        for i in self.recipe.keys():
            return i

    def list_ingredients(self,recipe_name):
        if recipe_name in self.recipe:
            return self.recipe.get(recipe_name)
        else:
            return "Ricetta inesistente"
             
            

    def search_recipe_by_ingredient(self, ingredient):
        recipes_ingredients=[]
        for i in self.recipe.items:
            if ingredient in i:
                recipes_ingredients.append(self.recipe.keys)    
            else:
                return f"nessuna ricetta contiene l'ingrediente: {ingredient}"
        return recipes_ingredients



manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))


"""
In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.

1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:
marca (stringa)
modello (stringa)
anno (intero)
Metodi:
__init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".
2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
numero_porte (intero)
Metodi:
__init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, 
nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".
3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)
Metodi:
__init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, 
nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".
"""

class Veicolo:

    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca=marca
        self.modello=modello
        self.anno=anno

    def descrivi_veicolo(self): 
        return f"Marca: [{self.marca}], Modello: [{self.modello}], Anno: [{self.anno}]"
    
class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte= numero_porte
    
    def descrivi_veicolo(self):
        return f"Marca: [{self.marca}], Modello: [{self.modello}], Anno: [{self.anno}], Numero di porte: [{self.numero_porte}]"
    
    
class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo=tipo
    
    def descrivi_veicolo(self): 
        return f"Marca: [{self.marca}], Modello: [{self.modello}], Tipo: [{self.tipo}]"