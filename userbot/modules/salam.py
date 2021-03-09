from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.S(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙰𝚜𝚜𝚊𝚕𝚊𝚖𝚞'𝚊𝚕𝚊𝚒𝚔𝚞𝚖 ...")


@register(outgoing=True, pattern="^.s(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙰𝚜𝚜𝚊𝚕𝚊𝚖𝚞'𝚊𝚕𝚊𝚒𝚔𝚞𝚖 ...")


@register(outgoing=True, pattern="^.D(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝚆𝚊'𝚊𝚕𝚊𝚒𝚔𝚞𝚖𝚜𝚊𝚕𝚊𝚖 ...")


@register(outgoing=True, pattern="^.d(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝚆𝚊'𝚊𝚕𝚊𝚒𝚔𝚞𝚖𝚜𝚊𝚕𝚊𝚖 ...")


CMD_HELP.update(
    {
        "salam": "`.S`\
\nUsage: Untuk Memberi salam.\
\n\n`.D`\
\nUsage: Untuk Menjawab Salam."
    }
)
