def maximums_recursive(MAX1, MAX2, List):
    if len(List) == 0:                  # Для пустого списка ничего не делаем, возвращаем пару MAX1 и MAX2
        return [MAX1, MAX2]
    if List[0] > MAX1:
        MAX2 = MAX1
        MAX1 = List[0]
    elif MAX1 > List[0] and List[0] > MAX2 or MAX2 == MAX1 and MAX2  > List[0]:
        MAX2 = List[0]
    return maximums_recursive(MAX1, MAX2, List[1:])

def maximum_2(List):
    if len(List) == 0:
        return None
    result = maximums_recursive(List[0], List[0], List[1:])
    if result[0] == result[1]:
        return None
    return result[1]
    
    import unittest
    
    
class Tests_for_recoursive_functions(unittest.TestCase):
        
    def test_Maximum_2(self):
        TestList = []
        self.assertEqual(maximum_2(TestList), None)                 # Проверка пустого списка, должен вернуться None
        TestList = [1]
        self.assertEqual(maximum_2(TestList), None)                 # Проверка с единственным членом, должен вернуться None
        TestList = [10, 10]
        self.assertEqual(maximum_2(TestList), None)                 # Проверка списка с одинаковыми членами, должен вернуться None
        TestList = [100, 99, 56, 59, 31, 98, 100, 6, 10, 100, 100]
        self.assertEqual(maximum_2(TestList), 99)                   # Проверка списка различных значений с повтором максимального
        
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
