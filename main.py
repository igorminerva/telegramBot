from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
import random
import os
import pandas as pd

BOT_TOKEN = os.getenv('BOT_TOKEN')

def load_quotes_from_csv(file_path="quotes.csv"):
    global quotes
    df = pd.read_csv(file_path, header=None, encoding='utf-8')  # no headers expected
    quotes = df.iloc[:, 0].dropna().astype(str).tolist()


subscribers = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You're not welcome but please /subscribe")

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    subscribers.add(chat_id)
    await update.message.reply_text("You subscribed, I'm sorry for you (not really)")

async def send_daily_quote(context: ContextTypes.DEFAULT_TYPE):
    if not quotes:  # Check if quotes are loaded
        return  # Do nothing if no quotes are available

    quote = random.choice(quotes)

    for chat_id in subscribers:
        await context.bot.send_message(chat_id=chat_id, text=f"🌞 Daily Bad Quote:\n\n{quote}")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not quotes:  # Check if quotes are loaded
        await update.message.reply_text("Error: No quotes available!")
        return

    quote = random.choice(quotes)

    user = update.effective_user
    name = user.username if user.username else user.first_name

    message = f"🌟 Hey @{name}, here's your quote:\n\n{quote}"
    await update.message.reply_text(message)

def main():
    load_quotes_from_csv()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("quote",quote))

    #scheduler = BackgroundScheduler()
    #scheduler.add_job(send_daily_quote,'cron', hour=9, minute=0, args=[app])
    #scheduler.start()

    app.run_polling()

if __name__ == "__main__":
    main()
