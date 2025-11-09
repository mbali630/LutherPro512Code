from datetime import datetime, date
from config import FINE_RATE  # Add this in config.py: FINE_RATE = 0.50

def calculate_fine(due_date_str, return_date_str=None):
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date() if return_date_str else date.today()

        if return_date > due_date:
            days_overdue = (return_date - due_date).days
            fine = days_overdue * FINE_RATE
            return round(fine, 2)
        return 0.0
    except ValueError:
        print("Invalid date format. Expected YYYY-MM-DD.")
        return 0.0

def format_date(date_obj):
    try:
        if isinstance(date_obj, str):
            return datetime.strptime(date_obj, "%Y-%m-%d").strftime("%B %d, %Y")
        return date_obj.strftime("%B %d, %Y")
    except Exception:
        return str(date_obj)

def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) == 10 and isbn.isdigit():
        return True
    elif len(isbn) == 13 and isbn.isdigit():
        return True
    return False