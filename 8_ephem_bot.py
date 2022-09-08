"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from itertools import count
import logging
import ephem
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def now_planet(update, context):
    now = date.today()
    planets = {"Mercury": ephem.Mercury, 
     "Venus": ephem.Venus, 
     "Mars" : ephem.Mars, 
     "Jupiter": ephem.Jupiter, 
     "Saturn": ephem.Saturn, 
     "Uranus": ephem.Uranus, 
     "Neptune": ephem.Neptune,
     "Moon": ephem.Moon,
     "Pluto": ephem.Pluto}
    user_text = update.message.text.split()
    planet_name = user_text[1]
    
    if planet_name in planets:
      const = ephem.constellation(planets[planet_name](f'{now}'))
    print(const)
    update.message.reply_text(f' Планета находится в созвездии {const[1]}')    

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("API_KEY", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", now_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
