import requests

class CurrencyConverterController:
    def __init__(self):
        self.url = 'https://api.exchangerate-api.com/v4/latest/PLN'
        self.rates = {}
        self.load_rates()

    def load_rates(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Sprawdza, czy odpowiedź jest pomyślna
            data = response.json()
            self.rates = data['rates']  # Ustawianie kursów walut
        except Exception as e:
            print(f"Błąd podczas pobierania danych z API: {e}")

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'PLN':
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        return amount