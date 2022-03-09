# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Ported by @mrismanaziz
# FROM Man-Userbot
# ReCode by @Pocongonlen

import random
import time
from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot, DEVS
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, poci_cmd

absen = [
    "**Hadir Cantik** 😁",
    "**Hadir kak** 😉",
    "**Hadir dong** 😁",
    "**Hadir Cantik** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak Cantik maap telat** 🥺",
]


misi = [
    "**Silahkan lewat cantik** 😍",
    "**Kaka cantik mau kemana** 👋🏻",
    "**Monggo kaka cantik ** 🥵",
    "**iya lewat Hati hati ya kaka cantik🥰**",
    "**Silahkan kaka cantik** 🥰",
    "**Iya kaka cantik lewat aja 😜**",
    "**Wih kaka cantik mau kemana ni🤭**",
    
]


hai = [
    "**Eh bang Zaen** 😁",
    "**Bang Zaen dari mana aja** 🙄",
    "**Dari mana aja bang baru on ** 😁",
    "**Hai bang Zaen gmn kabarnya🥰**",
    "**Lord Zaen datang ni** 🥵",
    "**Hai juga bang Zaen 😜**"
    
]
async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@poci_cmd(pattern="ping$")
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "****")
    await xx.edit("**P**")
    await xx.edit("**Po**")
    await xx.edit("**Pon**")
    await xx.edit("**Pong**")
    await xx.edit("**Pong!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await xx.edit(
        f"**𝐁𝐀𝐁𝐘𝐌𝐔-𝐔𝐒𝐄𝐑𝐁𝐎𝐓!!**\n"
        f"⚡ **Ping**  `%sms`\n"
        f"⏳ **BotUptime** `{uptime}` \n"
        f"🤖 **BotOf** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )

@poci_cmd(pattern="rping$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await ram.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await ram.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await ram.edit("**40% ████▒▒▒▒▒▒**")
    await ram.edit("**60% ██████▒▒▒▒**")
    await ram.edit("**80% ████████▒▒**")
    await ram.edit("**100% ██████████**")
    await ram.edit("✨")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await ram.edit(
        f"**💥𝗞𝗢𝗡𝗧𝗢𝗟-𝗠𝗘𝗟𝗘𝗗𝗔𝗞💥**\n"
        f"** ➠  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ➠  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ➠  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )

#  .Coded by Ramadhani RAM-UBOT

@poci_cmd(pattern="tping$")
async def _(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**𖣘 PING** "
        f"\n  ➥ `%sms` \n"
        f"** ➠  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ➠  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )
                 

#  .Coded by Lord-Userbot

@poci_cmd(pattern="speedtest$")
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@poci_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Gass!`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🏓 **Ping!**\n`%sms`" % (duration))


@poci_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8===✊D💦")
    await kping.edit("8====D💦💦")
    await kping.edit("**CROOTTTT KONTOLLL PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**KONTOllll NGENTOT!!!  🐨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@poci_cmd(pattern="keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await kopong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await kopong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await kopong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
        f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
        f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "
        f"\n ⫸ ᴷᵃᵐᵖᵃⁿᵍ『[{user.first_name}](tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala



# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(absen))

@register(incoming=True, from_users=1608831215, pattern=r"^.misi$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(misi))

@register(incoming=True, from_users=2010825200, pattern=r"^.hai$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(hai))



CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  •  **Syntax :** `{cmd}ping`\
        \n  •  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  •  **Syntax :** `{cmd}keping`\
        \n  •  **Function : **Untuk menunjukkan keping userbot.\
        \n\n  •  **Syntax :** `{cmd}pong`\
        \n  •  **Function : **Sama seperti perintah ping\
        \n\n  •  **Syntax :** `{cmd}kping`\
        \n  •  **Function : **Untuk menunjukkan kping userbot.\
        \n\n  •  **Syntax :** `{cmd}rping`\
        \n  •  **Function : **Untuk menunjukkan rping userbot.\
        \n\n  •  **Syntax :** `{cmd}tping`\
        \n  •  **Function : **Untuk menunjukkan tping userbot.\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  •  **Syntax :** `{cmd}speedtest`\
        \n  •  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
