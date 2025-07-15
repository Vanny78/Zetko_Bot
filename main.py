import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Scopri i Bot disponibili", callback_data="bots")],
        [InlineKeyboardButton("🧰 Diventa rivenditore", callback_data="reseller")],
        [InlineKeyboardButton("✍️ Richiedi un Bot personalizzato", callback_data="custom")],
        [InlineKeyboardButton("🧑‍💼 Contatta lo staff", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Benvenuto in Zekto!
Scegli cosa vuoi fare:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "bots":
        text = "🏠 Agenzia Immobiliare
🍝 Ristorante
🎨 Artigiano
🎥 Creator
💇‍♀️ Estetista

(Demo in arrivo)"
    elif data == "reseller":
        text = "Vuoi diventare rivenditore Zekto?
Compila il form qui:
https://forms.gle/XXXXXX"
    elif data == "custom":
        text = "Richiedi un bot personalizzato per la tua attività:
https://forms.gle/YYYYYY"
    elif data == "contact":
        text = "📧 Email: zekto.service@gmail.com
📲 Telegram: @Zekto_bot"
    else:
        text = "Selezione non valida."

    await query.edit_message_text(text=text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
