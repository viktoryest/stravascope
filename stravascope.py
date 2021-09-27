import telebot
import requests
import os
import mongo_file
from parser import common_function
from conf_var_func import config_vars
from picture_creator import find_images, image_maker, get_bytes_from_image

config_vars()

app_name = os.environ.get('app_name')
token = os.environ.get('token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start', 'go'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Good day!' + '\n' +
                     'This bot maintains the @stravascope channel '
                     'and is not intended for user interaction.' + '\n' +
                     'Perhaps this will change!' + '\n' +
                     '\n' +
                     'Доброго времени суток!' + '\n' +
                     'Этот бот поддерживает работу канала @stravascope '
                     'и не предназначен для взаимодействия с пользователем.' + '\n' +
                     'Возможно, это изменится!')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, 'Welcome to the channel @stravascope!' + '\n' +
                     '\n' + 'Добро пожаловать на канал @stravascope!')


def get_challenges():
    current_id = mongo_file.collection.find_one()['current_id']

    previous_limit_id = current_id - 200
    previous_index = previous_limit_id
    challenge_list = list(map(lambda i: int(i['challenge_id']),
                              mongo_file.challenge_collections.find({}, {'challenge_id': True})))

    while previous_index <= current_id:  # if current_id was set manually
        if previous_index not in challenge_list:
            link = 'https://www.strava.com/challenges/' + str(previous_index)
            url_inform = requests.get(link).text
            if 'Challenges - Strava' not in url_inform:
                try:
                    yield common_function(previous_index), \
                          get_bytes_from_image(image_maker(find_images(previous_index)))
                    mongo_file.challenge_collections.insert_one({
                        "challenge_id": previous_index
                    })
                except:
                    print(f'Unidentified error on page {link}')

        previous_index += 1

    limit_id = current_id + 200
    index = current_id + 1

    while index < limit_id:
        link = 'https://www.strava.com/challenges/' + str(index)
        url_inform = requests.get(link).text
        if 'Challenges - Strava' not in url_inform:
            try:
                yield common_function(index), get_bytes_from_image(image_maker(find_images(index)))
                mongo_file.collection.update_one({"title": "last_challenge"}, {"$set": {'current_id': index}})
                mongo_file.challenge_collections.insert_one({
                    "challenge_id": index
                })
                limit_id = index + 200
            except:
                print(f'Unidentified error on page {link}')

        index += 1
