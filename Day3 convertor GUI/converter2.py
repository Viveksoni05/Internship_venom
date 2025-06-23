import tkinter as tk
from tkinter import ttk
import json


root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)

amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency_label_dropdown = ttk.Combobox(root, values=["USD","INR", "EUR", "GBP", "JPY", "AUD"])
from_currency_label_dropdown.pack(pady=5)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_label_dropdown = ttk.Combobox(root, values=["USD", "INR", "EUR", "GBP", "JPY", "AUD"])
to_currency_label_dropdown.pack(pady=5)

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_label_dropdown.get().upper()
        to_currency = to_currency_label_dropdown.get().upper()
        with open('exchange.json', 'r') as f:
            rates = json.load(f)
        if from_currency not in rates or to_currency not in rates:
            result_label.config(text="Invalid currency selected.")
            return
        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]
        result_label.config(text=f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Please enter a valid amount.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

convert_button = tk.Button(root, text="Convert", width=10, command=convert_currency)
convert_button.pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()