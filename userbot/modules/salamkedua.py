from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.A(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙴𝚑𝚑 𝚓𝚊𝚗𝚐𝚊𝚗 𝚜𝚎𝚙𝚒 𝚍𝚘𝚗𝚐... :(")


@register(outgoing=True, pattern="^.a(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙰𝚜𝚝𝚊𝚐𝚏𝚒𝚛𝚞𝚕𝚕𝚘𝚑 𝚜𝚎𝚙𝚒 𝚋𝚊𝚗𝚐𝚎𝚝𝚜 𝚐𝚛𝚞𝚙 ... :(")


@register(outgoing=True, pattern="^.B(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙴𝚑𝚑 𝚔𝚊𝚖𝚞 𝚖𝚊𝚞 𝚝𝚊𝚞 𝚗𝚍𝚊𝚔?? ... :𝚟")


@register(outgoing=True, pattern="^.b(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙰𝚔𝚞 𝚖𝚊𝚞 𝚐𝚘𝚖𝚋𝚊𝚕/𝚙𝚊𝚗𝚝𝚞𝚗 𝚗𝚒𝚌𝚑, 𝚍𝚎𝚗𝚐𝚎𝚛𝚒𝚗 𝚔𝚎! :))")


CMD_HELP.update(
    {
        "salam": "`.A`\
\nUsage: Hanya Buat Becanda-an saja, Jangan serius!.\
\n\n`.B`\
\nUsage: Hanya Untuk Pantun/Gombal!."
    }
)
