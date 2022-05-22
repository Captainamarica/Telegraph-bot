from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from telegraph import upload_file
from database.setting import check_settings
from database.userchats import add_chat

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

HELP_TEXT = """**About Me**
- Just give me a media under 5MB
- Then I will download it
- I will then upload it to the telegra.ph link
Made by @ImDark_Empire"""


START_TEXT = """Hey User,
        
I'm a **𝕿𝖊𝖑𝖊𝖌𝖗𝖆.𝖕𝖍-𝖀𝖕𝖑𝖔𝖆𝖉𝖊𝖗 𝕭𝖔𝖙** That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to **Telegra.ph**
If you need any help send /help for more....😌😌
        
Made By @ImDark_Empire
You Can Clone me too :- [Click Here](https://github.com/DARKEMPIRESL/Anonymous-Bot)
Visit and give a **star**😁😁
Please Subscribe Our [Chanel](https://t.me/SLBotOfficial) 😎🔰"""


START_BUTTONS = InlineKeyboardMarkup(
    [
        [   
            [InlineKeyboardButton("OWNER", url="https://t.me/ImDark_Empire"),InlineKeyboardButton("About", callback_data="about")],
            [InlineKeyboardButton("Help", callback_data="help"),InlineKeyboardButton("Support Chanel", url="https://t.me/SLBotOfficial"),InlineKeyboardButton("Github", url=f"https://github.com/DARKEMPIRESL/Anonymous-Bot")],
        ]  
)



HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Channel', url='https://telegram.me/SLBotOfficial'),
            InlineKeyboardButton('Feedback', url='https://telegram.me/SL_BOTS_TM_bot')
        ],
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_TEXT = """**About Me**
- **Bot :** `Telegraph Uploader`
- **Creator :** [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊](https://telegram.me/ImDark_Empire)
- **Channel :** [Fayas Noushad](https://telegram.me/SLBotOfficial)
- **Source :** [Click here](https://github.com/DARKEMPIRESL)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""


@Client.on_callback_query()
async def cb_data(bot, update):
    
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()

@Client.on_message(filters.private & filters.media)
async def getmedia(bot, update):
    
    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
    
    try:
        message = await update.reply_message(
            text="`Processing...`",
            quote=True,
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('More Help', callback_data='help')]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    
    text=f"**Link :-** `https://telegra.ph{response[0]}`\n\n**Join :-** @ImDark_Empire"
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
            ],
            [
                InlineKeyboardButton(text="Join Updates Channel", url="https://telegram.me/FayasNoushad")
            ]
        ]
    )
    
    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
