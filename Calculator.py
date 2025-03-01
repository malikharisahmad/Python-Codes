import tkinter as tk
from tkinter import messagebox

# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

# Function to handle calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        operations = {
            "Addition": add,
            "Subtraction": subtract,
            "Multiplication": multiply,
            "Division": divide
        }

        if operation in operations:
            result = operations[operation](num1, num2)
            label_result.config(text=f"Result: {result}")
        else:
            messagebox.showerror("Error", "Please select a valid operation.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Enter second number:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Dropdown menu for operations
tk.Label(root, text="Select Operation:").pack()
operation_var = tk.StringVar()
operation_var.set("Addition")  # Default selection
operations_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operations_menu.pack()

# Calculate button
btn_calculate = tk.Button(root, text="Calculate", command=calculate)
btn_calculate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Run the main event loop
root.mainloop()
