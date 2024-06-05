def anagram(s: str, t: str) -> bool:
    # scrivere qui il codice
    s_lower=s.lower()
    t_lower=t.lower()
    
    for i in s_lower:
        for i in t_lower:
            if i in t_lower and i in s_lower and len(s_lower)==len(t_lower):
                return True
            else:
                return False

"""
Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

"""

class Account:
    def __init__(self, account_id: str, balance: float ) -> None:
        self.account_id=account_id
        self.balance=balance
        self.amount: float=0
        

    
    def deposit(self, amount: float):
        if amount != 0:
            self.balance += amount
    
    def get_balance(self):
        return self.balance
    
class Bank:

    def __init__(self) -> None:
        self.accounts= {}
    
    def create_account(self, account_id: Account):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        self.accounts[account_id] = Account(account_id)
        
        

    def deposit(self, account_id: Account, amount):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        self.accounts[account_id].deposit(amount)
        return amount
    

    def get_balance(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id].get_balance()

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

"""

def word_break(s: str, wordDict: list[str]) -> bool:
    pass
    for i in wordDict:
        if i in s and wordDict.count(i)==1:
            return True
        else:
            return False
        


def valid_sudoku(board: list[list[str]]) -> bool:
    for i in board:
        if "9" not in i[0][3][4][5][6] and "9" in i[1][2][7][8]:
            return True
        else:
            return False
"""

"""
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Methodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

"""




class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val=val
        
def reverse_list(head: ListNode) :
    reversed_list: list[int]= []
    queue: list[ListNode] = [head]
    while queue:
        curr_node = queue.pop(0)
        if curr_node:
            reversed_list.append(curr_node.val)
            queue.append(curr_node.next)
    return reversed_list[::-1]



def valid_sudoku(board: list[list[str]]) -> bool:
    rows: dict[int, list[int]] = {i: [] for i in range(9)}
    # rows =  {0: [],1: [], ... ,8: []}
    cols: dict[int,list[int]] = {i: [] for i in range(9)}
    squares: dict[int,list[int]] = {i: [] for i in range(9)}
    
    for i in range(9):
        for j in range(9):
            curr_elem: str= board[i][j]
            if curr_elem != '.':
                square_i, square_j = i//3, j//3
                square_index= 3*square_i + square_j

                if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[square_index]:
                    return False
                
                rows[i].append(curr_elem)
                cols[j].append(curr_elem)

#square_i= 0, square_j=0 -> 0
#square_i= 0, square_j=1 -> 1
#square_i= 0, square_j=2 -> 2
#square_i= 1, square_j=0 -> 3
#square_i= 1, square_j=1 -> 4
#square_i= 1, square_j=2 -> 5
#square_i= 2, square_j=0 -> 6
#square_i= 2, square_j=1 -> 7

#square_i= 2, square_j=2 -> 8



"""
def binary_to_dec(x: str):
    x: list[str] = list(x)
    # x-> ["1","0","1","1"]

    num: int = 0
    for i in range(len(x)):
        num += int(x[i]) * 2**(len(x)-i-1)
    return num

print(binary_to_dec("10"))
"""

