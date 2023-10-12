import asyncio
import time
from pyrogram import Client
from pyrogram.types import (InlineKeyboardMarkup,
                            InlineKeyboardButton)
from config import api_id, api_hash, bot_token, chat_id, test_chat, message, button

app = Client("yobahelp_bot",
             api_id,
             api_hash,
             bot_token)
first_button = InlineKeyboardButton(button["txt"], button["url"])


async def main():
    async with app:
        while True:
            if time.gmtime().tm_hour == 15:  # Greenwich = 18 msk
                await app.send_message(chat_id, message, reply_markup=InlineKeyboardMarkup([[first_button]]))
            await asyncio.sleep(3000)


app.run(main())
