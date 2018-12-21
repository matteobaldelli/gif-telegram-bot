# Gif Telegram Bot

This repository is a test for a telegram bot to send a gif every day hosted by heroku
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project you must have installed these programs:
* [python](https://www.python.org/)
* [pipenv](https://github.com/pypa/pipenv)
* [postgresql](https://github.com/postgres/postgres)

### Installing and serve

Create a .env file in project folder and add the following:

```
TELEGRAM_TOKEN="TOKEN-TELEGRAM-BOT"
HOST_URL="URL-FOR-WEBHOOK"
DATABASE_URL="postgresql://localhost/test"
```
after create a .env file go to the console

```
$ pipenv install
$ pipenv run python manage.py db upgrade
$ pipenv run python app.py
```

## Built With

* [flask](https://github.com/pallets/flask)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
