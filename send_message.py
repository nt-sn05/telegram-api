import requests

from config import TOKEN


def send_message(chat_id: int, text: str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    
    raise Exception('Bad Request')


send_message(6506116243, 'Hi')
