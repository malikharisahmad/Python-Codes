class Person:
    def __init__(self,name,contact_number):
        self.__name=name
        self.__contact_number=contact_number

    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,d):
        self.__name=d
    
    @property 
    def contact_number(self):
        return self.__contact_number
    @contact_number.setter
    def contact_number(self,d):
        self.__contact_number=d
    
    def __str__(self):
        vstr=""
        vstr+=str(self.__name)
        vstr+=" , "
        vstr+=str(self.__contact_number)
        return vstr


class Student(Person):
    def __init__(self,name,contact_number,department,semester):
        super().__init__(name,contact_number)
        self.__department=department
        self.__semester=semester
    
    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self,d):
        self.__department=d
    
    def __str__(self):
        vstr=""
        vstr+=super().__str__()
        vstr+=" , "
        vstr+=str(self.__department)
        vstr+=" , "
        vstr+=str(self.__semester)
        return vstr


class Teacher(Person):
    def __init__(self,name,contact_number,course,office_number):
        super().__init__(name,contact_number)
        self.__course=course
        self.__office_number=office_number

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self,d):
        self.__course=d
    
    @property
    def office_Number (self):
        return self.__office_number
    @office_Number.setter
    def office_number(self,d):
        self.__office_number=d
    
    def __str__ (self):
        vstr=""
        vstr+=super().__str__()
        vstr+=" , "
        vstr+=str(self.__course)
        vstr+=" , "
        vstr+=str(self.__office_number)
        return vstr
    

class TeacherAssisstant(Student,Teacher):
    def __init__(self,name,contact_number,department,semester,course,office_number):
        self.__name=name
        self.__contact_number=contact_number
        self.__department=department
        self.__semester=semester
        self.__course=course
        self.__office_number=office_number

    def __str__(self):
        vstr=""
        vstr+=str(self.__name)
        vstr+=","
        vstr+=str(self.__contact_number)
        vstr+=" , "
        vstr+=str(self.__department)
        vstr+=" , "
        vstr+=str(self.__semester)
        vstr+=" , "
        vstr+=str(self.__course)
        vstr+=" , "
        vstr+=str(self.__office_number)
        return vstr


def main():
    person=Person("ALI", "03001112222")
    print("Person:", person)

    student=Student("REHAN", "03236782340", "Data Science", 3)
    print("Student:", student)

    teacher=Teacher("ARIF BUTT", "03147892048", "Digital Logic Design", "C-22")
    print("Teacher:", teacher)

    ta=TeacherAssisstant("HARIS AHMAD", "02017170173", "Data Science", 2, "Discrete Structures", "B-07")
    print("Teacher Assistant:", ta)

if __name__ == "__main__":
    main()