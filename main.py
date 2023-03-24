import os
import telegram.ext
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the bot token from the environment variable
BOT_TOKEN = os.environ['BOT_TOKEN']

# Create the bot
bot = telegram.Bot(token=BOT_TOKEN)

# v0.0.1: Define a function to simply echo back the user's message
def echo(update, context):
    text = update.message.text
    update.message.reply_text(text)

# Sometimes updated things aren't good https://stackoverflow.com/a/74994229
# Create an updater instance for the bot, and a dispatcher instance to handle incoming messages
updater = telegram.ext.Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

# Add a MessageHandler to the dispatcher, which calls the echo function whenever it receives a text message
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, echo))

# Start polling the Telegram server for new messages
updater.start_polling()