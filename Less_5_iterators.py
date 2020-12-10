class List2:
    def __init__(self, start):
        self.start = start                              # задаем в конструкторе стартовое значение
        
    def __iter__(self):
        self.count = 0                                  # счетчик обращений к итератору
        return self

    def __next__(self): 
        current = self.start
        self.start = self.start * 2
        self.count += 1                                  # так как счетчик обращений начнется с 1
        if self.count < 10:                              # вводим ограничитель (10, включительно)
            return current
        raise StopIteration
    


class List2_2:
    def __init__(self, start, stop, infinity):
        self.start = start                              # задаем в конструкторе стартовое значение
        self.infinity_start = start                     # и значение к которому аозвращаться по окончании круга
        self.stop = stop                                # ограничитель тоже задается на входе
        self.infinity = infinity                        # флаг бесконечности
        self.count = 0
        
    def __iter__(self):
        return self

    def __next__(self): 
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count < self.stop:                  # до ограничителя просто возвращаем текущее значение 
            return current
        elif self.infinity:                         # если достигнут ограничитель и стоит флаг "бесконечность"
            self.count = 0                          # обнуляем счетчик 
            self.start = self.infinity_start        # обнуляем (приводим к исходному значению) параметр start
            return current                          # и возвращаем текущее значение
        else:
            raise StopIteration                     
