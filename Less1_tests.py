import unittest
class Tests_for_recoursive_functions(unittest.TestCase):
        
    def test_1_degree(self):
        self.assertEqual(0.25, degree(2, -2))               # проверка для отрицательной степени
        self.assertEqual(1, degree(5, 0))                   # проверка дя степени равной 0
        self.assertEqual(1024, degree(2, 10))               # проверка для положительной степени

    def test_2_figure_counter(self):
        self.assertEqual(0, figure_counter(0))                  
        self.assertEqual(10, figure_counter(1111111111))
        self.assertEqual(45, figure_counter(123456789))                 

    def test_3_length(self):
        self.assertEqual(0, length([]))                                                         # проверка для пустого списка
        self.assertEqual(4, length([256, 'string', ('tuple', 16), ['list', 12, 13]]))           # проверка для непустого списка

    def test_4_palindrom(self):
        self.assertTrue(palindrom('арозазора'))                                # проверка для палиндрома
        self.assertFalse(palindrom('а роза упала'))                             # проверка для непалиндрома
        self.assertTrue(palindrom('а роза упала на лапу азора'))                # проверка для палиндрома с пробелами
        self.assertTrue(palindrom('А Роза упала на лапу Азора'))                # проверка для палиндрома с пробелами и разными регистрами

    def test_5_even_numbered(self):
        print()
        even_numbered ([1, 6, 8, 2, 3, 5, 12])

    def test_6_even_numbered_index(self):
        print()
        even_numbered_index ([1, 6, 8, 2, 3, 5, 12])

    def test_7_Maximum_2(self):
        TestList = []
        self.assertEqual(maximum_2(TestList), None)                 # Проверка пустого списка, должен вернуться None
        TestList = [1]
        self.assertEqual(maximum_2(TestList), None)                 # Проверка с единственным членом, должен вернуться None
        TestList = [10, 10]
        self.assertEqual(maximum_2(TestList), None)                 # Проверка списка с одинаковыми членами, должен вернуться None
        TestList = [100, 98, 56, 59, 31, 99, 100, 6, 10]
        self.assertEqual(maximum_2(TestList), 99)                   # Проверка списка различных значений с повтором максимального
        
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
