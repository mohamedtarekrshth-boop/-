import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 اهلا يا تايجر! ابعت صورة المنتج")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 استلمت الصورة! بجهزلك الاعلان حالاً")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.COMMAND, start))
app.add_handler(MessageHandler(filters.PHOTO, handle))
app.run_polling()
