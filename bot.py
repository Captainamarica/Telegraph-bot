#    This file is part of the DARK EMPIRE distribution (https://github.com/DARKEMPIRESL/Telegraph-Uploader).
#    Copyright (c) 2021 Rithunand
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/DARKEMPIRESL/Telegraph-Uploader/blob/main/License> 

import os

from vars import var

from pyrogram import Client, idle



logging.getLogger("pyrogram").setLevel(logging.INFO)

Tgraph = Client(
   "Telegra.ph Uploader",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)




Tgraph.start()
uname = (Tgraph.get_me()).username
print(f"@{uname} Deployed Successfully !")

idle()



