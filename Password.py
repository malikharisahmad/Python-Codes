import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def show_password():
    password = password_var.get()
    if password:
        messagebox.showinfo("Generated Password", f"Your Password: {password}\n\nCopy it manually.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.config(bg="#222")

password_var = tk.StringVar()

tk.Label(root, text="Enter Password Length:", fg="white", bg="#222").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=5)
tk.Entry(root, textvariable=password_var, width=30, state="readonly").pack(pady=5)
tk.Button(root, text="Show Password", command=show_password, bg="blue", fg="white").pack(pady=5)

root.mainloop()
