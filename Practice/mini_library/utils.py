from datetime import date, timedelta

def validate_isbn(isbn:str):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    else:
        print("ISBN이 유효하지 않습니다.")
        return False
    
def calc_due_date(loan_date:date):
    return loan_date + timedelta(days=14)

def calc_overdue(due_date:date):
    diff = date.today() - due_date
    if diff.days > 0:
        return diff.days
    else:
        return 0