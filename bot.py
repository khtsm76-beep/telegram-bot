import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")  # ناخذ التوكن من المتغيرات

def start(update, context):
    update.message.reply_text("👋 مرحباً! البوت شغال تمام.")

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
