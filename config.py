import telebot

TOKEN = '1493901681:AAGCDoJK99fhfXwI7Jlauwix6oz7Uva9xHs'

bot = telebot.TeleBot(TOKEN)

exchanger = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}
