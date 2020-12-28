import json
import requests


response = requests.get('https://api.github.com/users/Krugger1982')

if response.status_code == 200:
    with open('1.txt', 'wt') as page_file:
        result = json.loads(response.text)
else:
    print("ERROR",response.status_code)
for keys in result:
    print(keys, result[keys])
