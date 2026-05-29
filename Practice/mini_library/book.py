import pandas as pd

class Book:
    book_number = 1001
    def __init__(self, title, author, isbn, publisher, year, total_qty, available_qty):
        self.book_id = Book.book_number
        Book.book_number += 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.total_qty = total_qty
        self.available_qty = available_qty

    def loan(self):
        if self.available_qty >= 1:
            self.available_qty -= 1
        else:
            print("해당 도서는 대출할 수 없습니다.")

    def return_book(self):
        self.available_qty += 1
    
    def display_info(self):
        print(f"도서 번호 : {self.book_id}\n도서명 : {self.title}\n저자 : {self.author}\nISBN : {self.isbn}\n출판사 : {self.publisher}\n출판연도 : {self.year}\n총 권수 : {self.total_qty}\n현재 대출 가능 권수 : {self.available_qty}")
    
    @classmethod
    def create_from_input(cls):
        title = input("도서명 : ")
        author = input("저자 : ")
        isbn = input("ISBN : ")
        publisher = input("출판사 : ")
        year = input("출판연도 : ")
        total_qty = input("총 권수 : ")
        available_qty = input("현재 대출 가능 권수 : ")
        return cls(title, author, isbn, publisher, year, total_qty, available_qty)

    @classmethod
    def from_series(cls, series):
        return cls(series["title"], series["author"], series["isbn"], series["publisher"], series["year"], series["total_qty"], series["available_qty"])