import requests
from urllib.parse import urlencode

from settings import BOT_TOKEN, BOT_API_URL

# Working with API

def get_updates(chat_id=None):
	endpoint = "getUpdates"
	if chat_id is not None:
		endpoint = endpoint + "?" + urlencode({'chat_id': chat_id})
	url = BOT_API_URL.format(endpoint)
	response = requests.get(url).json()
	return response


def send_message(chat_id, text):
	url = BOT_API_URL.format("sendMessage")
	payload = {"chat_id": chat_id, "text": text}
	return requests.post(url, json=payload).json()


def get_last_update():
	response = get_updates()
	if response['ok']:
		return response['result'][-1]
	return None