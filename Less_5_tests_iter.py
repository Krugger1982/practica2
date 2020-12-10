import unittest
import Less5_iter

class Tests_for_iterators(unittest.TestCase):
        
    def test_1(self):
        Start = 5
        TestList = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560]
        result = Less5_iter.List2(Start)
        k = 0                                               # для пробега по массиву Testlist
        for i in result:
            self.assertEqual(i, TestList[k])                # проверка очередного элемента
            k += 1                                          # сдвигаем позицию Testlist
        self.assertEqual(k, 9)                              # проверяем размер полученного списка List2

    def test_2_not_infinity(self):
        ''' Тест для проверки небесконечного итератра'''
        Start = 5
        Stop = 10
        TestList = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560]
        result = Less5_iter.List2_2(Start, 5, False)
        k = 0                                               # для пробега по массиву Testlist
        for i in result:
            self.assertEqual(i, TestList[k])                # проверка очередного элемента
            k += 1                                          # сдвигаем позицию Testlist    

    def test_2_infinity(self):
        ''' Тест для проверки бесконечного итератра'''
        Start = 5
        Stop = 10
        N = 3 * Stop                                        # для проверки возьмем троекратный проход "по кругу"
        
        TestList = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560]
        result = Less5_iter.List2_2(Start, Stop, True)
        for k in range(N):
            current = next(iter(result))
            self.assertEqual(current, TestList[k % Stop])   # проверка очередного элемента (при превышении параметра Stop значения пойдут по кругу с начала)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass    
