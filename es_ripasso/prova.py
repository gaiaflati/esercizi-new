"""
class Book:
    def __init__(self,book_id:str,title:str,author:str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed :bool= False
    
    def borrow(self):
        if  not self.is_borrowed:
            self.is_borrowed = True

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False

class Member:
    def __init__(self,member_id:str,name:str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books :list[Book]= []

    def borrow_book(self,book:Book):
        if book not in self.borrowed_books and book.is_borrowed==False:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("Book is already borrowed")

    def return_book(self,book:Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print("Book not borrowed by this member")

class Library:
    def __init__(self) -> None:
        self.books:dict[str,Book]={}
        self.members :dict[str:Member] = {}
    
    def add_book(self,book_id: str, title: str, author: str):
        if book_id not in self.books.keys():
            book = Book(book_id,title,author)
            self.books[book_id] = book
    
    def register_member(self,member_id: str, name: str):
        if member_id not in self.members.keys():
            member = Member(member_id,name)
            self.members[member_id] = member

    def borrow_book(self,member_id: str, book_id: str):
        if member_id not in self.members.keys():
            print("Member not found")
        elif not book_id in self.books.keys():
            print("Book not found")
        else:
            member:Member = self.members[member_id]
            book :Book = self.books[book_id]
            member.borrow_book(book)
    
    
    def return_book(self,member_id: str, book_id: str):

        if member_id in self.members.keys() and book_id in self.books.keys():
            book:Book = self.books[book_id]
            member :Member= self.members[member_id]
            member.return_book(book)
            
    def get_borrowed_books(self,member_id: str)->list[Book]:
        lista=[]
        if member_id in self.members.keys():
            for i in self.members[member_id].borrowed_books:
              lista.append(i.title)
        return lista
"""

"""

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
"""

class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float):
        if amount !=0:
            self.balance+=amount
        else:
            self.balance= 0

    def get_balance(self):
        if self.balance != 0:
            return self.balance
        else:
            return 0


"""
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""

class Bank:

    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}
    
    def create_account(self, account_id):
        if account_id not in self.accounts.keys():
            self.accounts[account_id]=Account(account_id, 0)
            return self.accounts[account_id]
        else:
            print ("Account gia esistente")

    def deposit(self, account_id, amount):
        if account_id in self.accounts.keys():
            self.accounts[account_id].deposit(amount)

    def get_balance(self,account_id): 
        if account_id in self.accounts.keys():
            return self.accounts[account_id].get_balance()

 	

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))