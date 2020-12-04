import xml.etree.ElementTree as ETree
import unittest

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()


# ЗАДАНИЕ № 1
# Вывести на печать  (в консоль) содержание каждого узла как первого, так и второго уровня,
# включая название тега, список атрибутов и значение
print(root.tag, root.keys(), root.text)
for i in root:                              # пробегаем по корню
    if len(i) == 0 and len(i.keys()) > 0:   # Если очередной элемент - одна сущность и имеет атрибуты
        print(i.tag, i.keys(), i.text)      # То напечатаем ее
    elif len(i) == 0:                       # если список атрибутов пуст
        print(i.tag, i.text)                # То напечатаем ее без атрибутов
    else:                                   # А если она - составная (из нескольких элементов)
        print(i.tag)                        # Напечатаем ее заголовок - тег
        for j in i:
            Attributes = j.keys()           # отдельно получим список атрибутов тега
            for Attribute in Attributes:    # пробежим по этому списку
                print('   ',Attribute, j.get(Attribute), j.text)    # напечатаем по отдельности каждый элемент (с отступом)
