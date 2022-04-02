import os
import sys
import time
import logging

from telegram.ext import Updater, CommandHandler

"""
 
Usage:
    * create your own script in example_bots/yourbot.py
    * import this class (f.e. "from src.bot import Bot")
    * create your own class and inherit from this class (f.e. "class YourBot(Bot):")
    * initialize the parent class in your __init__ function with super().__init__(tokenfile) where tokenfile is a file
      path containing a valid token from @BotFather
    * Example:
    
        from src.bot import Bot
        from telegram.ext import CommandHandler
    
        class YourBot(Bot):
            def __init__(self):
                # Note that all files that contain "token" in their name are excluded from git commits.
                # Git will refuse commit with passwords/tokens and block your account!
                # Make sure never to commit credentials! (thus use "token" somewhere in the token files name)
                
                super().__init__("valid/path/containing/token.txt")

    * From here you can add functions to the class. Look at the parent bots __print() function, you need to use the
      exact same function attributes. The __init__ function of YourBot(Bot) class needs to register your new function.
      Use self.dispatcher.add_handler(CommandHandler(command='myfunction', callback=self.my_function))
      Now you can start the bot and send him the command /myfunction to make him execute self.my_function
      
You can find the:
    * API documentation - https://python-telegram-bot.readthedocs.io/en/stable/
    * Github Repository - https://github.com/python-telegram-bot/python-telegram-bot

Example execution of Parent Bot:
    * create a tokenfile in this files folder (src) named "token" with your token in it
    * open a command line and change into this directory (easybot/)
    * start this bot with:
        "python3 -m venv venv && pip3 install -r requirements.txt && . venv/bin/activate && python3 bot.py"
    * open telegram and sent your bot a message with the /print command (f.e. "/print send back this text").
    
This will call the registered command handler in the __init__ function which calls the __print() function and
executes the code inside.

To create more advanced bots check out our collection of example bots in example_bot.
or the official API under https://python-telegram-bot.readthedocs.io/en/stable/telegram.html#handlers
"""

logger = logging.Logger("Bot")


class BotException(Exception):
    """
    Generic Exception Class.
    """
    pass


class Bot:
    """
    This is the Parent Bot Class.

    """
    def __init__(self, token_file="token"):

        logger.info("Init ...")

        if not os.path.isfile(token_file):
            raise BotException("A file containing a token must be provided. File {} does not exist!".format(token_file))

        self.__updater, self.__dispatcher = self.__register_bot(token_file)  # The actual updater and dispatcher

        logger.info("Updater and Dispatcher created ...")

        self.dispatcher.add_handler(CommandHandler(command='print', callback=self.__print))

    @property
    def updater(self):
        return self.__updater

    @property
    def dispatcher(self):
        return self.__dispatcher

    @staticmethod
    def __print(update, context):
        """ This is an example method to register to the dispatcher.
            Sends all arguments received to the chat the message was received.
            See https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackcontext.html for details on
            this functions arguments (update & context).

        :param update: The context of the chat
        :param context: The context of the message
        """
        message = " ".join(context.args)  # context.args contains all words except the received command

        update.message.reply_text(chat_id=update.message.chat_id, text=message)

        return

    def start_bot(self):
        """ Starts the Bot. """
        logger.info("Starting bot ...")

        self.updater.start_polling()
        self.updater.idle()

    @staticmethod
    def __register_bot(token_file):
        """ Registers the bot using a token. You can receive your own token from @BotFather (telegram).

        :param token_file: path to a file containing a valid token from the BotFather
        """
        if not os.path.isfile(os.path.abspath(token_file)):
            raise FileNotFoundError(token_file)

        try:
            with open(token_file, 'r') as file:
                token = file.read().strip()
        except FileNotFoundError as exc:
            raise BotException(exc)

        if token == "" or len(token) != 46:
            raise BotException(f"The token {token} provided by {os.path.abspath(token_file)} seems to be corrupted." 
                               "It must be 46 characters long!")

        updater = Updater(token=token)  # The updater for bot, takes the bot token to start
        dispatcher = updater.dispatcher  # The message dispatcher

        return updater, dispatcher


if __name__ == "__main__":
    # This is an endless loop, if the bot stops it'll start it again
    # Copy the whole if clause into your script and rename Bot() to the name of the class of your bot
    while True:
        try:
            bot = Bot()
            bot.start_bot()
        except BotException as err:
            print(err)
            print("This is a critical error - exiting main loop")
            sys.exit(1)
        except Exception as exc:
            print(exc)
            print("Restarting the bot in 5 seconds ...")
            time.sleep(5)
        finally:
            print("Bot shut down")
