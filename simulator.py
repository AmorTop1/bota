from role import bot
import json
import requests
from bs4 import BeautifulSoup


def parse_site(url, fields):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    result = []
    if fields is not None:
        for field in fields:
            tag_name = field.get("tag_name")
            class_name = field.get("class_name")
            indexes = field.get("indexes") if field.get("indexes") is not None and len(field.get("indexes")) > 0 else [0]
            a = soup.find_all(tag_name, class_=class_name)
            result.extend([item.text for index_, item in enumerate(a) if index_ in indexes])
    return result


def simulator():
    mess = ""
    with open("simulator_link.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for key, value in data.items():
        for item in value:
            url = ""
            fields = []
            for key_, value_ in item.items():
                if key_.startswith("url"):
                    url = value_
                elif key_.startswith("fields"):
                    fields = value_
                else:
                    break
            else:
                result = parse_site(url, fields)
                mess += "; ".join(result) + "\n\n"
                break
    return mess


@bot.message_handler(func=lambda x: x.text.startswith('Симулятори'))
def showArcades(message):
    bot.send_message(message.chat.id, simulator())


if __name__ == "__main__":
    bot.infinity_polling()
