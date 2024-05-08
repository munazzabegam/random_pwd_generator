import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from password_generator import generate_password

def generate_password_clicked():
    try:
        length = int(length_entry.get())
        use_special_chars = special_chars_var.get()
        
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6 characters.")
        else:
            password = generate_password(length, use_special_chars)
            password_entry.configure(state='normal')
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            password_entry.configure(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Invalid input for password length.")

root = tk.Tk()
root.title("Password Generator")

length_label = ttk.Label(root, text="Enter the length of the password:")
length_entry = ttk.Entry(root, width=10)
special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_clicked)
password_label = ttk.Label(root, text="Your generated password:")
password_entry = ttk.Entry(root, width=30, state="readonly")

length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
length_entry.grid(row=0, column=1, padx=5, pady=5)
special_chars_checkbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
password_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
password_entry.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
