from pyrogram import Client, filters

api_id = 39231196  
api_hash = '412cae7b9ba07585cb8af6e35e60e35e'
bot_token = '9089338518:AAGbaiD0FEqNejWEcnNhgijLkGisZFm5FQU'

app = Client(
    "my_telegram_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply("বট সচল আছে! @forward868_bot কাজ করছে।")

print("Bot is starting via GitHub/Cloud...")
app.run()
