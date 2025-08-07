from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7535391262:AAG-xbokyJGmR8gHhTSpu7uI1FScmqxqYZ4'
IMAGE_URL = 'https://i.imgur.com/nXmrUzW.jpeg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=f"👋 Hello {user.first_name}!\n\n🎉 WWELCOME TO ETHIO AVIATOR PREDICTOR PRO, CLICK BELOW THE BUTTON."
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot is running...")
app.run_polling()
