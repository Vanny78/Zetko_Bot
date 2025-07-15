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

    chat_id = update.effective_chat.id
    photo_path = "header.png"
    with open(photo_path, "rb") as photo:
        await context.bot.send_photo(chat_id=chat_id, photo=photo)

    welcome_text = (
        "👋 Benvenuto in Zekto!\n\n"
        "Zekto è il tuo assistente digitale personale.\n"
        "Parla con i clienti, presenta i tuoi prodotti, risponde ai messaggi, crea testi e immagini per i social...\n"
        "e lavora per te anche mentre dormi.\n\n"
        "Perfetto per aziende, artigiani, freelance, negozianti e influencer.\n\n"
        "⬇️ Scegli cosa vuoi fare:"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    back_button = [[InlineKeyboardButton("🔙 Torna al menù principale", callback_data="start")]]
    if data == "bots":
        text = "🏠 Agenzia Immobiliare\n🍝 Ristorante\n🎨 Artigiano\n🎥 Creator\n💇‍♀️ Estetista\n\n(Demo in arrivo)"
    elif data == "reseller":
        text = "Vuoi diventare rivenditore Zekto?\nCompila il form qui:\nhttps://forms.gle/XXXXXX"
    elif data == "custom":
        text = "Richiedi un bot personalizzato per la tua attività:\nhttps://forms.gle/YYYYYY"
    elif data == "contact":
        text = "📧 Email: zekto.service@gmail.com\n📲 Telegram: @Zekto_bot"
    elif data == "start":
        await start(update, context)
        return
    else:
        text = "Selezione non valida."

    reply_markup = InlineKeyboardMarkup(back_button)
    await query.edit_message_text(text=text, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
