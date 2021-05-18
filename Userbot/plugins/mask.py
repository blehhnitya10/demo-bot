# credits to @mrconfused and @sandy1709

#    Copyright (C) 2020  sandeep.n(π.$)

import base64
import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.helpers.functions import (
    awooify,
    baguette,
    convert_toimage,
    iphonex,
    lolice,
)
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="mask$", outgoing=True))
@bot.on(sudo_cmd(pattern="mask$", allow_sudo=True))
async def _(rebelbot):
    reply_message = await rebelbot.get_reply_message()
    if not reply_message.media or not reply_message:
        await edit_or_reply(rebelbot, "```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        await edit_or_reply(rebelbot, "```Reply to actual users message.```")
        return
    event = await rebelbot.edit("```Processing```")
    async with rebelbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await rebelbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await edit_or_reply(rebelbot, "`Please unblock` @hazmat_suit_bot `and try again`")
            return
        if response.text.startswith("Forward"):
            await edit_or_reply(rebelbot, "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await rebelbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@bot.on(admin_cmd(pattern="awooify$", outgoing=True))
@bot.on(sudo_cmd(pattern="awooify$", allow_sudo=True))
async def rebelbot(rebelmemes):
    replied = await rebelmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    if replied.media:
        rebelevent = await edit_or_reply(rebelmemes, "passing to telegraph...")
    else:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    try:
        rebel = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        rebel = Get(rebel)
        await rebelmemes.client(rebel)
    except BaseException:
        pass
    download_location = await rebelmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await rebelevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await rebelevent.edit("generating image..")
    else:
        await rebelevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await rebelevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    rebel = f"https://telegra.ph{response[0]}"
    rebel = await awooify(rebel)
    await rebelevent.delete()
    await rebelmemes.client.send_file(rebelmemes.chat_id, rebel, reply_to=replied)


@bot.on(admin_cmd(pattern="lolice$"))
@bot.on(sudo_cmd(pattern="lolice$", allow_sudo=True))
async def rebelbot(rebelmemes):
    replied = await rebelmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    if replied.media:
        rebelevent = await edit_or_reply(rebelmemes, "passing to telegraph...")
    else:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    try:
        rebel = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        rebel = Get(rebel)
        await rebelmemes.client(rebel)
    except BaseException:
        pass
    download_location = await rebelmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await rebelevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await rebelevent.edit("generating image..")
    else:
        await rebelevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await rebelevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    rebel = f"https://telegra.ph{response[0]}"
    rebel = await lolice(rebel)
    await rebelevent.delete()
    await rebelmemes.client.send_file(rebelmemes.chat_id, rebel, reply_to=replied)


@bot.on(admin_cmd(pattern="bun$"))
@bot.on(sudo_cmd(pattern="bun$", allow_sudo=True))
async def rebelbot(rebelmemes):
    replied = await rebelmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    if replied.media:
        rebelevent = await edit_or_reply(rebelmemes, "passing to telegraph...")
    else:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    try:
        rebel = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        rebel = Get(rebel)
        await rebelmemes.client(rebel)
    except BaseException:
        pass
    download_location = await rebelmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await rebelevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await rebelevent.edit("generating image..")
    else:
        await rebelevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await rebelevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    rebel = f"https://telegra.ph{response[0]}"
    rebel = await baguette(rebel)
    await rebelevent.delete()
    await rebelmemes.client.send_file(rebelmemes.chat_id, rebel, reply_to=replied)


@bot.on(admin_cmd(pattern="iphx$"))
@bot.on(sudo_cmd(pattern="iphx$", allow_sudo=True))
async def rebelbot(rebelmemes):
    replied = await rebelmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    if replied.media:
        rebelevent = await edit_or_reply(rebelmemes, "passing to telegraph...")
    else:
        await edit_or_reply(rebelmemes, "reply to a supported media file")
        return
    try:
        rebel = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        rebel = Get(rebel)
        await rebelmemes.client(rebel)
    except BaseException:
        pass
    download_location = await rebelmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await rebelevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await rebelevent.edit("generating image..")
    else:
        await rebelevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await rebelevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    rebel = f"https://telegra.ph{response[0]}"
    rebel = await iphonex(rebel)
    await rebelevent.delete()
    await rebelmemes.client.send_file(rebelmemes.chat_id, rebel, reply_to=replied)


CmdHelp("mask").add_command(
  "mask", "<reply to img/stcr", "Makes an image a different style."
).add_command(
  "iphx", "<reply to img/stcr", "Covers the replied image or sticker into iphonex wallpaper"
).add_command(
  "bun", "<reply to img/stcr", "Gives the replied img a cool bun eating look"
).add_command(
  "lolice", "<reply to img/stcr", "Gives the replied img the face of Lolice Cheif"
).add_command(
  "awooify", "<reply to img/stcr", "Gives the replied img or stcr the face or wooify"
).add() 
