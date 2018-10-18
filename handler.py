from time import sleep

from api_calls import get_last_update, send_message


last_update = None


def handler():
	global last_update
	retrieved_update = get_last_update()
	if retrieved_update is not None and last_update != retrieved_update:
		last_update = retrieved_update
		print(retrieved_update)
		send_message(retrieved_update['message']['chat']['id'],
			         retrieved_update['message']['text'])


if __name__ == '__main__':
	while(True):
		handler()
		sleep(10)
