import xml.etree.ElementTree as ETree
import unittest
import xml_2
import os.path


class Tests_xml(unittest.TestCase):
       
    def test_1(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'demo.xml')             # Так интерпретатор найдет файл "demo.xml"
        xml1 = ETree.parse(TESTDATA_FILENAME)
        Root = xml1.getroot()
        Testlist = ['name', 'age', 'sex', 'language', 'pc_item']                                                # список тегов, имеющих значения
        Results = [[Root[0]], [Root[1]], [Root[2]], [Root[3][0], Root[3][1], Root[3][2]], [Root[4][0], Root[4][1], Root[4][2], Root[4][3]]] # список соотв. узлов
        for i in range(len(Testlist)):
            self.assertEqual(xml_2.the_values_in_tag(Root, Testlist[i]),  Results[i])              # проверка - в соответствующем теге - соответствующие значения
        self.assertEqual(xml_2.the_values_in_tag(Root, 'weight'),  [])                             # проверка - поиск в несуществующем теге даст пустой список


    def test_2(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'demo.xml')        
        xml1 = ETree.parse(TESTDATA_FILENAME)
        Root = xml1.getroot()
        self.assertEqual(xml_2.parent(Root[0], xml1), Root)                   # проверка - у всех "детей" корневого узла"родитель" - Root
        self.assertEqual(xml_2.parent(Root[1], xml1), Root)
        self.assertEqual(xml_2.parent(Root[2], xml1), Root)
        self.assertEqual(xml_2.parent(Root[3], xml1), Root)
        self.assertEqual(xml_2.parent(Root[4], xml1), Root)
        self.assertEqual(xml_2.parent(Root[3][0], xml1), Root[3])               # проверка - у всех "детей"  узла langages - "родитель" - Root[3]
        self.assertEqual(xml_2.parent(Root[3][1], xml1), Root[3])
        self.assertEqual(xml_2.parent(Root[3][2], xml1), Root[3])
        self.assertEqual(xml_2.parent(Root[4][0], xml1), Root[4])               # проверка - у всех "детей"  узла pc - "родитель" - Root[4]
        self.assertEqual(xml_2.parent(Root[4][1], xml1), Root[4])
        self.assertEqual(xml_2.parent(Root[4][2], xml1), Root[4])
        self.assertEqual(xml_2.parent(Root[4][3], xml1), Root[4])

        New_Element = ETree.Element('something') 
        self.assertEqual(xml_2.parent(New_Element, xml1), None)                 # проверка - не внесенный в этот документ узел не имеет родителя


    def test_3(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'demo.xml')        
        xml1 = ETree.parse(TESTDATA_FILENAME)
        Root = xml1.getroot()        
        self.assertEqual(xml_2.the_values_in_tag(Root, 'age'),  [Root[1]])      # проверяем - узел 'age' существует
        xml_2.kill_item('age', xml1)                                            # удаляем его
        self.assertEqual(xml_2.the_values_in_tag(Root, 'age'),  [])             # проверка - узел 'age' исчез

        
        self.assertEqual(xml_2.the_values_in_tag(Root, 'languages'),  [Root[2]]) # проверяем - узел 'language' существует (теперь он на позиции Root[2])
        xml_2.kill_item('languages', xml1)                                       # удаляем его
        self.assertEqual(xml_2.the_values_in_tag(Root, 'languages'),  [])        # проверка - узел 'language' исчез
        self.assertEqual(xml_2.the_values_in_tag(Root, 'language'),  [])         # и исчезли все его "дети"
                
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
