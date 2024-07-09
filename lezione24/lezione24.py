
# Testi Digitali

#Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
#Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. 
#Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.


class Documento:

    def __init__(self, text: str) -> None:
        self.text= text

    def getText(self):
        return self.text

    def setText(self, text):
        if type(text)== str:
            self.text=text
    
    def isInText(self, key: str):
        if key in self.text:
            return True
        else:
            return False





#Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
#Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
#Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
#Da: alice@example.com, A: bob@example.com
#Titolo: Incontro
#Messaggio: Ciao Bob, possiamo incontrarci domani?
 
#Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.



class Email(Documento):

    def __init__(self, text: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(text)
         
        self.mittente=mittente
        self.destinatario=destinatario
        self.titolo=titolo
    
    def setMittente(self, mittente):
        if type(mittente)== str:
            self.mittente=mittente
    
    def getMittente(self):
        return self.mittente

    def setDestinatario(self, destinatario):
        if type(destinatario)== str:
            self.destinatario=destinatario
    
    def getDestinatario(self):
        return self.destinatario
    
    def setTitolo(self, titolo):
        if type(titolo)== str:
            self.titolo=titolo
    
    def getTitolo(self):
        return self.titolo
    
    def getText(self):
        print (f"Da: {self.mittente}, A: {self.destinatario}")
        print (f"Titolo: {self.titolo}")
        print (f"Messaggio: {self.text}")


 
#Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
#Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
#I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e 
#memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
#Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
#Percorso: nomePercorso/document.txt
#Contenuto: Questo e' il contenuto del file.

class File(Documento):

    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.nomePercorso: str= "lezione24/"


    def leggiTestoDaFile(self):

        with open(f"document.txt", "w") as reader:
            reader.write("Questo e' il contenuto del file.")
            self.text=reader.read()
    
    def getText(self):
        print(f"Percorso: {self.nomePercorso}")
        print(f"Contenuto: {self.text}")

doc1= Documento("ciao bella")
file1= File("Ciao core")
file1.leggiTestoDaFile()
        

   
        

