import time
from threading import Thread
import random
import unittest

def little_summa(id, List, res):
    sum = 0
    for i in range(len(List)):
        sum += List[i]
    res[id] = sum

    
def Summa(N, List):
    results = {}
    Razmer = len(List) // N
    threads = N * [None]            # процессы будут храниться в списке, чтоб имена были уникальные
    for i in range(N-1):            # первые N-1 отрезков суммируются одинаково (размер отрезка -  результат целого деления len(List) // N)
        Id = 'ID' + str(i + 1)
        start = i * Razmer
        stop = start + Razmer
        threads[i] = Thread(target=little_summa, name='Thread N '+str(i+1), args=(Id, List[start:stop], results))
        threads[i].start()
        time.sleep(0.05)
    # Последний отрезок кроме обычного количества элементов дополнительно содержит в себе остаточные элементы которые в остатке от деления len(List) % N. 
    # Этот остаток может быть и нулевым, тогда размер отрезка будет как у всех остальных отрезков.
    Id = 'ID' + str(N)
    start = (N-1) * Razmer
    threads[N-1] = Thread(target=little_summa, name='Thread N '+str(N), args=(Id, List[start:], results))
    threads[N-1].start()

    time.sleep(0.001 * len(List)/N)          # необходимо выдержать паузу, чтоб все процессы успели отработать
                                             # размер паузы явно линейно зависит от размера суммируемого участка то есть от len(List)/N
    S = 0
    for keys in results:
        S += results[keys]                   # подсчитываем сумму "кусочков"
    return S


class Test_for_parallels(unittest.TestCase):

    def test_1(self):
        
        Testlist = []                       # и тестовый массив
        M = 600000           # размером M
        print('размер массива = ', M)
        N = 50          # задаем количество процессов
        print('процессов - ', N)
        for i in range(M):
            Testlist.append(round(random.uniform(100, 10000), 2))    # заполняем тестовый массив случайными веществ. числами
        
        Summa1 = Summa(N, Testlist)         # подсчет по частям
        Summa2 = 0                          # подсчет с циклом
        for i in Testlist:
            Summa2 +=i
        self.assertEqual(round(Summa1, 2), round(Summa2, 2))        # проверка  - функция работает!!!!
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass 
