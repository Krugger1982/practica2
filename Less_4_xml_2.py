import xml.etree.ElementTree as ETree

# ЗАДАНИЕ 1
# Функция, выдающая список значений по тегу

def the_values_in_tag(root, tag):    
    result=[]
    for item in root.iter():                        # Обходим документ
        if  item.tag == tag:                        # если у текущего узла подходящий тег
            result.append(item)                     # добавляем узел в список
    return result


#ЗАДАНИЕ 2
# Функция, которая ищет родителя заданного узла

def parent (Element, parced_XML):
    root = parced_XML.getroot()
    for item in root.iter():                # обходим все узлы
        if Element in item:                 # находим "родителя" (Element - это его дочерний узел)
            return item                     # и возвращаем его (родителя)
    return None                             # Если не нашли, возвращаем None

# ЗАДАНИЕ 3
# Функция, которая удаляет узлы по заданому тегу

def kill_item(tag, parced_XML):
    root = parced_XML.getroot()
    for item in root.iter():                    # обходим весь документ 
        candidacy = item.findall(tag)           # каждый очередной узел проверяем на предмет наличия в детях заданого тега
        if len(candidacy) > 0:                  # Если таковые найдутся (список не пуст)
            for candidate in candidacy:         # то пробегаем по списку 
                item.remove(candidate)          # и удаляем их
