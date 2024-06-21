# 1. GESTIONALE PAGAMENTO

# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro

# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro

# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456

# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321
 

# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi
#  get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. 
# Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00".
#  Quando viene stampato, l'importo è sempre con 2 cifre decimali.



class Pagamento:

    def __init__(self) -> None:
        pass

    def setImporto(self, _importo: float):
       self.importo=_importo

    def getImporto(self):
        return self.importo
    
    def dettagliPagamento(self):
        return f"Importo del pagamento: {round(self.importo, 2)}"
    

# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro 
# e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()
    
    def setImporto(self, _importo: float):
        return super().setImporto(_importo)
    
    def dettagliPagamento(self):
        return f"Pagamento in contanti di: {round(self.importo, 2)}"
    
    def inPezziDa(self):
        pezzi_banconote=[500.00, 200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.01]
        for i in pezzi_banconote:
            if self.importo//i != 0:
                if i >= 5:
                    print(f"{self.importo//i} banconote da {i}") 
                    self.importo = self.importo %i
                else:
                    print(f"{self.importo//i} monete da {i}") 
                    self.importo = self.importo%i

# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. 
# Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome_titolare: str, scadenza: str, numero_carta: int) -> None:
        super().__init__()
        self.nome_titolare=nome_titolare
        self.scadenza=scadenza
        self.numero_carta= numero_carta

    def dettagliPagamento(self):
        return f"Pagamento di: {self.importo} effettuato con la carta di credito \n Nome sulla carta: {self.nome_titolare} \n Data di scadenza: {self.scadenza} \n Numero della carta: {self.numero_carta}"

        


                
    
# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() 
# per ognuno di essi.

contanti_1=PagamentoContanti()
contanti_2= PagamentoContanti()

credito_1=PagamentoCartaDiCredito(nome_titolare="Mario Rossi", scadenza="06/24", numero_carta=80056782789)
credito_2=PagamentoCartaDiCredito(nome_titolare="Gaia Flati", scadenza="05/32", numero_carta=38409809801)

contanti_1.setImporto(150)
contanti_2.setImporto(95.25)
print(contanti_1.dettagliPagamento())
contanti_1.inPezziDa()
print(contanti_2.dettagliPagamento())
contanti_2.inPezziDa()

credito_1.setImporto(500.00)
credito_2.setImporto(200.00)
print(credito_1.dettagliPagamento())
print(credito_2.dettagliPagamento())




    