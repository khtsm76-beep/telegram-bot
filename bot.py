from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pandas as pd

# دالة تحميل البيانات
def load_data():
    return pd.read_excel("results.xlsx")

# رسالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 أهلاً! أرسل رقم جلوسك لأعطيك نتيجتك.")

# البحث عن النتيجة
async def get_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    seat = update.message.text.strip()
    if seat.isdigit():
        seat = int(seat)
        df = load_data()
        result = df[df["Number"] == seat]
        if not result.empty:
            name = result.iloc[0]["nam"]
            total = result.iloc[0]["sum"]
            avr = result.iloc[0]["AVR"]
            status = result.iloc[0]["nag"]
            await update.message.reply_text(
                f"📄 الاسم: {name}\n"
                f"📊 المجموع: {total}\n"
                f"📈 المعدل: {avr}\n"
                f"✅ النتيجة: {status}"
            )
        else:
            await update.message.reply_text("❌ رقم الجلوس غير موجود.")
    else:
        await update.message.reply_text("⚠️ أدخل رقم جلوس صحيح.")

# تشغيل البوت
def main():
  TOKEN = "429620974:AAEXymUdVhTYSYiWJ_lMhAULtitVypoQrq8"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_result))

    print("✅ البوت يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()

