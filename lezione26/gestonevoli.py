

"""
Si vuole progettare un sistema in Python per la gestione delle prenotazioni aeree. Il sistema dovrà gestire diverse tipologie di voli, tra cui voli commerciali e voli charter.
 
Classe astratta Volo:
Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di volo, come il codice del volo (stringa) e 
la capacità massima di posti disponibili sul volo (numero intero) che sono attributi passati come argomenti in input. 
Inoltre, la classe deve avere un attributo chiamato prenotazioni, il quale non deve essere passato come argomento del costruttore; 
il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
 
Metodi:

    si definisca il metodo astratto prenota_posto().
    si definisca il metodo astratto posti_disponibili().
"""


from abc import ABC, abstractmethod

class AbcVolo(ABC):

    @abstractmethod

    def __init__(self, codice: str, capacità_max: int) -> None:
        self.codice= codice
        self.capacità_max = capacità_max
        self.prenotazioni= 0

    @abstractmethod
    
    def prenota_posto(self):
        pass
    
    @abstractmethod

    def posti_disponibili(self):
        pass
        



"""
Classe VoloCommerciale:
Estende la classe Volo e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. I
l costruttore deve inoltre gestire i seguenti attributi interi: posti_economica, posti_business, e posti_prima; i quali consentono di stabilire 
quanti posti sono stati riservati alla classe economica, quanti alla classe business e quanti alla prima classe su ogni volo. 
Il costruttore non deve ricevere in input questi argomenti, ma assegnare loro un valore iniziale tale che la somma di questi tre valori interi
 sia uguale al numero dei posti disponibili sul volo. Si può pensare di riservare il 70% dei posti alla classe economica, il 20% dei posti alla classe business 
 ed i restanti posti alla prima classe. Inoltre, il costruttore deve creare tre valori interi pari a 0, chiamati prenotazioni_economica, prenotazioni_business, 
 prenotazioni_prima.
 

 prenota_posto(posti, classe_servizio): che consente di prenotare un certo numero di posti sul volo in una determinata classe. 
    Tale metodo, prima di riservare un posto, deve controllare prima che ci siano posti disponibili sull'intero volo, poi se ci sono posti disponibili nella classe richiesta.
    In caso affermativo, contare il numero dei posti prenotati in tale classe. Inoltre, nel caso in cui sia possibile prenotare un posto, 
    il metodo deve stampare a schermo un messaggio che notifichi all'utente di aver riservato un tot di posti per una determinata classe su un dato volo 
    (specificando il codice del volo). In caso contrario, stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella classe scelta. 
    Se sul volo non ci sono più posti disponibili, il metodo deve stampare a schermo un messaggio notificando all'utente che il volo è al completo. 
    Inoltre, se la classe passata come input del metodo non risulta essere una delle seguenti classi ("economica", "business", "prima"), 
    il metodo deve stamapre a schermo un messaggio di errore, notificando all'utente che la classe richiesta non è valida. 
    Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di prenotazioni ricevute per ogni classe di servizio,
    poi aggiornare gli attributi prenotazioni_economica, prenotazioni_business, prenotazioni_prima con l'esatto numero delle prenotaioni ricevute per ogni classe di servizio.
    Suggerimento: introdurre delle variabili locali d'appoggio per gestire le prenotazioni per ogni classe di servizio da azzerare all'inizio di ogni fase di prenotazione.



    posti_disponibili(): che ritorna un dizionario in cui vengono salvati il numero di posti disponibili totali sul volo nel seguente modo: 
    il dizionario deve avere quattro chiavi, ovvero, 'posti disponibili', 'classe economica', 'classe business', 'prima classe'. Alla chiave 'posti disponibili' 
    associare come rispettivo valore il numero di posti disponibili rimasti sul volo, alla chiave 'classe economica' associare come rispettivo valore il numero di 
    posti che sono rimasti disponibili nella classe economica, alla chiave 'classe business' associare come rispettivo valore il numero di posti che sono rimasti 
    disponibili nella classe business, alla chiave 'prima classe' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella prima classe. 
    Se i posti disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore da associare alla corrispondete chiave è 0.

"""



class VoloCommerciale(AbcVolo):

    def __init__(self, codice: str, capacità_max: int) -> None:
        super().__init__(codice, capacità_max)
    
        self.posti_economica= capacità_max*70/100
        self.posti_businness= capacità_max*20/100
        self.posti_prima= capacità_max*10/100
        self.prenotazioni_economica = 0 
        self.prenotazioni_business = 0 
        self.prenotazioni_prima = 0
    
    
    def prenota_posto(self, posti, classe_servizio):
        if self.prenotazioni < self.capacità_max:

            if classe_servizio!= "economica" and classe_servizio!= "business" and classe_servizio!= "prima":
                print ("Classe inesistente")

            if classe_servizio=="economica" and self.prenotazioni_economica< self.posti_economica and posti<= self.posti_economica-self.prenotazioni_economica:
                self.prenotazioni_economica+=posti
                self.prenotazioni+=posti
                print(f"Congratulazioni! hai riservato {posti} posti in classe {classe_servizio}  sul volo {self.codice}")
            else:
                print(f"Non ci sono piu posti nella classe scelta")
            
            if classe_servizio=="business" and self.prenotazioni_business< self.posti_businness and posti<= self.posti_businness-self.prenotazioni_business:
                self.prenotazioni_business+=posti
                self.prenotazioni+=posti
                print(f"Congratulazioni! hai riservato {posti} posti in classe {classe_servizio}  sul volo {self.codice}")
            else:
                print(f"Non ci sono piu posti nella classe scelta")

            if classe_servizio=="prima" and self.prenotazioni_prima< self.posti_prima and posti<= self.posti_prima-self.prenotazioni_prima:
                self.prenotazioni_prima+=posti
                self.prenotazioni+=posti
                print(f"Congratulazioni! hai riservato {posti} posti in classe {classe_servizio}  sul volo {self.codice}")
            else:
                print(f"Non ci sono piu posti nella classe scelta")
        
        else:
            print(f"posti esauriti sul volo {self.codice}")
            pass
            
    def posti_disponibili(self):
        
        posti_disponibili=self.capacità_max- self.prenotazioni
        classe_economica= self.posti_economica- self.prenotazioni_economica
        classe_prima= self.posti_prima- self.prenotazioni_prima
        classe_business= self.posti_businness- self.prenotazioni_business
        disponibili: dict={"posti disponibili": posti_disponibili, "classe economica": classe_economica, "classe business": classe_business, "prima classe": classe_prima}

     

    
"""
 posti_disponibili(): che ritorna un dizionario in cui vengono salvati il numero di posti disponibili totali sul volo nel seguente modo: 
    il dizionario deve avere quattro chiavi, ovvero, 'posti disponibili', 'classe economica', 'classe business', 'prima classe'. Alla chiave 'posti disponibili' 
    associare come rispettivo valore il numero di posti disponibili rimasti sul volo, alla chiave 'classe economica' associare come rispettivo valore il numero di 
    posti che sono rimasti disponibili nella classe economica, alla chiave 'classe business' associare come rispettivo valore il numero di posti che sono rimasti 
    disponibili nella classe business, alla chiave 'prima classe' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella prima classe. 
    Se i posti disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore da associare alla corrispondete chiave è 0.
"""

    