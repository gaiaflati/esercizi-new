"""
1. Classe Movie:

Attributi:

    movie_id: str - Identificatore di un film.
    title: str - Titolo del film.
    director: str - Regista del film.
    is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

Metodi:

    rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio 
    "Il film {self.title} è già noleggiato."
    return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False, 
    altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."

"""

class Movie:

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool) -> None:
        self.movie_id= movie_id
        self.title= title
        self.director= director
        self.is_rented= is_rented

    def rent(self):
        if self.is_rented:
            print(f"Il film {self.title} è già noleggiato")
        else:
            self.is_rented=True
        
    def return_movie(self):
        #pp
        if self.is_rented:
            self.is_rented=False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")
    

"""
    2. Classe Customer:

Attributi:

    customer_id: str - Identificativo del cliente.
    name: str - Nome del cliente.
    rented_movies: list[Movie] - Lista dei film noleggiati.

Metodi:

    rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, 
    altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
    return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, 
    altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."
"""

class Custumer:

    def __init__(self, costumer_id: str, name: str) -> None:
        self.costumer_id=costumer_id
        self.name= name
        self.rented_movies: list[Movie]=[]

    def rent_movie(self, movie: Movie):
        if movie not in self.rented_movies:
            self.rented_movies.append(movie)
            movie.rent()
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")

    def return_movie(self, movie: Movie):
        if movie not in self.rented_movies:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        else:
            self.rented_movies.remove(movie)
            movie.return_movie()
            return self.rented_movies

"""
3. Classe VideoRentalStore:

Attributi:

    movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
    customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

Metodi:

    add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, 
    altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
    register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, 
    altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
    rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, 
    altrimenti stampa il messaggio "Cliente o film non trovato."
    return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, 
    altrimenti stampa il messaggio "Cliente o film non trovato."
    get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) 
    se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
"""

class VideoRentalStore:

    def __init__(self) -> None:
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Custumer] = {}

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies.keys():
            self.movies[movie_id]=Movie(movie_id, title,director, is_rented=False)
        
        else:
            print(f"Il film con ID {movie_id} esiste già")
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers.keys():
            self.customers[customer_id]=Custumer(customer_id, name)
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")
    
    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers.keys() and movie_id in self.movies.keys():
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers.keys() and movie_id in self.movies.keys():
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print ("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        vuota=[]
        if customer_id in self.customers.keys():
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato.")
            return vuota
        


 	

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")


"""
Il film 'Inception' è già noleggiato.↩
Il film 'Inception' non è stato noleggiato da questo cliente.↩
Film noleggiati da Alice: []↩
Film noleggiati da Bob: ['The Matrix']
"""