

import time


class Student:
    # initiator on constructor method
    def __init__(self, name, student_id, course, marks):
        self.__name = name                 
        self.__student_id = student_id
        self.__course = course
        self.__marks = marks

    # Mutator methods 
    def set_name(self, name):
        self.__name = name

    def set_course(self, course):
        self.__course = course

    def set_marks(self, marks):
        self.__marks = marks

    # Accessor methods for returning data
    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    def get_marks(self):
        return self.__marks

    def get_grade(self):
        if self.__marks >= 80:
            return 'High Distinction'
        elif self.__marks >= 70:
            return 'Distinction'
        elif self.__marks >= 50:
            return 'Pass'
        else:
            return 'Fail'

    # __str__  method for custom print fkuntion output
    def __str__(self):
        return ('Name   : ' + self.__name + '\n' +
                'ID     : ' + self.__student_id + '\n' +
                'Course : ' + self.__course + '\n' +
                'Marks  : ' + str(self.__marks) + '\n' +
                'Grade  : ' + self.get_grade())


def main():
    start = time.time()
    # Creating objects from the student class
    student1 = Student('Rafi Miazi', 'K250249', 'Bachelor of IT', 88)
    student2 = Student('Aisha Rahman', 'K250310', 'Bachelor of IT', 74)

    print(student1)
    print()
    print(student2)

    # Using a mutator to change the data, then an accessor to read it back
    student2.set_marks(81)
    print()
    print('Updated marks for', student2.get_name(), '->', student2.get_marks())
    print('New grade ->', student2.get_grade())

    end = time.time()
    print('Execution time:', end - start, 'seconds')


if __name__ == '__main__':
    main()