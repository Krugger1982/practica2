import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)
with open ('json_file.json', 'a') as file:
    Answers = {}
    for i in result:
        json.dump(i, file)                  # записываем все записи из ответа в файл
        if i['userId'] not in Answers:      # Если найден новый пользователь
            Answers[i['userId']] = {'Tasks':[], 'completed':0}       # Создаем для него новую запись в словаре
            # (Ключ - имя польз., содержание - список оригиналтных задач и счетчик выполненных)
        if i['id'] not in Answers[i['userId']]['Tasks'] and i['completed']:
            Answers[i['userId']]['Tasks'].append(i['id'])
            Answers[i['userId']]['completed'] += 1                      # и учитываем выполненную первую задачу
            
        elif i['id'] not in Answers[i['userId']]['Tasks']:               # а если ориг. задача не выполнена, то просто добавляем ее
            Answers[i['userId']]['Tasks'].append(i['id'])

# ВЫВОД ОТВЕТОВ

print ('Количество пользователей - ', len(Answers))
for i in Answers:
    print ('Пользователь ', i, ' Оригинальных здач - ', len(Answers[i]['Tasks']), ' Из них выполнено -', Answers[i]['completed'] )
