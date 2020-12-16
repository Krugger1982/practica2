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
    for i in range(N):              
        Id = 'ID' + str(i + 1)
        start = i * Razmer
        stop = start + Razmer
        if i == N-1:                    # некрасивая проверка
            stop = len(List)            # последний отрезок захватит еще и остаток (если len(List) на N делится не нацело)
        threads[i] = Thread(target=little_summa, name='Thread N '+str(i+1), args=(Id, List[start:stop], results))
        threads[i].start()
        time.sleep(0.05)
    Is_counting = True
    while Is_counting:
        for current_thread in threads:
            Is_counting = Is_counting and current_thread.is_alive()     # в бесконечном цикле проверяем, работает ли текущий процесс
    S = 0
    for keys in results:
        S += results[keys]                   # подсчитываем сумму "кусочков"
    return S


class Test_for_parallels(unittest.TestCase):

    def test_1(self):
        
        Testlist = []                       # и тестовый массив
        M = 1000000           # размером M
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
