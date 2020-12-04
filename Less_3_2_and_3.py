# ЗАДАНИЕ 2
# Функция, выдающая список значений по тегу

def obhod1(tag, root, result):              # Функция для рекурсивного обхода иерархического дерева сущностей XML-структуры
    if  root.tag == tag:                    # если у текущего узла подходящий тег
        result.append(root.text)            # добавляем в список  его содержимое
    if len(root) > 0:                       # если текущий узел имеет дочерние узлы
        for i in root:                      # ищем в них
            result = obhod1(tag, i, result)
    return result

def the_values_in_tag(tag, parced_XML):     # Собчтвенно, требуемая функция
    Root = parced_XML.getroot()
    rezult = []
    result = obhod1(tag, Root, rezult)
    return result


#ЗАДАНИЕ 3
# Функция, которая считает количество узлов с заданным атрибутом

def obhod2(atribute, root, counter=0):
    if atribute in root.attrib.keys():      # проверяем есть ли у текущего узла искомый аттрибут 
        counter += 1                        # сдвигаем счетчик
    if len(root) > 0:                       # для вложенных "нижних" уровней
        for i in root:                      # пробегаем по детям
            counter += obhod2(atribute, i)  # все найденное в детях прибавляем к счетчику
    return counter

def attribute_counter(atribute, parced_XML):
    Root = parced_XML.getroot()
    return obhod2(atribute, Root)

