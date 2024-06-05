class Banca:

    def __init__(self, nome: str, simbolo: str) -> None:

        self.nome: str = nome
        self.simbolo: str = simbolo

class Filiale:

    def __init__(self, codice: str, indirizzo: str, banca: Banca)-> None:
        self.codice= codice
        self.indirizzo= indirizzo
        self.banca= banca

unicredit: Banca = Banca(nome="Unicredit", simbolo="UCG")
intesa: Banca = Banca(nome="Intesa San Paolo", simbolo="IST")
filiale_unicredit1: Filiale= Filiale(codice="UCG01", indirizzo="Via Sierra Nevada, RM", banca=unicredit)


        