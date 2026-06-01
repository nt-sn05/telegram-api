import requests

from config import TOKEN


def send_message(chat_id: int, text: str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text
    }
    requests.get(url, params=params)


send_message(6506116243, 'Hi')
