
from lezione17.persona import Persona

### CLASSE: Dottore
"""
Creare un file chiamato "dottore.py".
In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa 
(ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcella per le visite in studio (si usi il tipo float). 
Gli attributi della classe dottore devono essere anch'essi privati.

- Definire i seguenti metodi:
costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel). 
Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, altrimenti assegna None all'attributo che non verifica 
la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".
setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. 
Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore,
ad esempio "La specializzazione inserita non è una stringa!".
setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. 
Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, 
ad esempio "La parcella inserita non è un float!".
getSpecialization(): consente di ritornare la specializzazione del dottore.
getParcel(): consente di ritornare la parcella del dottore.
isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, 
in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido.
 In caso contrario, stampare "Doctor nome e cognome is not valid!".
doctorGreet():tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specializzazione}"

"""

class Dottore(Persona):

    def __init__(self, _first_name: str, _last_name: str, _specialization: str, _parcel: float) -> None:
        super().__init__(_first_name, _last_name)
        self._specialization = _specialization
        self._parcel = _parcel
        if type(self._specialization) != str:
            self._specialization= None
            return "La specializzazione inserita non è una stringa!"
        elif type(self._parcel) != float:
            self._parcel = None
            return "La parcella inserita non è un float!"
    
    def setSpecialization(self, specialization):
        if type(specialization) == str:
            self._specialization=specialization
        else:
            return "La specializzazione inserita non è una stringa!"
        
    def setParcel(self, parcel):
        if type(parcel) == str:
            self._parcel=parcel
        else:
            return "La parcella inserita non è un float!"
        
    def getSpecialization(self): #consente di ritornare la specializzazione del dottore.
        return self._specialization
    
    def getParcel(self): #consente di ritornare la parcella del dottore.
        return self._parcel

    def isAValidDoctor(self):  
                                                                                         #stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni,
        if self._age >= 30:
            return f"Doctor {self._first_name} {self._first_name} is Valid!"  
                                                                                            #in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!
        else:
            return f"Doctor {self._first_name} {self._first_name} is not Valid!" 
                                                                                   # ", se il dottore risulta valido. In caso contrario, stampare "Doctor nome e cognome is not valid!".
    


    def doctorGreet(self):  
        self.greet()
        print(f"Sono un medico {self._specialization}")            #tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto 
                                                                    #"Sono un medico {specializzazione}"
    

