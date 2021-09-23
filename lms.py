from main import Book, Borrower, add_books, add_borrowers
from mongoengine import *


default_db_name = 'app-yaotingj'

def reset_db():
    disconnect(alias="default")
    newdb_connection = connect(default_db_name)
    newdb_connection.drop_database(default_db_name)
    add_books()
    add_borrowers()


def get_borrower_name(borrowerID):
    for borrower in Borrower.objects:
        if borrower.borrower_id == borrowerID:
            return borrower.name

def get_book_name(bookID):
    for book in Book.objects:
        if book.book_id == bookID:
            return book.title

def checkout_book(borrowerID, bookID):
    for b in Book.objects:
        if b.book_id == bookID and b.checked_out == "Y" and b.borrower_id != borrowerID:
            print(get_book_name(bookID), "is already checked out by someone")
        elif b.book_id == bookID and b.checked_out == "N":
            b.checked_out = "Y"
            b.borrower_id=borrowerID
            b.borrower_name=get_borrower_name(borrowerID)
            b.save()
    print(get_borrower_name(borrowerID), 'has checked out', get_book_name(bookID))

def return_book(borrowerID, bookID):
    for b in Book.objects:
        if b.book_id == bookID and b.checked_out == "N" and b.borrower_id != borrowerID :
            print(get_borrower_name(b.borrower_id), 'has not currently checked out', get_book_name(bookID))
        elif b.book_id == bookID and b.checked_out == "Y" and b.borrower_id == borrowerID:
            b.checked_out = "N"
            b.borrower_id = ""
            b.borrower_name = ""
            b.save()
            print(get_borrower_name(borrowerID), 'has returned ', get_book_name(bookID))

def get_books():
    book_list = []
    headers = ['book_id', 'title', 'author', 'checked_out', 'borrower_id', 'borrower_name']

    for b in Book.objects:
        book_list.append([f'"{b.book_id}"', f'"{b.title}"', f'"{b.author}"', f'"{b.checked_out}"',
                          f'"{b.borrower_id}"', f'"{b.borrower_name}"'])

    row_formatter ="{:>40}" * (len(headers))
    print(row_formatter.format(*headers))
    for row in book_list:
        print(row_formatter.format(*row))



if __name__ == "__main__":

    newdb = input('Enter a database name: ')
    if newdb == "":
        add_books()
        add_borrowers()
        print(default_db_name, 'is connected')
    else:
        default_db_name = newdb

    while True:
        action = input('Enter a command: ')

        if action == "checkout" or action == "return":
            borrower_id = input("Enter Borrower Id: ")
            book_id = input("Enter Book Id: ")

            is_bookid_valid = any(book.book_id == book_id for book in Book.objects)
            is_borrowerid_valid = any(borrower.borrower_id == borrower_id for borrower in Borrower.objects)

            # checkout a book
            if action == "checkout":
                if not is_bookid_valid:
                    print('Book with ID ', book_id, 'does not exist')
                elif not is_borrowerid_valid:
                    print('Borrower with ID', borrower_id, 'does not exist')
                else:
                    checkout_book(borrower_id, book_id)

            # return a book
            if action == "return":
                if not is_bookid_valid:
                    print('Book with ID ', book_id, ' does not exist')
                elif not is_borrowerid_valid:
                    print('Borrower with ID', borrower_id, ' is not a valid borrower')
                else:
                    return_book(borrower_id, book_id)

        # reset DB
        elif action == "reset":
            reset_db()
            print('Data has been reset')

        # print books
        elif action == "books":
            get_books()

        # exit
        elif action == "exit":
            print('Exiting')
            exit()

        # invalid request
        else:
            print("invalid command, please enter a valid command")
            continue