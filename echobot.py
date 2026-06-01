import time

import requests

from config import TOKEN


def get_updates(offset: int | None = None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"offset": offset}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["result"]

    raise Exception("Bad Request")


def send_message(chat_id: int, text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.get(url, params=params)


def main():
    update_id = None

    while True:
        for update in get_updates(offset=update_id):
            if update.get("message"):
                if update["message"].get("text"):
                    send_message(
                        chat_id=update["message"]["chat"]["id"],
                        text=update["message"]["text"],
                    )

            update_id = update["update_id"] + 1

        time.sleep(1)


main()
