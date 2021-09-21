from mongoengine import *

db_connection = connect('app-yaotingj')
db_connection.drop_database('app-yaotingj')

class Book(Document):
   book_id = StringField(max_length=18)
   title = StringField(max_length=100)
   author = StringField(max_length=18)
   checked_out = StringField(default="N")
   borrower_id = StringField(default="")
   borrower_name = StringField(default="")


def add_books():
   book1 = Book(book_id="A234", title="The 101 Dalmations", author="Dodie Smith")
   book2 = Book(book_id="A675", title="The Adventures of Huckleberry Finn", author="Mark Twain")
   book3 = Book(book_id="A212", title="Bag of Bones", author="Stephen King")
   book4 = Book(book_id="B671", title="Charlie and the Chocolate Factory", author="Roald Dahl")
   book5 = Book(book_id="B534", title="Charlotte's Web", author="E.B.White")
   book6 = Book(book_id="B777", title="A Christmas Carol", author="Charles Dickens")
   book7 = Book(book_id="B778", title="Dracula", author="Bram Stoker")
   book8 = Book(book_id="B812", title="A Farewell to Arms", author="Ernest Hemingway")
   book9 = Book(book_id="C101", title="The Firm", author="John Grisham")

   book1.save()
   book2.save()
   book3.save()
   book4.save()
   book5.save()
   book6.save()
   book7.save()
   book8.save()
   book9.save()


class Borrower(Document):
   borrower_id = StringField(max_length=3)
   name = StringField(max_length=18)
   phone = StringField(max_length=12)

def add_borrowers():
   borrower1 = Borrower(borrower_id="L34", name="Andrea Selleck", phone="639-555-1239")
   borrower2 = Borrower(borrower_id="L22", name="Lucas Hyatt", phone="408-555-2365")
   borrower3 = Borrower(borrower_id="L19", name="Carol Leonard", phone="650-555-8921")
   borrower4 = Borrower(borrower_id="L84", name="Ayesha Ford", phone="415-555-2120")
   borrower5 = Borrower(borrower_id="L77", name="Kenneth Trout", phone="510-555-1982")

   borrower1.save()
   borrower2.save()
   borrower3.save()
   borrower4.save()
   borrower5.save()

