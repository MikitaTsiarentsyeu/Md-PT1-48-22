#5339396394:AAGyY93nRFoAevMjriYcR-5kltTjmk8KFqs
import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5339396394:AAGyY93nRFoAevMjriYcR-5kltTjmk8KFqs")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there!')

@bot.message_handler(commands=['update'])
def update_message(message):
    html = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)

    tag_list = soup.findAll('p', {'class': 'value'})

    buy = tag_list[0].text
    sell = tag_list[1].text
    nb = tag_list[2].text

    bot.send_message(message.chat.id, buy + ", " + sell + ", " + nb)


bot.polling()
