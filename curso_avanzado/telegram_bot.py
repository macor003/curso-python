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
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


class Char:
    def __init__(self, name, vocation, level, world):
        self.name = name
        self.vocation = vocation
        self.level = level
        self.world = world


class World:
    def __init__(self, players_online, creation_date, location, pvp_type, battleye_status):
        self.players_online = players_online
        self.creation_date = creation_date
        self.location = location
        self.pvp_type = pvp_type
        self.battleye_status = battleye_status


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
    
    *Hola Bienvenid@ al bot de Tibia en Español!*
    
    Para conocer los comandos disponibles utiliza /help
    
    ''', ParseMode.MARKDOWN)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('''
_Bienvenid@!_
    
Para hacer uso del bot ejecuta alguno de los siguientes comandos:
   
/char *NOMBRE_CHAR*
/rashid
/boosted
/world *NOMBRE_WORLD*
    
    
    ''', ParseMode.MARKDOWN)


def request_char(char_name):
    logging.info('https://api.tibiadata.com/v2/characters/' + char_name + '.json')
    response = requests.get('https://api.tibiadata.com/v2/characters/' + char_name + '.json')
    character = ''
    if response.status_code == 200:
        logging.info('Request Success')
        data = json.loads(response.content)
        character = Char(data["characters"]['data']['name'], data["characters"]['data']['vocation'],
                         str(data["characters"]['data']['level']), data["characters"]['data']['world'])
    else:
        logging.error('ERROR!!')
        logging.error(response.status_code)

    return character


def char(update: Update, context: CallbackContext) -> None:
    count = len(context.args)
    char_name = ''
    for idx in range(0, count):
        char_name += context.args[idx] + ' '

    character = request_char(char_name.strip().replace(' ', '+'))
    mensaje_salida = ''' Hola  *{}* , Eres un _{}_ Level _{}_ y juegas en *{}*.

    _Gracias por consultar, pronto tendremos mas información._ 
            '''.format(character.name, character.vocation, character.level, character.world)

    update.message.reply_text(mensaje_salida, ParseMode.MARKDOWN)


def request_world(world_name):
    logging.info('https://api.tibiadata.com/v2/world/' + world_name + '.json')
    response = requests.get('https://api.tibiadata.com/v2/world/' + world_name + '.json')
    world_object = ''
    if response.status_code == 200:
        logging.info('Request Success')
        data = json.loads(response.content)
        world_object = World(str(data["world"]['world_information']['players_online']),
                             data["world"]['world_information']['creation_date'],
                             data["world"]['world_information']['location'],
                             data["world"]['world_information']['pvp_type'],
                             data["world"]['world_information']['battleye_status'])
    else:
        logging.error('ERROR!!')
        logging.error(response.status_code)

    return world_object


def world(update: Update, context: CallbackContext) -> None:
    world_name = context.args[0]
    world = request_world(world_name.strip().lower())

    update.message.reply_text(
        ''' 
        El servidor de *{}* tiene actualmente las siguientes características:

Creado: *{}*
Jugadores en linea: *{}*
Ubicado en: *{}*
Es de tipo: *{}*.

_{}_
 
        '''.format(world_name.capitalize(), world.creation_date, world.players_online, world.location, world.pvp_type,
                   world.battleye_status), ParseMode.MARKDOWN)


def rashid(update: Update, context: CallbackContext) -> None:
    logging.info('https://api.tibialabs.com/v1/rashid/city')
    response = requests.get('https://api.tibialabs.com/v1/rashid/city')

    if response.status_code == 200:
        logging.info('Request Success')
        update.message.reply_text('Rashid esta ubicado hoy en: *' + response.text + '*', ParseMode.MARKDOWN)
    else:
        logging.error('ERROR!!')
        logging.error(response.status_code)


def boosted(update: Update, context: CallbackContext) -> None:
    logging.info('https://api.tibialabs.com/v1/boostedcreature/name')
    response = requests.get('https://api.tibialabs.com/v1/boostedcreature/name')

    if response.status_code == 200:
        logging.info('Request Success')
        update.message.reply_text('La creatura Boosted de hoy es:  *' + response.text + '*', ParseMode.MARKDOWN)
    else:
        logging.error('ERROR!!')
        logging.error(response.status_code)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    update.message.reply_text('Lo siento no te entiendo, ejecuta /help para saber como usarme')


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
    dispatcher.add_handler(CommandHandler("world", world))

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
