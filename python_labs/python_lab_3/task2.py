#импортируем уже созданный класс из задания 1
from task1_5 import Student

#создаем класс с атрибутами имя, возраст и функцией строкового вывода
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Имя: {self.name}, возраст: {self.age}"

#создаем дочерний класс с атрибутами имя, возраст, предмет
class Teacher(Person):
    def __init__(self, name, age, subject):
         super().__init__(name, age)
         self.subject = subject
         #создаем пустой список для хранения студентов
         self.students = []
    
    #создаем функцию добавления студентов
    def add_student(self, student):
        #проверяем, является ли объект студентом
        if isinstance(student, Student):
            #проверяем, есть ли студент в списке у преподавателя
            if student not in self.students:
                #если нет, добавляем и сообщаем
                self.students.append(student)
                print(f"Студент {student.name} записан к преподавателю {self.name}")
            #если да, не добавляем ещё раз
            else:
                print(f"Студент {student.name} уже записан к преподавателю {self.name}")
        else:
            print("Можно добавить только студента!")
    
    #создаем функцию удаления студента
    def remove_student(self, student):
        #проверяем, является ли объект студентом
        if isinstance(student, Student):
            #если да, проверяем, есть ли студент в списке
            if student not in self.students:
                #если нет, не можем удалить и сообщаем
                print(f"Студент {student.name} не записан к преподавателю {self.name}")
            #если да, удаляем
            else:
                self.students.remove(student)
                print(f"Студент {student.name} удалён из списка преподавателя {self.name}")
        else:
            print("Можно удалить только студента!")
    
    #создаем функция для вывода списка студентов у преподавателя
    def list_students(self):
        #если список пустой, сообщаем
        if len(self.students) == 0:
            print(f"К преподавателю {self.name} не записан ни один студент")
        #если студенты есть, выводим имя каждого элемента списка
        else:
            print(f"Список студентов, записанных к преподавателю {self.name}:")
            for student in self.students:
                print(student.name)

    #создаем функцию для строкового вывода информации о преподавателе
    def __str__(self):
        return f"Преподаватель: {self.name}, Предмет: {self.subject}, Студентов: {len(self.students)}"

#защищаем демонстративный код от выполнения при импортировании  
if __name__ == '__main__':

    #создаем преподавателя, студентов и добавляем их в список, выводим
    python_teacher = Teacher("Максим Кириллович", 18, "python")
    stu_1 = Student("Арина Теймурова", "1132243259")
    stu_2 = Student("RUDN foreign student", "11111111")
    python_teacher.add_student(stu_1)
    python_teacher.add_student(stu_2)
    python_teacher.list_students()

    #удаляем одного, выводим информацию уже в строке
    print("Обновление списка студентов")
    python_teacher.remove_student(stu_1)
    print(python_teacher)
