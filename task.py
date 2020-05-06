import person
import teacher
import student

# Создать иерархию классов Person–Student–Teacher. Каждый класс
# должен содержать свойства, а также виртуальную функцию Print и
# переопределенную функцию ToString( ). Основная программа должна
# создавать массив объектов Person или их наследников, после чего выдавать
# его на экран. У каждого объекта класса Teacher должен быть список
# объектов класса Students, которыми он руководит, у каждого объекта
# класса Student – объект класса Teacher, который им руководит.


def main():
    print("Task script")

    teacher1 = teacher.Teacher("Valentina",  "Petrovna", 48)
    teacher2 = teacher.Teacher("Halina", "Ivanovna", 44)

    student1 = student.Student("Alesha", "Taras", 17)
    student1.teacher = teacher1
    student2 = student.Student("Gotama", "Gulyaka", 10)
    student2.teacher = teacher1
    student3 = student.Student("Alesha", "Pupkin", 15)
    student3.teacher = teacher1
    student4 = student.Student("Alexandr", "Nastya", 16)
    student4.teacher = teacher2
    student5 = student.Student("Dimitry", "Shturmovik", 33)
    student5.teacher = teacher2

    teacher1.students = [student1, student2, student3]
    teacher2.add_student(student4)
    teacher2.add_student(student5)

    peoples = [teacher1, teacher2, student1, student2, student3, student4, student5]

    for people in peoples:
        people.print()


if __name__ == '__main__':
    main()
