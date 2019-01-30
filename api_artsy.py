import requests
import json
import sys

client_id = '************'
client_secret = '************'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}



artists_dict = {}
for line in sys.stdin:
    line = line.strip()

    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/{}".format(line), headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)

    artists_dict[j['sortable_name']] = int(j['birthday'])

for name, birthday in sorted(artists_dict.items(), key=lambda x: (x[1], x[0])):
    print(name)