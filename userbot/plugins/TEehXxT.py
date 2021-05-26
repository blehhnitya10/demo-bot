#THANKS TO @Veryhelpful (SAWAN SIR)
#MADE BY NOOB (@I_AM_DANGEROUS_JATT)
from telethon import events
from REBELBOT.util import admin_cmd

ormiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
               'v','w','x','y','z']
irclefont = ['a⃠','b⃠','c⃠','d⃠','e⃠','f⃠','g⃠','h⃠','i⃠','j⃠','k⃠','l⃠','m⃠','n⃠','o⃠','p⃠','q⃠','r⃠','s⃠','t⃠','u⃠',
              'v⃠','w⃠','x⃠','y⃠','z⃠']

@borg.on(admin_cmd(pattern = "text1 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`give me a text `")
        return
    string = '  '.join(args).lower()
    for ormiecharacter in string:
        if ormiecharacter in ormiefont:
            irclecharacter = irclefont[ormiefont.index(ormiecharacter)]
            string = string.replace(ormiecharacter, irclecharacter)
    await event.edit(string)


nnormiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
               'v','w','x','y','z']
ccirclefont = ['𝖆','𝖇','𝖈','𝖉','𝖊','𝖋','𝖌','𝖍','𝖎','𝖏','𝖐','𝖑','𝖒','𝖓','𝖔','𝖕','𝖖','𝖗','𝖘','𝖙','𝖚',
              '𝖛','𝖜','𝖝','𝖞','𝖟']

@borg.on(admin_cmd(pattern = "text2 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`give me a text `")
        return
    string = '  '.join(args).lower()
    for nnormiecharacter in string:
        if nnormiecharacter in nnormiefont:
            ccirclecharacter = ccirclefont[nnormiefont.index(nnormiecharacter)]
            string = string.replace(nnormiecharacter, ccirclecharacter)
    await event.edit(string)


normiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
              'v','w','x','y','z']
circlefont = ['𝓪','𝓫','𝓬','𝓭','𝓮','𝓯','𝓰','𝓱','𝓲','𝓳','𝓴','𝓵','𝓶','𝓷','𝓸','𝓹','𝓺','𝓻','𝓼','𝓽','𝓾',
             '𝓿','𝔀','𝔁','𝔂','𝔃']

@borg.on(admin_cmd(pattern = "text3 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`give me a text `")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            circlecharacter = circlefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, circlecharacter)
    await event.edit(string)


onormiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
               'v','w','x','y','z']
ocirclefont = ['🅰','🅱','🅲','🅳','🅴','🅵','🅶','🅷','🅸','🅹','🅺','🅻','🅼','🅽','🅾','🅿','🆀','🆁','🆂','🆃','🆄',
              '🆅','🆆','🆇','🆈','🆉']

@borg.on(admin_cmd(pattern = "text4 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`give me a text `")
        return
    string = '  '.join(args).lower()
    for onormiecharacter in string:
        if onormiecharacter in onormiefont:
            ocirclecharacter = ocirclefont[onormiefont.index(onormiecharacter)]
            string = string.replace(onormiecharacter, ocirclecharacter)
    await event.edit(string)


anormiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
               'v','w','x','y','z']
acirclefont = ['🄰','🄱','🄲','🄳','🄴','🄵','🄶','🄷','🄸','🄹','🄺','🄻','🄼','🄽','🄾','🄿','🅀','🅁','🅂','🅃','🅄',
              '🅅','🅆','🅇','🅈','🅉']

@borg.on(admin_cmd(pattern = "text5 ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`give me a text `")
        return
    string = '  '.join(args).lower()
    for anormiecharacter in string:
        if anormiecharacter in anormiefont:
            acirclecharacter = acirclefont[anormiefont.index(anormiecharacter)]
            string = string.replace(anormiecharacter, acirclecharacter)
    await event.edit(string)