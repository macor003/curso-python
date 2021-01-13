#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def request_tibia(char_name):
    print('https://api.tibiadata.com/v2/characters/' + char_name + '.json')
    response = requests.get('https://api.tibiadata.com/v2/characters/' + char_name + '.json')
    if response.status_code == 200:
        print('Request Success')
        print(str(response.content))
    else:
        print('ERROR!!')


def char(update: Update, context: CallbackContext) -> None:
    count = len(context.args)
    char_name = ''
    for idx in range(0, count):
        char_name += context.args[idx] + ' '

    update.message.reply_text('Hola ' + str(char_name.strip()) + '''.
    
    Bienvenid@ al bot de tibia que te muestra todo 
    lo que necesites.''')

    request_tibia(char_name)


def compa(update: Update, context: CallbackContext) -> None:
    nombre = context.args[0].upper()
    if nombre == 'EDGAR':
        update.message.reply_text('Compa compa compa compa llegate compa te estamos esperando en Medellin')
    else:
        update.message.reply_text('Lo siento tu no eres el compa. Chao!')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1273550293:AAHcVHWFa6fTzG9j8L2ctH0sa1XdPBLaK00", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("char", char))
    dispatcher.add_handler(CommandHandler("compa", compa))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
