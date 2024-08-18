import tkinter as tk
from tkinter import messagebox
import re

# Create a dictionary to store contacts
contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    if not re.match(r'^\d{10}$', phone):  # Assuming 10-digit phone number format
        messagebox.showerror("Error", "Phone number must be exactly 10 digits!")
        return

    # Email field is no longer validated
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
    else:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        update_contact_list()
        clear_entries()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['Phone']}")

def search_contact():
    search_term = search_entry.get()
    results = [name for name in contacts if search_term.lower() in name.lower() or search_term in contacts[name]['Phone']]
    
    contact_list.delete(0, tk.END)
    if results:
        for name in results:
            contact_list.insert(tk.END, f"{name}: {contacts[name]['Phone']}")
    else:
        messagebox.showinfo("Search", "No contacts found")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(':')[0]
        del contacts[name]
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Select a contact to delete")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def update_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(':')[0]
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        
        if not phone:
            messagebox.showerror("Error", "Phone is required!")
            return
        
        if not re.match(r'^\d{10}$', phone):  # Assuming 10-digit phone number format
            messagebox.showerror("Error", "Phone number must be exactly 10 digits!")
            return
        
        # Email field is no longer validated
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Select a contact to update")

def on_select(event):
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(':')[0]
        details = contacts[name]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, details['Phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, details['Email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, details['Address'])

def validate_phone_input(new_value):
    return new_value.isdigit() or new_value == ""

# Create main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("600x400")
root.minsize(400, 300)  # Set a minimum size for the window
root.configure(bg="#e0f7fa")

# Register validation commands
validate_phone = root.register(validate_phone_input)

# Create input fields
tk.Label(root, text="Name:", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=10, sticky="e")
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w", columnspan=2)

tk.Label(root, text="Phone:", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=10, sticky="e")
phone_entry = tk.Entry(root, font=("Arial", 12), validate="key", validatecommand=(validate_phone, '%P'))
phone_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w", columnspan=2)

tk.Label(root, text="Email:", bg="#e0f7fa", font=("Arial", 12)).grid(row=2, column=0, pady=5, padx=10, sticky="e")
email_entry = tk.Entry(root, font=("Arial", 12))  # Removed validation command
email_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w", columnspan=2)

tk.Label(root, text="Address:", bg="#e0f7fa", font=("Arial", 12)).grid(row=3, column=0, pady=5, padx=10, sticky="e")
address_entry = tk.Entry(root, font=("Arial", 12))
address_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w", columnspan=2)

# Create buttons
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.grid(row=4, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

tk.Button(button_frame, text="Add Contact", command=add_contact, bg="#4caf50", fg="white", font=("Arial", 12), width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Contact", command=update_contact, bg="#2196f3", fg="white", font=("Arial", 12), width=15).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white", font=("Arial", 12), width=15).grid(row=0, column=2, padx=5)

# Create search field
search_frame = tk.Frame(root, bg="#e0f7fa")
search_frame.grid(row=5, column=0, columnspan=3, pady=5, padx=10, sticky="nsew")

tk.Label(search_frame, text="Search:", bg="#e0f7fa", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_contact, bg="#9e9e9e", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

# Create contact list
contact_list = tk.Listbox(root, font=("Arial", 12), width=75, height=10)
contact_list.grid(row=6, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")
contact_list.bind('<<ListboxSelect>>', on_select)  # Bind selection event

# Configure row and column weights for dynamic resizing
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Run the application
root.mainloop()
