# StravaScope Bot

[@stravascope_bot](https://t.me/stravascope_bot ) - 
неофициальный телеграм-бот,
предназначенный для интеграции с популярным сервисом отслеживания
спортивной активности Strava.  
При появлении на [сайте](https://www.strava.com/) новой задачи
бот отправляет сообщение, включающее название, дату, типы
активностей  и ссылку, в канал
[StravaScope Channel](https://t.me/stravascope).

## Взаимодействие с ботом

В настоящее время не предусмотрено взаимодействие пользователя
непосредственно с ботом. Последний отвечает на любое сообщение
заранее заданным текстом.

## Технологии/Фреймворки

- Bot API:
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)  
- Веб-фреймворк: [Flask](https://github.com/pallets/flask)  
- База данных: [MongoDB](https://www.mongodb.com/)
- Генерация изображений: 
[Pillow](https://pillow.readthedocs.io/en/stable/)  
- Хостинг: [Heroku](https://heroku.com/)

## Установка

Для установки зависимостей выполните команду:  
```shell
pip install -r requirements.txt
```  
Для локального использования замените значение переменных в 
`.env_example` на собственные и замените название файла на 
`.env`.  
Затем запустите файл `app.py`:
```shell
python app.py
```