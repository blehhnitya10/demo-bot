
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in rebel Userbot by @REBEL_IS_OP

import asyncio
import random
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, rebelversion
from REBELBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for ÂÝŮ$HópBØȚ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

rebel = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/528425227d8763cedee29.mp4"
file2 = "https://telegra.ph/file/6700325671af519dd3fd8.mp4"
file3 = "https://telegra.ph/file/a3090425421917fd339ee.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥ℝ𝔼𝔹𝔼𝕃𝔹𝕆𝕋 𝕀𝕊 𝔸𝕃𝕀𝕍𝔼🔥🔥**__\n\n"

pm_caption += (
    f"                 👑𝕄𝔸𝕊𝕋𝔼ℝ👑\n**  『😈[{DEFAULTUSER}](tg://user?id={rebel})😈』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `{version.__version__}` \n\n"

pm_caption += f"😈ℝ𝔼𝔹𝔼𝕃𝔹𝕆𝕋😈 : `{rebelversion}`\n\n"

pm_caption += f"😱SUDO😱            : `{sudou}`\n\n"

pm_caption += "😇CHANNEL😇️   : 

pm_caption += "😎CREATOR😎    : [༼🇷È🇧É🇱](https://t.me/REBEL_IS_OP)\n\n"

pm_caption += "🤩SUPPORTER🤩    :[ⓃⒾⓈⒽⓊ](https://t.me/Baapisbacknishujibolmotherchod)\n\n"

pm_caption += "      [🔥REPO🔥](https://github.com/REBEL725/REBELBOT) 🔹 [📜License📜](https://github.com/REBEL725/REBELBOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="xalive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    