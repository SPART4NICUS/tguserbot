from telethon.tl.functions.users import GetFullUserRequest

from tg_userbot import bot, CMD_HELP, GBAN_BOTS, GBANS
from tg_userbot.events import register
from tg_userbot.modules.libs.get_id import get_id


@register(outgoing=True, pattern=r"^.gban(?: |$)([\s\S]*)")
async def gban(request):
    if not request.text[0].isalpha() and request.text[0] in ("."):
        if GBANS:
            message = request.pattern_match.group(1)
            args = message.split()
            user = ''
            reason = ''
            response = ''
            if request.reply_to_msg_id:
                previous_message = await request.get_reply_message()
                user = await request.client(GetFullUserRequest(previous_message.from_id))
                user = str(user.user.id)
                reason = message
                gbantext = '/gban ' + user + ' ' + reason
            else:
                user = str(message.split(' ', 1)[0])
                user = await get_id(request, user)
                if str(type(user)) != '<class \'telethon.tl.types.UserFull\'>':
                    await request.edit("`Lemme gban you for not giving a proper username!`")
                    return
                user = str(user.user.id)
                if len(args) == 2:
                    reason = str(message.split(' ', 1)[1])
                if len(args) == 1:
                    reason = ""
                if len(args) == 0:
                    await request.edit("`Lemme gban you for not giving a proper username!`")
                gbantext = '/gban ' + user + ' ' + reason
            for GBAN_BOT in GBAN_BOTS:
                async with bot.conversation(GBAN_BOT) as conv:
                    await conv.send_message(gbantext)
                    x = await conv.get_response()
                    if x:
                        pass
                    else:
                        x = GBAN_BOT + '  didn\'t respond'
                    response += GBAN_BOT + ': ' + x.text.replace("**", "").replace("`", "").replace("tg://user?id=", "") + '\n\n'
            await request.edit("```" + response + "```")
        else:
            await request.edit("`You haven't enabled GBANS!`")


@register(outgoing=True, pattern=r"^.ungban(?: |$)([\s\S]*)")
async def ungban(request):
    if not request.text[0].isalpha() and request.text[0] in ("."):
        if GBANS:
            message = request.pattern_match.group(1)
            args = message.split()
            user = ''
            response = ''
            if request.reply_to_msg_id:
                previous_message = await request.get_reply_message()
                user = await request.client(GetFullUserRequest(previous_message.from_id))
                user = str(user.user.id)
                gbantext = '/ungban ' + user
            else:
                user = str(message.split(' ', 1)[0])
                user = await get_id(request, user)
                if str(type(user)) != '<class \'telethon.tl.types.UserFull\'>':
                    await request.edit("`Lemme gban you instead for not giving a proper username!`")
                    return
                user = str(user.user.id)
                if len(args) == 0:
                    await request.edit("`Lemme gban you instead for not giving a proper username!`")
                gbantext = '/ungban ' + user
            for GBAN_BOT in GBAN_BOTS:
                async with bot.conversation(GBAN_BOT) as conv:
                    await conv.send_message(gbantext)
                    x = await conv.get_response()
                    if x:
                        pass
                    else:
                        x = GBAN_BOT + '  didn\'t respond'
                    response += GBAN_BOT + ': ' + x.text.replace("**", "").replace("`", "").replace("tg://user?id=", "") + '\n\n'
            await request.edit("```" + response + "```")
        else:
            await request.edit("`You haven't enabled GBANS!`")


@register(outgoing=True, pattern=r"^.gkick(?: |$)([\s\S]*)")
async def gkick(request):
    if not request.text[0].isalpha() and request.text[0] in ("."):
        if GBANS:
            message = request.pattern_match.group(1)
            args = message.split()
            user = ''
            reason = ''
            response = ''
            if request.reply_to_msg_id:
                previous_message = await request.get_reply_message()
                user = await request.client(GetFullUserRequest(previous_message.from_id))
                user = str(user.user.id)
                reason = message
                gbantext = '/gkick ' + user + ' ' + reason
            else:
                user = str(message.split(' ', 1)[0])
                user = await get_id(request, user)
                if str(type(user)) != '<class \'telethon.tl.types.UserFull\'>':
                    await request.edit("`Dafaq am i gonna gkick you?!`")
                    return
                user = str(user.user.id)
                if len(args) == 2:
                    reason = str(message.split(' ', 1)[1])
                if len(args) == 1:
                    reason = ""
                if len(args) == 0:
                    await request.edit("`Dafaq am i gonna gkick you?!`")
                gbantext = '/gkick ' + user + ' ' + reason
            for GBAN_BOT in GBAN_BOTS:
                async with bot.conversation(GBAN_BOT) as conv:
                    await conv.send_message(gbantext)
                    x = await conv.get_response()
                    if x:
                        pass
                    else:
                        x = GBAN_BOT + '  didn\'t respond'
                    response += GBAN_BOT + ': ' + x.text.replace("**", "").replace("`", "").replace("tg://user?id=", "") + '\n\n'
            await request.edit("```" + response + "```")
        else:
            await request.edit("`You haven't enabled GBANS!`")


CMD_HELP.update({
    'gbans':
        '`.gban, .ungban, .gkick\nUsage: You\'ll know if you\'ve ever had a bot. Does exactly as it says.`'
})
