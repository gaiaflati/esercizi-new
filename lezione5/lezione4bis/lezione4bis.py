def is_palindrome(x: int): 
    """
        dato un intero x, restituisce True se x è plindromo
        e False altrimenti

        esempio1:
        x=121 -> True
        spiegazione:121 si legge 121 sia da destra che da sinistra

        esempio2:
        x=-121 ->False
        spiegazione: se lo ruoti non si legge allo stesso modo

        esempio3:
        x=10-> False
        siegazione: se lo ruoto è 01, non è palindromo 
    """
def is_palindrome(x: int):
    x=str(x)
    if x == ''.join(reversed(x)):
        print(True)
    else:
        print (False)
out=is_palindrome(121)
