import tkinter as tk
from tkinter import messagebox
from database.db_manager import add_member  # ✅ Integrate with DB

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Membership Registration Form")

        # Labels and Entries
        tk.Label(root, text="Member Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.member_number = tk.Entry(root)
        self.member_number.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="First Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.first_name = tk.Entry(root)
        self.first_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.last_name = tk.Entry(root)
        self.last_name.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Email:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.email = tk.Entry(root)
        self.email.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Phone:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.phone = tk.Entry(root)
        self.phone.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Address:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.address = tk.Entry(root)
        self.address.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(root, text="Membership Type:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.membership_type = tk.Entry(root)
        self.membership_type.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(root, text="Status:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.status = tk.Entry(root)
        self.status.grid(row=7, column=1, padx=10, pady=5)

        tk.Button(root, text="Register Member", command=self.register_member).grid(row=8, column=1, pady=10)

    def register_member(self):
        member_number = self.member_number.get().strip()
        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        email = self.email.get().strip()
        phone = self.phone.get().strip()
        address = self.address.get().strip()
        membership_type = self.membership_type.get().strip()
        status = self.status.get().strip() or "Active"

        if not all([member_number, first_name, last_name, email]):
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        try:
            add_member(member_number, first_name, last_name, email, phone, address, membership_type)
            messagebox.showinfo("Success", "Member registered successfully!")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to register member: {e}")

    def clear_form(self):
        for entry in [self.member_number, self.first_name, self.last_name, self.email, self.phone, self.address, self.membership_type, self.status]:
            entry.delete(0, tk.END)

# Run the form
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()