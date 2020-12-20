def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
#        print(id, sum)
        if x < n - 1:
            yield
        else:
            yield sum
            
def generators(Numbers):
    Result = {}                                                         # создаем словарь ответов
    Processes = []                                                      # и список с именами генераторов
    for Number in Numbers:                                             # пробегая по входному списку
        ID = 'id' + str(Number)                                        # присваиваем имена процессам
        Result[ID] = None                               # создаем под очередного генератора ячейку в словаре ответов
        Processes.append(long_process(ID, Number))      # производим "запуск" очередного генератора и запоминаем его имя  в списке
    # ячейки в словаре хранятся в той же последовательности, в какой они туда добавлялись
    # то есть в той же последовательности, что и в списке Processes
    Results = list(Result.keys())
    for i in range(max(Numbers)):                                               # количество проходов равно максимальному значению из входного списка
        for current in range(len(Numbers)):                                     # пробегаем по списку чисел
            ID = 'id' + str(Numbers[current])                
            if Result[ID] is None:
                Result[ID] = next(Processes[current])                           # для каждого в этой итерации считаем очередную сумму
    return Result
