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

    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
        
        else:
            return "Libro già preso in prestito"
    
    def return_book(self):

        if self.is_borrowed == True:
            self.is_borrowed= False
        
        else:
            return "Libro non in prestito"

        
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

    def __init__(self, member_id: str, name: str, borrowed_books: list[Book]) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self, book: Book):
        if book.is_borrowed == False and book not in self.borrowed_books:
            self.borrowed_books.append(book)
            book.borrow()
            return self.borrowed_books
        elif book.is_borrowed== True:
            return "Book is already"
    
    def return_book(self, book: Book):
        if book in self.borrowed_books and book.borrow():
            self.borrowed_books.remove(book)
            return self.borrowed_books
        else:
            return "Book not borrowed by this member"
        

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

    def __init__(self)-> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books.keys():
            self.books[book_id]=Book(book_id=book_id, title=title,author=author, is_borrowed=False)
    
    def register_member(self, member_id:str, name: str):
        if member_id not in self.members.keys():
            self.members[member_id]=Member(member_id=member_id, name=name, borrowed_books=[])
    
    def borrow_book(self, member_id: str, book_id: str):
        if book_id in self.books and member_id in self.members and self.books[book_id].is_borrowed==False:
            self.members[member_id].borrow_book(self.books[book_id])
            return self.members[member_id].borrowed_books
        elif 
    
    def return_book(self, member_id: str, book_id: str):
        self.members[member_id].return_book(self.books[book_id])
        return self.members[member_id].borrowed_books
    
    def get_borrowed_books(self, member_id): 
        prestati=[]
        for i in self.members[member_id].borrowed_books:
            prestati.append(i.title)
        return prestati
        


library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))
print(library.get_borrowed_books("M002"))

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

	


