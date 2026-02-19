class Book:
    def __init__(self,book_id,title):
        self.book_id=book_id
        self.title=title
        self.is_issued=False

class Student:
    def __init__(self,sid,name):
        self.sid=sid
        self.name=name
        self.issued_books=[]

class Library:
    def __init__(self):
        self.books={}

    def add_book(self,book):
        self.books[book.book_id]=book
        print("success")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed")
        else:
            print("Book not found")

    def display_books(self):
        if not self.books:
            print("No books available")
            return

        for book_id, book in self.books.items():
            if book.is_issued == True:
                status = "Issued"
            else:
                status = "Available"

            print(f"ID:{book_id}, Title:{book.title}, Status:{status}")
    
    def search_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            print(book.book_id, book.title, book.is_issued)
        else:
            print("Book not found")

    def issue_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_issued:
                book.is_issued = True
                print("Issued")
            else:
                print("Already issued")
        else:
            print("Book not found")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]

            if book.is_issued == True:
                book.is_issued = False
                print("Book returned successfully")
            else:
                print("Book was not issued")
        else:
            print("Book not found")

lib=Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        book = Book(book_id, title)
        lib.add_book(book)

    elif choice == "2":
        lib.display_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID to issue: "))
        lib.issue_book(book_id)

    elif choice == "4":
        book_id = int(input("Enter Book ID to return: "))
        lib.return_book(book_id)

    elif choice == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice")


        

        



'''
class Library:
    def __init__(self):
        self.books=["python","java script","java"]

    def display_choice(self):
        print("1.add book\n2.remove book\n3.show book\n4.exit")

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        self.books.remove(book)

    def show_books(self):
        return self.books
    


lib=Library()

try:
    while True:
        lib.display_choice()
        choice=int(input("choice:"))
        if choice==1:
            bname=input("enter book name:")
            lib.add_book(bname)
            print(f"{bname} added")
        elif choice==2:
            bname=input("enter book name:")
            lib.remove_book(bname)
            print(f"{bname} removed")
        elif choice==3:
            print(lib.show_books())
        elif choice==4:
            break
        else:
            print("invalid choice")
    
except Exception as e:
    print(e)
'''