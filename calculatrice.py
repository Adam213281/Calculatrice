import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erreur : division par zéro"
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result.set(add(num1, num2))
        elif operation == "Soustraction":
            result.set(subtract(num1, num2))
        elif operation == "Multiplication":
            result.set(multiply(num1, num2))
        elif operation == "Division":
            result.set(divide(num1, num2))
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")


root = tk.Tk()
root.title("Calculatrice")


operation_var = tk.StringVar(value="Addition")
result = tk.StringVar()


tk.Label(root, text="Premier nombre :").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Deuxième nombre :").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Opération :").grid(row=2, column=0)
tk.OptionMenu(root, operation_var, "Addition", "Soustraction", "Multiplication", "Division").grid(row=2, column=1)

tk.Button(root, text="Calculer", command=calculate).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Résultat :").grid(row=4, column=0)
tk.Entry(root, textvariable=result, state="readonly").grid(row=4, column=1)


tk.mainloop()
