 import time



# Superclass
class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def show_discipline(self):
        print('I am a student, but I have not chosen a discipline.')


# Subclass 1
class IT(Student):
    def __init__(self, name, student_id, language):
        Student.__init__(self, name, student_id)
        self.__language = language

    def get_language(self):
        return self.__language

    def show_discipline(self):
        print('I study Information Technology.')
        print('My main programming language is', self.__language)


# Subclass 2
class Business(Student):
    def __init__(self, name, student_id, major):
        Student.__init__(self, name, student_id)
        self.__major = major

    def get_major(self):
        return self.__major

    def show_discipline(self):
        print('I study Business.')
        print('My major is', self.__major)


# Subclass 3
class Accounting(Student):
    def __init__(self, name, student_id, software):
        Student.__init__(self, name, student_id)
        self.__software = software

    def get_software(self):
        return self.__software

    def show_discipline(self):
        print('I study Accounting.')
        print('I use', self.__software, 'for bookkeeping.')


def show_student(student):
    print('Name:', student.get_name())
    print('ID  :', student.get_student_id())
    student.show_discipline()          # correct version is called via polylmorphism
    print()


def main():
    start = time.time()
    it_student = IT('Rafi Miazi', 'K250249', 'Python')
    business_student = Business('Aisha Rahman', 'K250310', 'Marketing')
    accounting_student = Accounting('Daniel Chen', 'K250487', 'Xero')

    for student in [it_student, business_student, accounting_student]:
        show_student(student)

    print('Is the IT student also a Student?', isinstance(it_student, Student))
    end = time.time()
    print('Execution time:',end - start, 'seconds')


if __name__ == '__main__':
    main()