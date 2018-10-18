import os

BOT_TOKEN = os.environ.get('ECHO_BOT_TOKEN')
BOT_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/{{}}"