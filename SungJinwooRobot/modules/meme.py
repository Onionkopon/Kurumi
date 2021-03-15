import html
import random
import time
import requests

import SungJinwooRobot.modules.meme_strings as meme_strings
from SungJinwooRobot import dispatcher
from SungJinwooRobot.modules.disable import DisableAbleCommandHandler
from SungJinwooRobot.modules.helper_funcs.chat_status import is_user_admin
from SungJinwooRobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

GIF_ID = "CgACAgQAAx0CSVUvGgAC7KpfWxMrgGyQs-GUUJgt-TSO8cOIDgACaAgAAlZD0VHT3Zynpr5nGxsE"


@run_async
def hug(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(hugged_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(meme_strings.HUG_GIFS), caption=f"*{user1} hugs {user2}*")
   
#plugin by t.me/RCage
@run_async
def meme(update: Update, context: CallbackContext):
    msg = update.effective_message
    meme = requests.get("https://meme-api.herokuapp.com/gimme/Animemes/").json()
    image = meme.get("url")
    caption = meme.get("title")
    if not image:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(
                photo=image, caption=caption)


MEME_HANDLER = DisableAbleCommandHandler("meme", meme)
SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize)
HUG_HANDLER = DisableAbleCommadHandler("hug", hug) 

dispatcher.add_handler(MEME_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(HUG_HANDLER)

__command_list__ = [
    "sanitize",
    "meme",
    "hug",
]
__handlers__ = [
    SANITIZE_HANDLER,
    MEME_HANDLER,
    HUG_HANDLER,
]
