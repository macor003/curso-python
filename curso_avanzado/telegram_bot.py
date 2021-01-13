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

import json
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


class Char:

    def __init__(self, name, vocation, level, world):
        self.name = name
        self.vocation = vocation
        self.level = level
        self.world = world


def request_tibia(char_name):
    print('https://api.tibiadata.com/v2/characters/' + char_name + '.json')
    response = requests.get('https://api.tibiadata.com/v2/characters/' + char_name + '.json')
    character = ''
    if response.status_code == 200:
        print('Request Success')
        # print(str(response.content))
        data = json.loads(response.content)
        # print(data)

        character = Char(data["characters"]['data']['name'], data["characters"]['data']['vocation'],
                         str(data["characters"]['data']['level']), data["characters"]['data']['world'])
    else:
        print('ERROR!!')

    return character


def char(update: Update, context: CallbackContext) -> None:
    count = len(context.args)
    char_name = ''
    for idx in range(0, count):
        char_name += context.args[idx] + ' '

    character = request_tibia(char_name.strip().replace(' ', '+'))

    update.message.reply_text(
        'Hola ' + character.name + ', Eres un ' + character.vocation + ' Level ' + character.level + ' y juegas en ' + character.world)


def rashid(update: Update, context: CallbackContext) -> None:
    response = requests.get('https://api.tibialabs.com/v1/rashid/city')
    update.message.reply_text('Rashid esta ubicado hoy en: ' + response.text)


def boosted(update: Update, context: CallbackContext) -> None:
    response = requests.get('https://api.tibialabs.com/v1/boostedcreature/name')
    update.message.reply_text('La creatura Boosted de hoy es: ' + response.text)


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
    dispatcher.add_handler(CommandHandler("rashid", rashid))
    dispatcher.add_handler(CommandHandler("boosted", boosted))

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
