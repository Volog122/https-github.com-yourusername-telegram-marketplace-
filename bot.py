from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler


async def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛍️ Открыть маркетплейс",
                web_app=WebAppInfo(url="https://your-marketplace.onrender.com "),
            )
        ]
    ]
    await update.message.reply_text(
        "Добро пожаловать!", reply_markup=InlineKeyboardMarkup(keyboard)
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token("ВАШ_ТОКЕН").build()
    application.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    application.run_polling()
