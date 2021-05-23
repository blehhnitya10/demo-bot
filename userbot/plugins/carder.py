import os
from faker import Faker
import datetime
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from REBELBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from REBELBOT import CmdHelp, bot as rebelbot


@REBELBOT.on(admin_cmd("gencc$"))
@REBELBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(rebelevent):
    if rebelevent.fwd_from:
        return
    rebelcc = Faker()
    rebelname = rebelcc.name()
    rebeladre = rebelcc.address()
    rebelcard = rebelcc.credit_card_full()
    
    await edit_or_reply(rebelevent, f"__**👤 NAME :- **__\n`{rebelname}`\n\n__**🏡 ADDRESS :- **__\n`{rebeladre}`\n\n__**💸 CARD :- **__\n`{rebelcard}`")
    

@rebelbot.on(admin_cmd(pattern="bin ?(.*)"))
@rebelbot.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    rebel_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/bin {rebel_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@rebelbot.on(admin_cmd(pattern="vbv ?(.*)"))
@rebelbot.on(sudo_cmd(pattern="vbv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    rebel_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/vbv {rebel_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
    
    
@rebelbot.on(admin_cmd(pattern="key ?(.*)"))
@rebelbot.on(sudo_cmd(pattern="key ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    rebel_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/key {rebel_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
 
  
@rebelbot.on(admin_cmd(pattern="iban ?(.*)"))
@rebelbot.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    rebel_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/iban {rebel_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
@rebelbot.on(admin_cmd(pattern="ccheck ?(.*)"))
@rebelbot.on(sudo_cmd(pattern="ccheck ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    rebel_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/ss {rebel_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
             
             
@rebelbot.on(admin_cmd(pattern="ccbin ?(.*)"))
@rebelbot.on(sudo_cmd(pattern="ccbin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    rebel_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{rebel_input}`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/gen {rebel_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
CmdHelp("carder").add_command(
  "gencc", None, "Generates fake cc..."
).add_command(
  "ccheck", "<query>", "Checks that the given cc is live or not"
).add_command(
  "iban", "<query>", "Checks that the given IBAN ID is live or not"
).add_command(
  "key", "<query>", "Checks the status of probided key"
).add_command(
  "vbv", "<query>", "Checks the vbv status of given card"
).add_command(
  "bin", "<query>", "Checks that the given bin is valid or not"
).add_command(
  "ccbin", "<bin>", "Generates CC from the given bin."
).add()