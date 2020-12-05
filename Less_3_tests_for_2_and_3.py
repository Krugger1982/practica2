import xml.etree.ElementTree as ETree
import unittest
import xml_1_23
import os.path


class Tests_archives(unittest.TestCase):
       
    def test_1(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'demo.xml')             # Так интерпретатор найдет файл "demo.xml"
        xml1 = ETree.parse(TESTDATA_FILENAME)
        Testlist = ['name', 'age', 'sex', 'language', 'pc_item']                                                # список тегов, имеющих значения
        Results = [['Petya'], ['23'], ['true'], ['9', '7', '8'], ['Linux', 'Intel Core i7-8700', '64', '5000']] # список их значений
        for i in range(len(Testlist)):
            self.assertEqual(xml_1_23.the_values_in_tag(Testlist[i],xml1),  Results[i])              # проверка - в соответствующем теге - соответствующие значения
        self.assertEqual(xml_1_23.the_values_in_tag('weight',xml1),  [])                             # проверка - поиск в несуществующем теге даст пустой список

    def test_2(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'demo.xml')        
        xml1 = ETree.parse(TESTDATA_FILENAME)
        self.assertEqual(xml_1_23.attribute_counter('name', xml1), 7)                # проверка - всего в файле 7 узлов с аттрибутом 'name'
        Root = xml1.getroot()   
        self.assertEqual(xml_1_23.obhod2('name', Root[3]), 3)                        # а в ветке 'languages' - 3 таких узла
        self.assertEqual(xml_1_23.obhod2('name', Root[4]), 4)                        # а в ветке 'pc' - 4

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
