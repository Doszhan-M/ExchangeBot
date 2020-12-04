import json
import requests

from config import *


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = f"{message.chat.username}, я могу подсказать текущий курс валют! \n\n" \
           f"Для этого введите: \n<имя валюты> <в какую валюты перевести>" \
           f"<количество переводимой валюты> \n\nНапример, евро доллар 100 \n\n" \
           f"Чтобы увидеть список доступных валют: /values"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanger.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://api.exchangeratesapi.io/latest?base={exchanger[quote]}&symbols={exchanger[base]}')
    total = int(amount) * round(json.loads(r.content)['rates'][exchanger[base]], 2)
    text = f'Цена {amount} {quote} в {base} -- {total} {exchanger[base]}'
    bot.reply_to(message, text)


bot.polling(none_stop=True, interval=0)
