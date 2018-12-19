from flask import Flask, request
import telegram
import os
import time
import datetime
from flask_sqlalchemy import SQLAlchemy

TOKEN = os.environ.get('TELEGRAM_TOKEN')
HOST = os.environ.get('HOST_URL')
PORT = int(os.environ.get('PORT', '8443'))

db = SQLAlchemy()
bot = telegram.Bot(TOKEN)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db.init_app(app)

    return app


if __name__ == '__main__':
    time.sleep(1)
    bot.setWebhook(url='%s/%s' % (HOST, TOKEN))
    app = create_app()

    @app.route('/' + TOKEN, methods=['POST'])
    def webhook():
        from models import User

        update = telegram.update.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat_id

        user = User.query.filter_by(chat_id=chat_id).first()
        if not user:
            user = User(chat_id=chat_id)
        user.update_date = datetime.datetime.now()
        user.save()

        bot.send_message(chat_id=chat_id, text='Gif every morning')

        return 'OK'

    app.run(host='0.0.0.0', port=PORT)
