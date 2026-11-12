from Books import Book, FictionBook, NonFictionBook, Library
import json

lib = Library()


def get_int():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Enter valid number")


def add_book():
    typebook = input("What book type: ")
    title = input("\nTitle: ")
    author = input("\nAuthor: ")
    year = int(input("\nYear: "))
    price = float(input("\nPrice: "))

    if typebook == "fiction":
        theme = input("theme: ")
        FictionBook(title, author, year, price, theme)
    elif typebook == "nonfiction":
        subject = input("subject: ")
        NonFictionBook(title, author, year, price, subject)
    else:
        Book(title, author, year, price)


    #On startup load data
Library.from_json()


while True:
    print("1: Add book")
    print("2: Find book")
    print("3: Show books")
    print("4: Remove book")
    print("5: Sort books")
    print("6: Show value ")
    print("7: Exit")

    choice = get_int()

    match choice:
        case 1:
            add_book()
        case 2:
            book_type = input("What book type are you looking for?: ")
            if book_type.lower() == "fiction":
                mylist = [book.title for book in Library.all_books if book.book == "Fiction"]

                for index, item in enumerate(mylist, start=1):
                    print(f"Book {index}: {item}")
            elif book_type.lower() == "nonfiction":
                mylist1 = [book.title for book in Library.all_books if book.book == "NonFiction"]
                for index, item in enumerate(mylist1, start=1):
                    print(f"Book {index}: {item}")

        case 3:
            for index, books in enumerate(Library.all_books, start= 1):
                print(f"Book {index}: {books.title}")

        case 4:
            found = False
            book_removed = input("What book would you like to remove: ")
            for book in Library.all_books:
                if book.title.lower() == book_removed.lower():
                    Library.all_books.remove(book)
                    found = True
            if not found:
                print("Book not found")

        case 5:
            print("On what would you like to sort:")
            print("1: Price")
            print("2: Theme")
            print("3: Author")

            sort_theme = get_int()
            if sort_theme == 1:
                print("1: High to low")
                print("2: Low to high")
                high_or_low = get_int()
                if high_or_low == 1:
                    sorted_books = sorted(Library.all_books, key=lambda book: book.price, reverse=True)
                    for book in sorted_books:
                        print(book.title, book.price)
                elif high_or_low == 2:
                    sorted_books = sorted(Library.all_books, key=lambda book: book.price)
                    for book in sorted_books:
                        print(book.title, book.price)
                else:
                    break
            elif sort_theme == 2:
                subject_theme = input("What theme: ")
                print(book.title for book in Library.all_books if book.theme == subject_theme or book.subject == subject_theme)
            elif sort_theme == 3:
                author_sort = input("What author: ")
                print(book.title for book in Library.all_books if author_sort == book.author)

        case 6:
            print(f"Libraries total value: ${lib.total_value}")

        case 7:
            data = Library.to_json()
            with open("Books.JSON", 'w') as f:
                json.dump(data, f, indent=2)
            break
        case _:
            continue



