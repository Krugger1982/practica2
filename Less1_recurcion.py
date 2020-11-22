def degree(N, M):
    ''' Функция которая считает возведение числа N в степень M'''
    if M == 0:
        return 1
    if M < 0:
        return 1 / degree(N, -M)        # для отрицатеьных степеней поведение немного другое
    if M == 1:
        return N
    return N * degree(N, M - 1)

def figure_counter(N):
    ''' Функция которая считает все цифры числа N'''
    if N < 10:
        return N
    return N % 10 + figure_counter(N // 10)

def length(List):
    List1 = List.copy()
    return length_recoursive(List1)

def length_recoursive(List):
    ''' Функция которая считает длину списка List'''
    try:
        List.pop(0)
    except IndexError:                  # отсекаем пустой список
        return 0
    else:
        return 1 + length_recoursive(List)

def palindrom(String):
    ''' Функция которая готовит строку к проверке и запускает проверку, является ли строка палиндромом'''

    String1 = ''.join(String.split())               # избавимся от пробелов
    String1 = String1.lower()                       # и приведем все буквы к одному регистру
    return palindr(String1)
    
def palindr(String):
    """ Рекурсивная функция проверяет является ли строка палидромом"""
    if len(String) < 2:
        return True
    return String[0] == String[-1] and palindr(String[1:-1])

#def even_numbered(List):
#    """ Печатает четные числа из списка List"""
#    try:
#        current = List[0]
#    except IndexError:
#        return
#    else:
#        if current % 2 == 0:
#            print(current, end=' ')
#        even_numbered(List[1:])

def even_numbered(List):
    """ Печатает четные числа из списка List"""
    if len(List) > 0:
        print(List[0], end=' ')
        even_numbered(List[1:])
        
def even_numbered_index(List, i=0):
    """ Печатает числа из списка List, находящиеся на четном индексе  """
    try:
        print (List[i], end=' ')
    except IndexError:
        return
    else:
        even_numbered_index(List, i + 2)
        
#def maximum_1(List):
#    """ Находит максимальное число в массиве (рекурсивно) """
#    if len(List) == 0:
#        return None
#    if len(List) == 1:
#        return List[0]
#    return max(List[0], maximum_1(List[1:]))
#
#def maximum_2(List):
#    """ Находит второе максимальное число в массиве """
#    List1 = List.copy()              # создадим копию списка чтоб не портить исходный, далее работаем с List1
#    Max = maximum_1(List1)           # Находим максимальное число
#    if Max is None:
#        return Max                   # Для пустого массива вернется  None
#    while maximum_1(List1) == Max:
#        List1.remove(Max)            # И удаляем все экземпляры этого числа из списка
#    return maximum_1(List1)          # После удаления находим максимальное число из оставшихся

def max_1_2(current, rezlist):
    ''' Функция для сравнения, на вход - текущее значение и список из 2х элементов, [MAX1, MAX2]'''
    if current > rezlist[0]:
        rezlist[0] = current                        # Увеличиваем MAX1
    elif current < rezlist[0] and current > rezlist[1]:
        rezlist[1] = current                        # Или увеличиваем MAX2
                                                    # В противном случае (если  current равен кому-либо из них или меньше обоих, ничего не делаем
    return rezlist                                  # На выходе - список ииз двух максимальных элементов (самый большой и 2-е место)
                                                     
def maximums_recursive(List):
    if len(List) == 0:                  # Для пустого списка ничего не получится
        return None
    if len(List) == 1:                  # Граничный случай
        return [List[0], List[0]]
    return max_1_2(List[0], maximums_recursive(List[1:]))

def maximum_2(List):
    result = maximums_recursive(List)
    if result is None or result[0] == result[1]:
        return None
    return result[1]
