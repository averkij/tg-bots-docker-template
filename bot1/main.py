import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os


BOT_TOKEN = os.getenv("BOT_TOKEN")



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    logging.info("start command")
    await update.message.reply_text('Hello! I am a simple bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text('I can help you with basic commands. Try /start!')

def main():
    """Start the bot."""
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    
    application.run_polling()

if __name__ == '__main__':
    main()