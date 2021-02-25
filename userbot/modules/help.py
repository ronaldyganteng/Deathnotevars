# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def hep(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
            await asyncio.sleep(15)
            await event.delete()
        else:
            await event.edit("Please checking for modules user-bot.")
            await asyncio.sleep(5)
            await event.delete()
    else:
        string1 = "Maaf Ini Daftar MODUL USER-BOT !!\nUsage: .help <module name>\n\n"
        string = "• "
        string3 = "List for MODULES USER-BOT !!: "
        string2 = "-------------------------------------------------------------"
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`  •  "
        await event.edit(
            f"{string1}" f"{string3}" f"{string2}\n" f"{string}" f"{string2}"
        )
        await asyncio.sleep(20)
        await event.delete()
