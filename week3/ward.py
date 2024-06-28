from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, yob) -> None:
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name=name, yob=yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist) -> None:
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject) -> None:
        super().__init__(name=name, yob=yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.subject}")


class Ward:
    def __init__(self, name) -> None:
        self.__name = name
        self.__listPeople = []

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def count_doctor(self):
        num_doctor = 0
        for p in self.__listPeople:
            if isinstance(p, Doctor):
                num_doctor = num_doctor + 1
        return num_doctor

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()


if __name__ == '__main__':
    student1 = Student(name="studentZ2023", yob=2011, grade="6")
    assert student1._yob == 2011
    student1.describe()

    teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
    assert teacher1._yob == 1991
    teacher1.describe()

    doctor1 = Doctor(name="doctorZ2023", yob=1981,
                     specialist="Endocrinologists")
    assert doctor1._yob == 1981
    doctor1.describe()

    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    assert ward1.count_doctor() == 1
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1.add_person(doctor2)
    print(ward1.count_doctor())
