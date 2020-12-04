import telebot

from extensions import *

bot = telebot.TeleBot(TOKEN)


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
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Слишком много параметров')
        quote, base, amount = values
        total = Convertor.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} -- {total} {exchanger[base]}'
        bot.reply_to(message, text)


bot.polling(none_stop=True, interval=0)
