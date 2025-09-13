class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    #создаём метод добавления оценок
    def add_grade(self, grade):
        #Проверяем, что оценка от 0 до 10
        if 0 <= grade <= 10:     
            # Добавляем оценку в список 
            self.grades.append(grade)  
        #Если оценка не соответствует формату (не может быть оценкой), выводим ошибку
        else:
            print(f"Ошибка: {grade} не является оценкой")

    #создаем метод вычисления среднего балла
    def get_average(self):
        #если оценок нет (список пустой), выводим сообщение об ошибке
        if not self.grades: 
            print("Ошибка: у студента ещё нет оценок")
            return None
        else:
            #находим средний балл (сумма оценок/количество)      
            return sum(self.grades) / len(self.grades)
        
    #создаем метод вывода информации о студенте
    def display_info(self):
        print(f"Информация о студенте {self.name}")
        print(f"Имя: {self.name}")
        print(f"ID: {self.student_id}")
        #если оценок нет (список пустой), выводим сообщение и не вычисляем средний (иначе ошибка)
        if not self.grades:
            print("Нет оценок")
        #если оценки есть, выводим их и средний балл
        else:
            #преобразуем оценки в строку, соединяем их с разделителем пробел
            print(f"Оценки: {' '.join(map(str, self.grades))}")
            print(f"Средний балл: {self.get_average()}")

    def __str__(self): 
        #если список оценок пустой, сразу выводим об этом сообщение во избежание ошибок
        if not self.grades:
            return f"Студент - {self.name}, id - {self.student_id}; нет оценок"
        #если оценки есть, выводим также их и средний балл
        else:
            return f"Студент - {self.name}, id - {self.student_id}; средний балл - {self.get_average():.2f}, оценки - {self.grades}"

    def __eq__(self,other):
        #проверяем принадлежность к классу Student
        if isinstance(other,Student):
            #если объект сравнения принадлежит классу Student, сравниваем его (при совпадении true, иначе false)
            return self.student_id==other.student_id
        #если не принадлежит, сразу false
        return False

    def __len__(self):
        return len(self.grades)

#тестирование работы класса, этот код защищен от импортирования в другие файлы
if __name__ == "__main__":
    # Создаем студента 1 по имени Арина Теймурова с id 1132243259
    stu_1 = Student("Арина Теймурова", "1132243259")
    
    # Добавляем ему оценки
    stu_1.add_grade(0)
    stu_1.add_grade(9)
    stu_1.add_grade(10)
    #пробуем добавить число, не являющееся оценкой
    stu_1.add_grade(11)  
    # Выводим информацию о студенте 1
    stu_1.display_info()
    print(f"Количество оценок у студента {stu_1} - {len(stu_1)}")
    
    # Создаем еще одного студента
    stu_2 = Student("Лев Сигал", "060823")
    stu_2.add_grade(10)
    stu_2.add_grade(9)
    #выводим информацию в виде столбцов и строки (оба метода) 
    stu_2.display_info()
    print(stu_2)

    #для проверки создаем студента с id как у 1
    stu_same_id = Student("Другой студент", "1132243259")
    #для проверки создаем переменную не из Student
    not_student = 10
    #для проверки создаем студента без оценок 
    stu_none = Student("Студент без оценок", "0")

    #выводим информацию о студенте без оценок
    print(stu_none)
    stu_none.display_info()

    #сравниваем студентов с разными id
    print(f"stu_1 == stu_2: {stu_1 == stu_2}")
    #сравниваем студентов с одинаковым id
    print(f"stu_1 == stu_same_id: {stu_1 == stu_same_id}")
    #сравниваем с не Student
    print(f"stu_1 == not_student: {stu_1 == not_student}")
