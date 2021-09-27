import telebot
from flask import Flask, request
import os
import threading
import time
from stravascope import bot, get_challenges
from conf_var_func import config_vars

config_vars()

app = Flask(__name__)


@app.route('/' + os.environ.get('token'), methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(
        request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(os.environ.get('app_name'), os.environ.get('token')))
    return "Application is OK", 200


@app.route('/update', methods=["GET"])
def run_bot():
    threading.Thread(target=print_challenges).start()
    return "Searching for new challenges", 200


def print_challenges():
    new_challenges = get_challenges()
    for text, photo in new_challenges:
        bot.send_photo(chat_id='@stravascope', photo=photo, caption=text + '\n')
        time.sleep(3)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
