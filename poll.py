import telebot
import pyautogui
import os
from dotenv import load_dotenv

pyautogui.FAILSAFE = True

# Load environment variables from .env file
load_dotenv()

bot_token = os.getenv("TELE_BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# class triggers:
#
#     triggers = {}
#
#     def __init__(self):
#         pass
#
#     def check(self, message):
#         for i in range(len(triggers)):
#             if

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to the NUSCAS Halloween Games! \n\n\
NUSCASハロウィン パーティーへようこそ～～　\n \n \
(ゝω´･)～☆")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Here are the list of commands: \n \
    \n /up : walk upwards \n \
    \n /down : walk downwards \n \
    \n /left : walk left \n \
    \n /right : walk right \n \
    \n /restart : restarts the level \n \
    \n /enter: presses enter \n \
    \n /advice : check stage advice")

@bot.message_handler(commands=['w', 'W', 'up'])
def send_welcome(message):
	pyautogui.press('w')

@bot.message_handler(commands=['a', 'A', 'left'])
def send_welcome(message):
	pyautogui.press('a')

@bot.message_handler(commands=['s', 'S', 'down'])
def send_welcome(message):
	pyautogui.press('s')

@bot.message_handler(commands=['d', 'D', 'right'])
def send_welcome(message):
	pyautogui.press('d')

@bot.message_handler(commands=['r', 'R', 'restart'])
def send_welcome(message):
	pyautogui.press('r')

@bot.message_handler(commands=['enter'])
def send_welcome(message):
	pyautogui.press('enter')

@bot.message_handler(commands=['advice'])
def send_welcome(message):
	pyautogui.press('l')


bot.infinity_polling()
