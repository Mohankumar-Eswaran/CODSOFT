import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def animate_password_generation(password):
    result_label.config(text="")
    for i in range(len(password) + 1):
        partial_password = password[:i]
        result_label.config(text=f"Generated Password: {partial_password}")
        root.update_idletasks()
        root.after(25)

def on_generate():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer.")
            return
        password = generate_password(length)
        animate_password_generation(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#282c34")


style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), background="#61afef", foreground="#282c34")
style.configure("TLabel", font=("Helvetica", 12), background="#282c34", foreground="#abb2bf")


title_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), background="#282c34", foreground="#61afef")
title_label.pack(pady=10)

input_label = ttk.Label(root, text="Enter the desired length of the password:")
input_label.pack(pady=5)

entry = ttk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
