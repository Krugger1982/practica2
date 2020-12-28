import json
import requests



url = 'https://api.vk.com/method/friends.getOnline?v=5.52&access_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# токен я по соображениям безопасности отсюда убрал

response = requests.get(url)

if response.status_code == 200:
    with open('1.txt', 'wt') as page_file:
        result = json.loads(response.text)
else:
    print("ERROR",response.status_code)
for keys in result:
    print(keys, result[keys])
