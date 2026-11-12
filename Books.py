from datetime import datetime
import json


class Book:

    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.book = "Normal"
        Library.all_books.append(self)

    @property
    def age(self):
        return datetime.now().year - self.year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year > datetime.now().year:
            raise ValueError("Invalid year try again")
        self._year = year

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Invalid price try again")
        self._price = price

    def describe(self):
        print(f"Title: {self.title} \n Author: {self.author} \n Year: {self.year} \n Price: ${self.price} \n")

    def to_dict(self) -> dict:
        return {
            "type": self.book,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "price": self.price
        }

    def __repr__(self):
        return self.title



class FictionBook(Book):

    def __init__(self, title, author, year, price, theme):
        super().__init__(title, author, year, price)
        self.theme = theme
        self.book = "Fiction"

    def describe(self):
        print(f"Title: {self.title} \n Author: {self.author} \n Year: {self.year} \n Price: ${self.price} \n Theme:"
              f" {self.theme}")

    def to_dict(self):
        return {
            "type": self.book,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "price": self.price,
            "theme": self.theme
        }


class NonFictionBook(Book):

    def __init__(self, title, author, year, price, subject):
        super().__init__(title, author, year, price)
        self.subject = subject
        self.book = "NonFiction"

    def describe(self):
        print(f"Title: {self.title} \n Author: {self.author} \n Year: {self.year} \n Price: ${self.price} \n Theme:"
              f" {self.subject}")

    def to_dict(self):
        return {
            "type": self.book,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "price": self.price,
            "subject": self.subject
        }


class Library:

    all_books = []

    @property
    def total_value(self):
        return sum(item.price for item in Library.all_books)

    @staticmethod
    def from_string(data):
        if data["type"] == "Fiction":
            return FictionBook(data["title"], data["author"], int(data["year"]), float(data["price"]), data["theme"])
        elif data["type"] == "Nonfiction":
            return NonFictionBook(data["title"], data["author"], int(data["year"]), float(data["price"]), data["subject"])
        else:
            return Book(data["title"], data["author"], int(data["year"]), float(data["price"]))

    @classmethod
    def to_json(cls):
        return [book.to_dict() for book in cls.all_books]

    @classmethod
    def from_json(cls):
        with open("Books.JSON", 'r') as f:
            file_check = f.read()
            f.seek(0)
            if not file_check:
                print("File Empty")
                return
        data = json.loads(file_check)
        for item in data:
            cls.from_string(item)


















