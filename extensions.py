import json

import requests

from config import *


class ConversionException(Exception):
    pass


class Convertor:
    @staticmethod
    def convert(quote, base, amount):

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = exchanger[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = exchanger[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total = int(amount) * round(json.loads(r.content)['rates'][exchanger[base]], 2)

        return total
