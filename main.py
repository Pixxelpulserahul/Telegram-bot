from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import json

BOT = "BOT_API"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello sar")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text_message = update.message.text.lower()

    if "request" in text_message:
        new_text_message = text_message.replace('request ', "")

        with open('data.json', 'r') as f:
            data = json.load(f)
            for key, value in data.items():
                key = key.lower() + '''
                creator's @ = https://t.me/Zo0riva
                creator's ig = @pixelpulserahul
                '''
                if new_text_message in key:
                    await context.bot.sendVideo(chat_id=update.message.chat_id, caption=key, video=value)
    else:
        await update.message.reply_text(
            "Make sure you typed correct here is the typing assis = request correct_movie_name")


async def data_convert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    movie_id = update.message.video.file_id
    movie_name = update.message.video.file_name

    with open('data.json', 'r') as f:
        data = json.load(f)

    with open('data.json', 'w') as f:
        data[f"{movie_name}"] = f"{movie_id}"
        json.dump(data, f)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "FOR REQUESTING ANY MOVIE JUST TYPE----> request movie_name <---- REMEMBER MOVIE NAME SHOULD BE CORRECT")


sender = ApplicationBuilder().token(BOT).build()

sender.add_handler(CommandHandler("start", start))
sender.add_handler(CommandHandler("hello", hello))
sender.add_handler(MessageHandler(filters.TEXT, message))
sender.add_handler(MessageHandler(filters.VIDEO, data_convert))

sender.run_polling()