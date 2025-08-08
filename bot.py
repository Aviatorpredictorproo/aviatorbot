import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading

BOT_TOKEN = os.getenv('BOT_TOKEN')  # Token from environment variable
IMAGE_URL = 'https://i.imgur.com/OEaAePP.jpeg'

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=f"👋🏻 Hello {user.first_name}!\n\n🎉 WELCOME TO ETHIO AVIATOR PREDICTOR PRO."
    )

app.add_handler(CommandHandler("start", start))

def run_bot():
    app.run_polling()

web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
