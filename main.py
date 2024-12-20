#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"{user.mention_html()} Read More community'mizga xush kelibsiz!  Kirish kodini olish uchun /login ni bosing",
    )


async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /login is issued."""
    code = 12345
    user = update.effective_user
    print(user.id)
    print(user.username)
    print(user.first_name)
    print(user.last_name)

    await update.message.reply_html(
        f"Sizning kirish kodingiz: <code>{code}</code>. Nusxalash uchun kodni ustiga bosing.")


# Telefon raqamini so'rash
def ask_phone(update: Update, context: CallbackContext) -> None:
    # Reply keyboard yaratamiz
    keyboard = [[KeyboardButton("Telefon raqamni ulashish", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text("Telefon raqamingizni ulashish uchun tugmani bosing:", reply_markup=reply_markup)


# Telefon raqamini qabul qilish
def receive_contact(update: Update, context: CallbackContext) -> None:
    contact = update.message.contact
    if contact:
        update.message.reply_text(f"Rahmat! Sizning telefon raqamingiz: {contact.phone_number}")
    else:
        update.message.reply_text("Telefon raqamini ulashishda xatolik yuz berdi.")


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7522039374:AAFKAWV_D58Wl0DxNT6Sw9lGbecwpJVaYKE").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("login", login))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
