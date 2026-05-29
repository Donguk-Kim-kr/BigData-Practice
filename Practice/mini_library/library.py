import pandas as pd
from datetime import date, timedelta

class Library:
    loan_number = 5001
    def __init__(self):
        self.books_df = pd.DataFrame({
            "book_id":[],
            "title":[],
            "author":[],
            "isbn":[],
            "publisher":[],
            "year":[],
            "total_qty":[],
            "available_qty":[]
        })
        
        self.loans_df = pd.DataFrame({
            "loan_id":[],
            "book_id":[],
            "member_id":[],
            "loan_date":[],
            "due_date":[],
            "return_date":[],
            "status":[]
            })

    def add_book(self, book):
        new_row = pd.DataFrame([{
        "book_id": book.book_id,
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "publisher": book.publisher,
        "year": book.year,
        "total_qty": book.total_qty,
        "available_qty": book.available_qty
    }])
        self.books_df = pd.concat([self.books_df, new_row], ignore_index=True)
        print(f"{book.title} 도서가 등록되었습니다. (도서 번호 : {book.book_id})")

    def process_loan(self, book_id, member_id):
        today = date.today()
        due = today + timedelta(days=14)
        new_row = pd.DataFrame({
        "loan_id":[Library.loan_number],
        "book_id":[book_id],
        "member_id":[member_id],
        "loan_date":[today],
        "due_date":[due],
        "return_date":[None],
        "status":["loaned"]
    })
        available = self.books_df.loc[self.books_df["book_id"] == book_id, "available_qty"].values[0]

        if available >= 1:
            self.books_df.loc[self.books_df["book_id"] == book_id, "available_qty"] -= 1
            Library.loan_number += 1
            self.loans_df = pd.concat([self.loans_df, new_row], ignore_index=True)
        else:
            print("해당 도서는 대출할 수 없습니다.")



    def process_return(self, loan_id):
        book_id = self.loans_df.loc[self.loans_df["loan_id"] == loan_id, "book_id"].values[0]
        self.loans_df.loc[self.loans_df["loan_id"] == loan_id, "return_date"] = date.today()
        self.loans_df.loc[self.loans_df["loan_id"] == loan_id, "status"] = "returned"
        self.books_df.loc[self.books_df["book_id"] == book_id, "available_qty"] += 1