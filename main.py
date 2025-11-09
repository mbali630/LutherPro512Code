from gui.main_window import LibraryApp
import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))
from database.db_manager import initialize_database

initialize_database()  # Ensure tables exist
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()