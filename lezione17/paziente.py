
### CLASSE: Paziente
"""
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
"""

from lezione17.persona import Persona


class Paziente(Persona):

    def __init__(self, _first_name: str, _last_name: str, _idCode: str) -> None:
        super().__init__(_first_name, _last_name)
        self._idCode=_idCode

    def setIdCode(self, idCode): #consente di impostare il codice identificativo del paziente.
        if type(idCode) != str:
            return "l'Id code non è una stringa"
        else:
            self._idCode=idCode
    
    def getidCode(self):
        return self._idCode
    
    def patientInfo(self):
        print (f"Paziente: {self._first_name} {self._last_name} \n ID: {self._idCode}")
