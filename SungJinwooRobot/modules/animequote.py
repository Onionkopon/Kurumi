import html
import random
import SungJinwooRobot.modules.animequote_string as animequote_string
from SungJinwooRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SungJinwooRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def aq(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(animequote_string.ANIMEQUOTE))

AQ_HANDLER = DisableAbleCommandHandler("aq", aq)

dispatcher.add_handler(AQ_HANDLER)

__mod_name__ = "anime quote"

__help__ = """
 - `/aq` : get random anime quotes

"""
