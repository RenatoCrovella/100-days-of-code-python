import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    c_data = response.json()

    if from_currency.upper() in c_data["rates"]:
        rate = c_data["rates"][to_currency.upper()]
        converted = amount * rate
        return converted
    else:
        raise ValueError("The currency wasn't found.")

input_amount = float(input("Type the value to be converted: "))
from_input = input("From (i.e: USD): ")
to_input = input("To (i.e: EUR): ")

try:
    result = convert_currency(input_amount, from_input, to_input)
    print(f"{input_amount:.2f} {from_input.upper()} = {result:.2f} {to_input.upper()}")
except Exception as e:
    print("Error:", e)
