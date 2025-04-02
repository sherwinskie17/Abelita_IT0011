import pandas as pd


def get_exchange_rates():
    """Returns a dictionary of currency exchange rates for 1 USD."""
    return {
        "EUR": 0.931936,
        "GBP": 0.827816,
        "JPY": 131.199494,
        "AUD": 1.439774,
        "CHF": 0.920289,
        "PHP": 54.814728,
    }

def convert_currency(amount, target_currency, exchange_rates):
    """Converts the given amount from USD to the target currency."""
    rate = exchange_rates.get(target_currency.upper())
    if rate is None:
        return None
    return amount * rate

def main():
    exchange_rates = get_exchange_rates()
    
    amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency do you want to have? ").strip().upper()
    
    converted_amount = convert_currency(amount, target_currency, exchange_rates)
    if converted_amount is None:
        print("Invalid currency code!")
    else:
        print(f"\nDollar: {amount} USD")
        print(f"{target_currency}: {converted_amount}")

if __name__ == "__main__":
    main()
