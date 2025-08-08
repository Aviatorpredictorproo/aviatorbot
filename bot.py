from flask import Flask
import threading                                                from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, Co>
import os

BOT_TOKEN = os.getenv('7535391262:AAG-xbokyJGmR8gHhTSpu7uI1FScm>IMAGE_URL = 'https://i.imgur.com/OEaAePP.jpeg'

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_T>
    user = update.effective_user
    await update.message.reply_photo(                                   photo=IMAGE_URL,
        caption=f"👋🏻 Hello {user.first_name}!\n\n🎉 WELCOME T>
    )

app.add_handler(CommandHandler("start", start))

def run_bot():
    app.run_polling()

# Flask server for Render
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running!"

