from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update
from secret_keys import token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Salom men siz yozgan so'zlarni takrorlayman")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    echo_handler = MessageHandler(filters.TEXT, echo)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()

