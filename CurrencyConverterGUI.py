import tkinter as tk
from tkinter import messagebox

class CurrencyConverterGUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title("Currency Converter")
        self.currency_converter = converter

        # Interfejs użytkownika
        self.intro_label = tk.Label(self, text='Currency Converter', fg='blue', relief=tk.RAISED, borderwidth=3)
        self.intro_label.grid(row=0, column=1, pady=10)

        self.amount_entry = tk.Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.converted_amount_labels = []
        for i in range(8):
            label = tk.Label(self, text=f'Currency {i + 1}:', fg='green', relief=tk.RIDGE, borderwidth=3)
            label.grid(row=i + 2, column=0, padx=10, pady=10)
            self.converted_amount_labels.append(label)

        self.convert_button = tk.Button(self, text='Convert', fg='red', command=self.perform)
        self.convert_button.grid(row=10, column=1, pady=10)

    def perform(self):
        try:
            input_amount = self.amount_entry.get().replace(',', '.')  # Zamiana przecinka na kropkę
            amount = float(input_amount)

            selected_currencies = ['USD', 'EUR', 'GBP', 'AUD', 'CAD', 'JPY', 'CNY', 'INR']  # Przykładowe waluty
            for i, currency in enumerate(selected_currencies):
                converted_amount = self.currency_converter.convert('PLN', currency, amount)
                self.converted_amount_labels[i].config(text=f'{currency}: {converted_amount}')
        except ValueError:
            messagebox.showerror("Error", "Incorrect input")