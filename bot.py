import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = f"https://aviatorbot-eyft.onrender.com/webhook"  # Your Render link
IMAGE_URL = 'https://i.imgur.com/OEaAePP.jpeg'

flask_app = Flask(__name__)
tg_app = ApplicationBuilder().token(BOT_TOKEN).build()

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=f"👋🏻 Hello {user.first_name}!\n\n🎉 WELCOME TO ETHIO AVIATOR PREDICTOR PRO."
    )

tg_app.add_handler(CommandHandler("start", start))

# Webhook endpoint for Telegram
@flask_app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), tg_app.bot)
    tg_app.update_queue.put_nowait(update)
    return "ok"

# Home page
@flask_app.route("/")
def home():
    return "Bot is running with webhook!"

if __name__ == "__main__":
    import asyncio

    async def set_webhook():
        await tg_app.bot.set_webhook(WEBHOOK_URL)

    asyncio.run(set_webhook())
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
