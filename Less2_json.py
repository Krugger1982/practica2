import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)
with open ('json_file.json', 'a') as file:
    json.dump(result, file)                  # записываем все записи из ответа в файл
Answers = {}
for i in result:
    if i['userId'] not in Answers:                              # Если найден новый пользователь
        Answers[i['userId']] = {'Tasks':[], 'completed':0}      # Создаем для него новую запись в словаре
        # (Ключ - имя польз., содержание - список оригиналтных задач и счетчик выполненных)
    if i['id'] not in Answers[i['userId']]['Tasks']:
        Answers[i['userId']]['Tasks'].append(i['id'])           # если задача оригинальная, добавляем ее в список задач            
    if  i['completed']:
        Answers[i['userId']]['completed'] += 1              # и учитываем выполнена ли она
        
# ВЫВОД ОТВЕТОВ

print ('Количество пользователей - ', len(Answers))
for i in Answers:
    print ('Пользователь ', i, ' Оригинальных здач - ', len(Answers[i]['Tasks']), ' Из них выполнено -', Answers[i]['completed'] )
