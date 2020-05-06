

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        try:
            str(value)
        except ValueError:
            print("Surname must be string")
            return
        self._surname = str(value)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            int(value)
        except ValueError:
            print("Age must be integer")
            return
        if int(value) < 0:
            print("Age must be positive")
        else:
            self._age = int(value)

    def print(self):
        print(self.__str__())

    def __str__(self):
        return "Name: {},\t Surname: {},\t Age: {}.".format(self.name, self.surname, self.age)


def main():
    print("Pearson test")
    persons = [Person("Alex", "Shevchenko", 20), Person("Gotama", 1, 55)]
    persons[0].__str__()
    for person in persons:
        person.print()


if __name__ == '__main__':
    main()
