
"""
Classe Book:

    Attributi:
        book_id: str - Identificatore di un libro.
        title: str - titolo del libro.
        author: str - autore del libro
        is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
    Metodi:
        borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
        return_book()- Contrassegna il libro come restituito.
"""

class Book:

    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool ) -> None:
        self.book_id= book_id
        self.title= title
        self.author= author
        self.is_borrowed= is_borrowed

    def borrow(self):
        if self.is_borrowed==False:
            self.is_borrowed= True  

    def return_book(self):
        if self.is_borrowed==True:
            self.is_borrowed= False


"""
Classe Member:

    Attributi:
        member_id: str - identificativo del membro.
        name: str - il nome del membro.
        borrowed_books: list[Book] - lista dei libri presi in prestito.
    Metodi:
        borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
        return_book(book): rimuove il libro dalla lista borrowed_books.
"""

class Member:

    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book]= []

    def borrow_book(self, book: Book):
        if book not in self.borrowed_books and book.is_borrowed==False:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("Book is already borrowed")
    
    def return_book(self, book:Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print("Book is not borrowed by this member")
    
    
"""
Classe Library:

    Attributi:
        books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
        members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
    Metodi:
        add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
        register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
        borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
        return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
        get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
    """

class Library:

    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books.keys():
            self.books[book_id]=Book(book_id, title, author, False)
        else:
            print("Book is already in the library")
    
    def register_member(self, member_id:str, name: str):
        if member_id not in self.members.keys():
            self.members[member_id]=Member(member_id, name)
        else:
            print("Mmeber is already registred")
        
    def borrow_book(self, member_id: str, book_id: str):
        if member_id not in self.members.keys():
            print("Member not found")
        elif book_id not in self.books.keys():
            print("Book not found")
        else:
            self.members[member_id].borrow_book(self.books[book_id])
    
    def return_book(self, member_id: str, book_id: str):
        if member_id not in self.members.keys():
            print("Member not found")
        elif book_id not in self.books.keys():
            print("Book not found")
        
        else:
            self.members[member_id].return_book(self.books[book_id])
    
     
    def get_borrowed_books(self, member_id)-> list[Book]:
        lista=[]
        for i in self.members[member_id].borrowed_books:
            lista.append(i.title)
        return lista

    

