from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from XMusic import app
from XMusic.core.call import XMusic
from XMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await XMusic.stop_stream(chat_id)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
