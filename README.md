# StravaScope Bot

[@stravascope_bot](https://t.me/stravascope_bot ) - 
unofficial telegram-bot for integration with popular service 
Strava.  
When a new challenge appears on [site](https://www.strava.com/)
bot sends a message to the [StravaScope Channel](https://t.me/stravascope), 
including title, date, activity types and link.

## Interaction with the bot

At the present time user interaction with the bot directly is not provided.
The bot replies to any message with the same welcome text.

## Technologies/Frameworks

- Bot API:
[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)  
- Web framework: [Flask](https://github.com/pallets/flask)  
- Database: [MongoDB](https://www.mongodb.com/)
- Generation of images: 
[Pillow](https://pillow.readthedocs.io/en/stable/)  
- Hosting: [Heroku](https://heroku.com/)

## Installation

To install the dependencies, run the command:
```shell
pip install -r requirements.txt
```
For local use, replace the value of the variables in
`.env_example` with your own and replace the filename with
`.env`.  
Then run the file `app.py`:
```shell
python app.py
```