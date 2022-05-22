from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I'm a **𝕿𝖊𝖑𝖊𝖌𝖗𝖆.𝖕𝖍-𝖀𝖕𝖑𝖔𝖆𝖉𝖊𝖗 𝕭𝖔𝖙**
I can upload media to telegra.ph and give you back the link with ease. Try sending multiple media, and it still won't stop me.
I can also be used in groups !!

To see `Supported Media Types` tap the related button below.
Use the other buttons to know more about me and my usage.

By @ImDark_Empire
    """

    # Help Message
    HELP = """
**READ BELOW TO KNOW HOW TO USE ME.**

See `Supported Media Types` by clicking that related button below.

**How to use me here?**
Just send the media and leave rest on me. 

**How to use in group?**
Add to me the group.
Then reply to a media with /telegraph to get the telegra.ph link.
You can alternatively also use "t" or "tg" as commands and "!" as prefix to do the same.
That is,
!t   ,   !tg   ,   !telegraph 
/t   ,   /tg   ,   /telegraph
[If you add in your group, your group users won't need to join our channel.]

__Note__ : If the bot doesn't respond in the expected way, make the bot admin so that bot gets updates for sure. Telegram is weird.

More features in development. Keep track by joining @ImDark_Empire.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @SLBotOfficial

Source Code : [Click Here](https://github.com/DARKEMPIRESL/Telegra.ph-Uploader)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImDark_Empire

Support : @trtechguide
    """

    SUPPORTED_MEDIA_TYPES = """
✨ **SUPPORTED MEDIA TYPES** ✨

1) Image
2) Sticker
3) Gifs or Animation
4) Video
5) Video Note
6) Document (Video/Photo/Gif)

Note : Telegraph has a size limit of 5 MB.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/SLBotOfficial/28")],
        [InlineKeyboardButton("♾️ Supported Media Types ♾️", callback_data="supported_media_types"),InlineKeyboardButton("Dev", url="https://t.me/ImDark_Empire")],
        [InlineKeyboardButton("Close 🌐", callback_data="close")],
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/SLBotOfficial/28")
        ],
        [InlineKeyboardButton("♾️ Supported Media Types ♾️", callback_data="supported_media_types"),InlineKeyboardButton("Dev", url="https://t.me/ImDark_Empire")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("📥 About 📥", callback_data="about")
        ],
        [InlineKeyboardButton("Close 🌐", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/SLBotOfficial/28"),InlineKeyboardButton("Dev", url="https://t.me/ImDark_Empire")],
        [InlineKeyboardButton("Close 🌐", callback_data="close")],
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")]
    ]
