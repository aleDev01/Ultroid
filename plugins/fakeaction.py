# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}ftyping <time/in secs>`
    `Show Fake Typing in current chat.`

• `{i}faudio <time/in secs>`
    `Show Fake Recording Action in current chat.`

• `{i}fvideo <time/in secs>`
    `Show Fake video action in current chat.`

• `{i}fgame <time/in secs>`
    `Show Fake Game Playing Action in current chat.`

• `{i}flocation <time/in secs>`
    `Show Fake location Action in current chat.`

• `{i}fcontact <time/in secs>`
    `Show Fake contact choosing Action in current chat.`

• `{i}fsticker <time/in secs>`
    `Show Fake sticker choosing Action in current chat.`

• `{i}stopaction`
   `Stop any ongoing Chat Action going in Chat.`
"""

from . import *


@ultroid_cmd(pattern="f(typing|audio|contact|location|video|game|sticker) ?(.*)")
async def _(e):
    act = e.pattern_match.group(1)
    t = e.pattern_match.group(2)
    if act in ["audio", "video"]:
        act = "record-" + act
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await ban_time(e, t)
            except BaseException:
                return await eor(e, "`Incorrect Format`", time=5)
    await eor(e, f"Starting Fake Action For {t} sec.", time=5)
    async with e.client.action(e.chat_id, act):
        await asyncio.sleep(t)


@ultroid_cmd(pattern="stopaction")
async def do_it(e):
    await e.client.action(e.chat_id, "cancel")
    await eor(e, "Fake Action Stopped.", time=5)
