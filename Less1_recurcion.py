def degree(N, M):
    ''' Функция которая считает возведение числа N в степень M'''
    if M == 0:
        return 1
    if M < 0:
        return 1 / degree(N, -M)
    if M == 1:
        return N
    return N * degree(N, M - 1)

def figure_counter(N):
    ''' Функция которая считает все цифры числа N'''
    if N < 10:
        return N
    return N % 10 + figure_counter(N // 10)


def length(List):
    ''' Функция которая считает длину списка List'''
    try:
        List.pop(0)
    except IndexError:
        return 0
    else:
        return 1 + length(List)

def palindrom(String):
    ''' Функция которая готовит строку к проверке и запускает проверку, является ли строка палиндромом'''

    String = ''.join(String.split())            # избавимся от пробелов
    String = String.lower()                     # и приведем все буквы к одному регистру
    return palindr(String)
    
def palindr(String):
    """ Рекурсивная функция проверяет является ли строка палидромом"""
    if len(String) < 2:
        return True
    return String[0] == String[-1] and palindr(String[1:-1])

def even_numbered(List):
    """ Печатает четные числа из списка List"""
    try:
        current = List.pop(0)
    except IndexError:
        return
    else:
        if current % 2 == 0:
            print(current, end=' ')
        even_numbered(List)

def even_numbered_index(List, i=0):
    """ Печатает числа из списка List, находящиеся на четном индексе  """
    try:
        print (List[i], end=' ')
    except IndexError:
        return
    else:
        even_numbered_index(List, i + 2)
    
def maximum_1(List):
    """ Находит максимальное число в массиве (рекурсивно) """
    if len(List) == 0:
        return None
    if len(List) == 1:
        return List[0]
    return max(List[0], maximum_1(List[1:]))

def maximum_2(List):
    """ Находит второе максимальное число в массиве """
    Max = maximum_1(List)           # Находим максимальное число
    if Max is None:
        return Max
    while maximum_1(List) == Max:
        List.remove(Max)            # И удаляем все экземпляры этого числа из массива
    return maximum_1(List)          # После удаления находим максимальное число из оставшихся
