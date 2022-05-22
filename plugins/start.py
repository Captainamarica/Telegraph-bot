from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
Hey User,
        
I'm a **𝕿𝖊𝖑𝖊𝖌𝖗𝖆.𝖕𝖍-𝖀𝖕𝖑𝖔𝖆𝖉𝖊𝖗 𝕭𝖔𝖙** That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to **Telegra.ph**

If you need any help send /help for more....😌😌
        
Made By @ImDark_Empire

You Can Clone me too :- [Click Here](https://github.com/DARKEMPIRESL)
Visit and give a **star**😁😁
Please Subscribe Our [Chanel](https://t.me/SLBotOfficial) 😎🔰
"""


if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup(
        [   
            [InlineKeyboardButton("OWNER", url="https://t.me/ImDark_Empire"),InlineKeyboardButton("About", callback_data="about")],
            [InlineKeyboardButton("Help", callback_data="help"),InlineKeyboardButton("Support Chanel", url="https://t.me/SLBotOfficial"),InlineKeyboardButton("Github", url=f"https://github.com/DARKEMPIRESL/Anonymous-Bot")],
        ]       
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = message.from_user.id
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    NewVar = START
    if var.OWNER_ID and not message.from_user.id == var.OWNER_ID:
        geto = await client.get_users(var.OWNER_ID)
        NewVar += f"\n\nMaintained By {geto.mention}"
    else:
        NewVar += "\n**Onwer Commands** - https://te.legra.ph/Owner-Commands-04-03-9"
    await message.reply_text(
        NewVar, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )
