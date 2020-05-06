import person
import teacher


class Student(person.Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.teacher = list()

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        self._teacher = value

    def print(self):
        print(self.__str__())
        print("\tHis\\her teacher:\n\t\t" + str(self.teacher))

    def __str__(self):
        return "{}".format(super(Student, self).__str__())


def main():
    teach = teacher.Teacher("Halina", "Ivanovna", 44)
    stud = Student("Alesha", "Taras", 17)
    stud.teacher = teach

    stud.print()


if __name__ == '__main__':
    main()
