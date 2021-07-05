# Support Channel @Vckyouuu

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from GeezMusic import Geez as app
from GeezMusic import LOGGER

pm_start_text = """
Hey👋 [{}](tg://user?id={}), Saya Bot Pengunduh Lagu Yang Telah Di Rancang 
Khusus Oleh Seseorang Dengan Segabut Mungkin😂, Saya Bisa Mengunduhkan Sebuah
Lagu Yang Anda Minta Dengan Cara:


Ketik /help untuk mengetahui perintah saya

Di kelola Oleh {OWNER}
"""

help_text = """
Perintah saya👇

- /lagu <nama lagu>: unduh lagu melalui Youtube
- /savn <nama lagu>: mengunduh lagu melalui JioSaavn
- /deez <nama lagu>: mengunduh lagu melalui Deezer
- Kirim url youtube ke pm saya untuk mendownload music yang anda minta
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Di Dukung Oleh ❤️", url="https://t.me/SujandraAsissten"
                    ),
                    InlineKeyboardButton(
                        text="Owner☕", url="https://t.me/LordGanss10"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("Geez Music Sudah Online!")
idle()
