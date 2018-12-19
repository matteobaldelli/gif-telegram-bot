import os
import requests
import telegram
from telegram.error import Unauthorized
from flask_sqlalchemy import SQLAlchemy

from models import User
from app import create_app

TOKEN = os.environ.get('TELEGRAM_TOKEN')

db = SQLAlchemy()
bot = telegram.Bot(TOKEN)
app = create_app()
app.app_context().push()

users = User.query.all()

url = 'https://api.giphy.com/v1/stickers/random'

params = dict(
    api_key='dc6zaTOxFJmzC',
    tag='cute-cat'
)

resp = requests.get(url=url, params=params)
data = resp.json()

for user in users:
    try:
        bot.send_animation(chat_id=user.chat_id, animation=data['data']['image_mp4_url'])
    except Unauthorized:
        user.delete()
