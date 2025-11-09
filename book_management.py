import tkinter as tk
from tkinter import messagebox
from api.openlibrary_api import fetch_book_by_isbn_openlib
from database.db_manager import add_book

class BookManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # ISBN
        tk.Label(self, text="ISBN:").grid(row=0, column=0, padx=10, pady=10)
        self.isbn_entry = tk.Entry(self)
        self.isbn_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self, text="Fetch Details", command=self.fetch_details).grid(row=0, column=2, padx=10, pady=10)

        # Title
        tk.Label(self, text="Title:").grid(row=1, column=0)
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=1, column=1)

        # Author
        tk.Label(self, text="Author:").grid(row=2, column=0)
        self.author_entry = tk.Entry(self)
        self.author_entry.grid(row=2, column=1)

        # Publisher
        tk.Label(self, text="Publisher:").grid(row=3, column=0)
        self.publisher_entry = tk.Entry(self)
        self.publisher_entry.grid(row=3, column=1)

        # Year
        tk.Label(self, text="Year:").grid(row=4, column=0)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=4, column=1)

        # Pages
        tk.Label(self, text="Pages:").grid(row=5, column=0)
        self.pages_entry = tk.Entry(self)
        self.pages_entry.grid(row=5, column=1)

        # Language
        tk.Label(self, text="Language:").grid(row=6, column=0)
        self.language_entry = tk.Entry(self)
        self.language_entry.grid(row=6, column=1)

        # Category
        tk.Label(self, text="Category:").grid(row=7, column=0)
        self.category_entry = tk.Entry(self)
        self.category_entry.grid(row=7, column=1)

        # Description (use Text for multi-line)
        tk.Label(self, text="Description:").grid(row=8, column=0)
        self.description_entry = tk.Text(self, height=4, width=30)
        self.description_entry.grid(row=8, column=1)

        # Shelf Location
        tk.Label(self, text="Shelf Location:").grid(row=9, column=0)
        self.shelf_entry = tk.Entry(self)
        self.shelf_entry.grid(row=9, column=1)

        # Total Copies
        tk.Label(self, text="Total Copies:").grid(row=10, column=0)
        self.total_copies_entry = tk.Entry(self)
        self.total_copies_entry.grid(row=10, column=1)

        # Save Button
        tk.Button(self, text="Save Book", command=self.save_book).grid(row=11, column=1, pady=20)

    def fetch_details(self):
        isbn = self.isbn_entry.get().strip()
        if not isbn:
            messagebox.showerror("Error", "Please enter an ISBN.")
            return

        book_info = fetch_book_by_isbn_openlib(isbn)
        if book_info:
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, book_info["title"])

            self.author_entry.delete(0, tk.END)
            self.author_entry.insert(0, book_info["author"])

            self.publisher_entry.delete(0, tk.END)
            self.publisher_entry.insert(0, book_info["publisher"])

            self.year_entry.delete(0, tk.END)
            self.year_entry.insert(0, book_info["publication_year"] or "")

            self.pages_entry.delete(0, tk.END)
            self.pages_entry.insert(0, book_info["page_count"])

            self.language_entry.delete(0, tk.END)
            self.language_entry.insert(0, book_info["language"])

            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, book_info["category"])

            self.description_entry.delete("1.0", tk.END)
            self.description_entry.insert(tk.END, book_info["description"])
        else:
            messagebox.showerror("Error", "Book details not found.")

    def save_book(self):
        isbn = self.isbn_entry.get().strip()
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        publisher = self.publisher_entry.get().strip()
        year = self.year_entry.get().strip()
        pages = self.pages_entry.get().strip()
        language = self.language_entry.get().strip()
        category = self.category_entry.get().strip()
        description = self.description_entry.get("1.0", tk.END).strip()
        shelf = self.shelf_entry.get().strip()
        total_copies = self.total_copies_entry.get().strip()

        if not isbn or not title:
            messagebox.showerror("Error", "ISBN and Title are required.")
            return

        # Validate numeric fields
        try:
            year = int(year) if year else None
            pages = int(pages) if pages else 0
            total_copies = int(total_copies) if total_copies else 1
        except ValueError:
            messagebox.showerror("Error", "Year, Pages, and Total Copies must be numbers.")
            return

        try:
            add_book(isbn, title, author, publisher, year, category, description,
                     f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg",
                     pages, language, total_copies, shelf)
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save book: {e}")

    def clear_fields(self):
        for entry in [self.isbn_entry, self.title_entry, self.author_entry, self.publisher_entry,
                      self.year_entry, self.pages_entry, self.language_entry, self.category_entry,
                      self.shelf_entry, self.total_copies_entry]:
            entry.delete(0, tk.END)
        self.description_entry.delete("1.0", tk.END)