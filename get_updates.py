from pprint import pprint

import requests

from config import TOKEN


def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    raise Exception('Bad Request')


data = get_updates()
pprint(data)

