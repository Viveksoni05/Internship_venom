import json

def load_exchange_rates(file_path='exchange.json'):
    try:
        with open(file_path, 'r') as file:
            exchange_rates = json.load(file)
        return exchange_rates
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError(f"Currency not supported: {from_currency} or {to_currency}")

    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]


rates = load_exchange_rates()
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()


converted_amount = convert_currency(amount, from_currency, to_currency, rates)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")