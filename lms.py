from main import Book, Borrower

def get_borrower_name(borrowerID):
    for borrower in Borrower.objects:
        if borrower.borrower_id == borrowerID:
            return borrower.name

def get_book_name(bookID):
    for book in Book.objects:
        if book.book_id == bookID:
            return book.author

def checkout_book(borrowerID, bookID):
    for b in Book.objects:
        if b.book_id == bookID and b.checked_out == "Y" and b.borrower_id != borrowerID:
            print(get_book_name(bookID), "is already checked out by someone")
        elif b.book_id == bookID and b.checked_out == "":
            b.checked_out = "Y"
            b.borrower_id=borrowerID
            b.borrower_name=get_borrower_name(borrowerID)
            #TODO update DB
            b.save()
    print(get_borrower_name(borrowerID), 'has checked out ', get_book_name(bookID))

def return_book(borrowerID, bookID):
    for b in Book.objects:
        if b.book_id == bookID and b.checked_out == "" and b.borrower_id != borrowerID :
            # TODO
            # What should be the initial value of checked_out
            print(get_borrower_name(b.borrower_id), 'has not currently checked out', get_book_name(bookID))
        elif b.book_id == bookID and b.checked_out == "Y" and b.borrower_id == borrowerID:
            b.checked_out =""
            b.borrower_id=""
            b.borrower_name=""
            #TODO update DB
            b.save()
            print(get_borrower_name(borrowerID), 'has returned ', get_book_name(bookID))

def reset_db():
    for book in Book.objects:
        book.checked_out = ""
        book.borrower_id = ""
        book.borrower_name = ""
        #TODO update DB
        book.save()

if __name__ == "__main__":

    while True:
        action = input('Enter a command: ')

        if action == "checkout a book" or action == "return a book":
            borrower_id = input("Enter Borrower Id: ")
            book_id = input("Enter Book Id: ")

            is_bookid_valid = any(book.book_id == book_id for book in Book.objects)
            is_borrowerid_valid = any(borrower.borrower_id == borrower_id for borrower in Borrower.objects)

            print('test', is_bookid_valid)
            print('test 2', is_borrowerid_valid)

            # checkout a book
            if action == "checkout a book":
                if not is_bookid_valid:
                    print('Book with ID ', book_id, ' does not exist')
                elif not is_borrowerid_valid:
                    print('Borrower with ID', borrower_id, ' does not exist')
                else:
                    checkout_book(borrower_id, book_id)

            # return a book
            if action == "return a book":
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
            for b in Book.objects:
                print(b.book_id,",", b.title,",", b.author,",", b.checked_out,",", b.borrower_id,",", b.borrower_name)

        # exit
        elif action == "exit":
            print('Exiting')
            exit()

        # invalid request
        else:
            print("invalid request, please enter a valid request")
            continue