# Currency Convertor using freecurrencyapi

import freecurrencyapi
from list_of_all_currencies import return_curr_list
from api_key import api_string

api_key = api_string()

client = freecurrencyapi.Client(api_key)
list_of_currencies = return_curr_list()


def convert_inputs(convert_from: str, convert_amount: float, convert_to: str):
    result = client.latest(base_currency=f"{convert_from}", currencies=[f"{convert_to}"])
    conversion = float(convert_amount) * float(result["data"][f"{convert_to}"])
    print(f"{convert_amount} {convert_from} is {conversion:.2f} {convert_to}")


def main() -> None:
    convert_from_valid = False
    convert_amount_valid = False
    convert_to_valid = False
    convert_from = ""
    convert_amount = None
    convert_to = ""

    while not convert_from_valid:
        convert_from: str = input("What currency would you like to convert from?")
        if convert_from in list_of_currencies:
            convert_from_valid = True
        else:
            print("ERROR! This currency code does not exist!")

    while not convert_amount_valid:
        convert_amount = input("What is the amount of this currency that you will be converting?")
        try:
            convert_amount = float(convert_amount)
            convert_amount_valid = True
        except ValueError:
            print("ERROR! Invalid Input. Please enter a valid number.")

    while not convert_to_valid:
        convert_to = input("What currency would you like to convert to?")
        if convert_to in list_of_currencies:
            convert_to_valid = True
        else:
            print("ERROR! This currency code does not exist!")

    convert_inputs(convert_from, convert_amount, convert_to)


if __name__ == "__main__":
    main()
