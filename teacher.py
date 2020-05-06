import person
import student


class Teacher(person.Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.students = list()

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, value):
        self._students = value

    def add_student(self, value):
        if type(value) == student.Student:
            self.students.append(value)
        else:
            print("Cannot add object typeof " + str(type(value)) + " to students")
            return False

    def remove_student(self, value):
        if type(value) == student.Student:
            try:
                self.students.remove(value)
            except ValueError:
                print("The teacher does not have such a student")
                return False
        else:
            print("Cannot remove object typeof " + type(value) + " from students")
            return False

    def print(self):
        print(self.__str__())
        print("\tHis\\her students:")
        for stud in self.students:
            print("\t\t" + str(stud))

    def __str__(self):
        return "Teacher: {}".format(super(Teacher, self).__str__())


def main():
    studs = [student.Student("Gotama", "Gulyaka", 10), student.Student("Alesha", "Pupkin", 15)]
    teach = Teacher("Valentina",  "Petrovna", 48)
    teach.students = studs

    teach.print()


if __name__ == '__main__':
    main()
