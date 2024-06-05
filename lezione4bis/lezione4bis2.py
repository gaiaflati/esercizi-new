"""
    Data una strnga s che contiene parole e spazi,
    restituire la lunghezza dell'ultima parola in s
    Una parola è una sottostringa che contiene caratteri contigui
    diversi dallo spazio

    Esempio1: 
    s= "Hello World" -> restituisce 5
    spiegazione: l'ultima parola è world che ha lunghezza 5

    Esempio2:
    x= "fly me    to   the moon" -> restituisce 4
    spiegazione: l'ultima parola è moon che ha lunghezza 4
"""

def lenght_of_last_world(s: str):
    s_strip=s.strip()
    s_split=s_strip.split()
    print(len(s_split[-1]))
out=lenght_of_last_world("  CIAO    belli  ")