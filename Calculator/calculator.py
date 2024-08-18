import tkinter as tk
from tkinter import messagebox
import time

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            messagebox.showerror("Invalid Operation", "Please enter a valid operation (+, -, *, /)")
            return
        
        label_result.config(text=f"Result: {result}")
        animate_result()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed")

def animate_result():
    for i in range(3):
        label_result.config(fg='red')
        app.update()
        time.sleep(0.1)
        label_result.config(fg='black')
        app.update()
        time.sleep(0.1)

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Add background color
app.configure(bg='lightblue')

# Create and place the widgets
label_num1 = tk.Label(app, text="Enter first number:", bg='lightblue', fg='black', font=('Arial', 12))
label_num1.pack(pady=5)

entry_num1 = tk.Entry(app, font=('Arial', 12))
entry_num1.pack(pady=5)

label_num2 = tk.Label(app, text="Enter second number:", bg='lightblue', fg='black', font=('Arial', 12))
label_num2.pack(pady=5)

entry_num2 = tk.Entry(app, font=('Arial', 12))
entry_num2.pack(pady=5)

label_operation = tk.Label(app, text="Enter operation (+, -, *, /):", bg='lightblue', fg='black', font=('Arial', 12))
label_operation.pack(pady=5)

entry_operation = tk.Entry(app, font=('Arial', 12))
entry_operation.pack(pady=5)

button_calculate = tk.Button(app, text="Calculate", command=perform_calculation, bg='green', fg='white', font=('Arial', 12, 'bold'))
button_calculate.pack(pady=10)

label_result = tk.Label(app, text="Result: ", bg='lightblue', fg='black', font=('Arial', 14))
label_result.pack(pady=10)

# Run the main application loop
app.mainloop()
