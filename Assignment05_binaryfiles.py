import struct
student_format = '11s30s2sif11s'
grade_format = '20s11sf'
student_file = 'students.dat'
grade_file = 'grades.dat'


def pack_student_data(roll, name, department, semester, marks, phone):
    return struct.pack(student_format, roll.encode(), name.encode(), department.encode(), semester, marks, phone.encode())

def unpack_student_data(data):
    return struct.unpack(student_format, data)

def pack_grade_data(course, roll, marks):
    return struct.pack(grade_format, course.encode(), roll.encode(), marks)

def unpack_grade_data(data):
    return struct.unpack(grade_format, data)


def duplicate_roll(roll):
    with open(student_file, 'rb') as file:
        while True:
            data = file.read(struct.calcsize(student_format))
            if not data:
                break
            existing_roll = unpack_student_data(data)[0].decode().strip('\x00')
            if existing_roll == roll:
                return True
    return False


def add_student():
    with open(student_file,"ab") as file:
        roll=input("Enter roll number: ")
        if not duplicate_roll(roll):
            name=input("Enter name: ")
            department=input("Enter department code: ")
            semester=int(input("Enter semester: "))
            marks=float(input("Enter last semester percent marks: "))
            phone=input("Enter phone number: ")
            student_data=pack_student_data(roll,name,department,semester,marks,phone)
            file.write(student_data)
            print("Student added successfully!")
        else:
            print("OOPs! Duplicate roll number. Student cannot be added.")


def view_student_by_roll_no(roll):
    with open(student_file,"rb") as file:
        while True:
            data=file.read(struct.calcsize(student_format))
            if not data:
                break
            current_roll, _, _, _, _, _ =unpack_student_data(data)
            if current_roll.decode().strip('\x00')==roll:
                print("Roll number: {}, Name: {}, Department: {},Semester: {}, Marks: {}, Phone Number:{}".format(*unpack_student_data(data)))
            else:
                print("Student not found.")


def edit_student_by_roll_no(roll):
    with open(student_file, "r+b") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(student_format))
            if not data:
                break
            current_roll, _, _, _, _, _ = unpack_student_data(data)
            if current_roll.decode().strip('\x00') == roll:
                found = True
                name = input("Enter new name: ")
                department = input("Enter new department code: ")
                semester = int(input("Enter new semester: "))
                marks = float(input("Enter last semester percent marks: "))
                phone = input("Enter phone number: ")
                updated_student_data = pack_student_data(roll, name, department, semester, marks, phone)
                file.seek(-struct.calcsize(student_format), 1)
                file.write(updated_student_data)
                print("Student edited successfully!")
                break
        
        if not found:
            print("Student not found.")


def delete_student_by_roll_no(roll):
    with open(student_file, "r+b") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(student_format))
            if not data:
                break
            current_roll, _, _, _, _, _ = unpack_student_data(data)
            if current_roll.decode().strip('\x00') == roll:
                found = True
                file.seek(-struct.calcsize(student_format), 1)
                file.write(b'\x00' * struct.calcsize(student_format))
                print("Student deleted successfully!")
                break
        if not found:
            print("Student not found.")


def list_students_by_semester(semester):
    with open(student_file, "rb") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(student_format))
            if not data:
                break
            _, _, _, current_semester, _, _ = unpack_student_data(data)
            if current_semester == semester:
                found = True
                print("Roll number: {}, Name: {}, Department: {}, Semester: {}, Marks: {}, Phone Number:{}".format(*unpack_student_data(data)))

        if not found:
            print("No students found for the specified semester.")


def list_students_by_name(name):
    with open(student_file, "rb") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(student_format))
            if not data:
                break
            _, current_name, _, _, _, _ = unpack_student_data(data)
            if current_name.decode().strip('\x00') == name:
                found = True
                print("Roll number: {}, Name: {}, Department: {}, Semester: {}, Marks: {}, Phone Number:{}".format(*unpack_student_data(data)))
        if not found:
            print("No students found with the specified name.")


def print_students_list():
    with open(student_file, "rb") as file:
        while True:
            data = file.read(struct.calcsize(student_format))
            if not data:
                break
            print("Roll number: {}, Name: {}, Department: {}, Semester: {}, Marks: {}, Phone Number:{}".format(*unpack_student_data(data)))


def add_grade_of_a_student_for_a_course():
    course = input("Enter course name: ")
    roll = input("Enter student's roll number: ")
    if not duplicate_roll(roll):
        print("Student not found. Cannot add grade.")
        return
    with open(grade_file, "wb+") as file:
        while True:
            data = file.read(struct.calcsize(grade_format))
            if not data:
                break
            current_course, current_roll, _ = unpack_grade_data(data)
            if current_course.decode().strip('\x00') == course and current_roll.decode().strip('\x00') == roll:
                print("Grade already exists for the specified course and student.")
                return
    marks = float(input("Enter marks for the course: "))
    with open(grade_file, "ab") as file:
        grade_data = pack_grade_data(course, roll, marks)
        file.write(grade_data)
    print("Grade added successfully!")


def import_grades_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if len(data) == 3:
                course, roll, marks = data
                marks = float(marks)
                if duplicate_roll(roll):
                    with open(grade_file, 'ab') as file:
                        grade_data = pack_grade_data(course, roll, marks)
                        file.write(grade_data)
                    print(f"Grade for {course} added successfully for student with roll number {roll}.")
                else:
                    print(f"Student with roll number {roll} not found. Grade not added.")


def view_grades_of_a_student(roll):
    with open(grade_file, "rb") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(grade_format))
            if not data:
                break
            _, current_roll, current_marks = unpack_grade_data(data)
            if current_roll.decode().strip('\x00') == roll:
                found = True
                print("Course: {}, Roll number: {}, Marks: {}".format(*unpack_grade_data(data)))
        if not found:
            print("No grades found for the specified student.")


def edit_grades_of_a_student_for_a_course():
    pass


def delete_grades_of_a_student_for_a_course():
    pass


def list_student_wise_grade_of_courses(roll):
    with open(grade_file, "rb") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(grade_format))
            if not data:
                break
            current_course, current_roll, current_marks = unpack_grade_data(data)
            if current_roll.decode().strip('\x00') == roll:
                found = True
                print("Course: {}, Marks: {}".format(current_course.decode().strip('\x00'), current_marks))
        if not found:
            print("No grades found for the specified student.")


def list_course_wise_grade_of_students(course):
    with open(grade_file, "rb") as file:
        found = False
        while True:
            data = file.read(struct.calcsize(grade_format))
            if not data:
                break
            current_course, current_roll, current_marks = unpack_grade_data(data)
            if current_course.decode().strip('\x00') == course:
                found = True
                print("Roll number: {}, Marks: {}".format(current_roll.decode().strip('\x00'), current_marks))
        if not found:
            print("No grades found for the specified course.")


def award_sheet():
    with open(grade_file, "rb") as file:
        courses = set()
        while True:
            data=file.read(struct.calcsize(grade_format))
            if not data:
                break
            current_course, _, _=unpack_grade_data(data)
            courses.add(current_course.decode().strip('\x00'))
        for course in courses:
            print(f"\nCourse: {course}")
            file.seek(0)
            found = False
            while True:
                data = file.read(struct.calcsize(grade_format))
                if not data:
                    break
                current_course, current_roll, current_marks=unpack_grade_data(data)
                if current_course.decode().strip('\x00')==course:
                    found = True
                    print("Roll number: {}".format(current_roll.decode().strip('\x00')))
            if not found:
                print("No students enrolled in the specified course.")


def summary_sheet():
    with open(grade_file, "rb") as file:
        courses = set()
        while True:
            data = file.read(struct.calcsize(grade_format))
            if not data:
                break
            current_course, _, _ = unpack_grade_data(data)
            courses.add(current_course.decode().strip('\x00'))
        for course in courses:
            print(f"\nCourse: {course}")
            file.seek(0)
            found = False
            while True:
                data = file.read(struct.calcsize(grade_format))
                if not data:
                    break
                current_course, current_roll, current_marks = unpack_grade_data(data)
                if current_course.decode().strip('\x00') == course:
                    found = True
                    print("Roll number: {}, Marks: {}".format(current_roll.decode().strip('\x00'), current_marks))
            if not found:
                print("No students enrolled in the specified course.")


def transcripts_for_a_range_of_student(start_roll,end_roll):
    with open(student_file, "rb") as file1, open(grade_file, "rb") as file2:
        found_students = False
        while True:
            student_data=file1.read(struct.calcsize(student_format))
            if not student_data:
                break
            roll, name, _, _, _, _ = unpack_student_data(student_data)
            current_roll = roll.decode().strip('\x00')
            if start_roll <= current_roll <= end_roll:
                found_students = True
                print("\nTranscript for Student\nRoll Number: {}\tName: {}".format(current_roll, name.decode().strip('\x00')))
                print("\n-------------------------------------------------------")
                file2.seek(0)
                while True:
                    grade_data = file2.read(struct.calcsize(grade_format))
                    if not grade_data:
                        break
                    current_course, current_grade_roll, current_marks = unpack_grade_data(grade_data)
                    if current_grade_roll.decode().strip('\x00') == current_roll:
                        print(f"Course: {current_course}, Marks: {current_marks}")
        if not found_students:
            print(f"No students found in the specified range ({start_roll} to {end_roll}).")


def main():
    while True:
        print("1. Quit the management system.\n2. Add a student.\n3. View student by roll no.\n4. Edit student by roll no.\n5. Delete student by roll no.\n6. List students by semester.\n7. List students by name.\n8. Print students list.\n9. Add grade of a student for a course.\n10. Import grades for a course for many students from a TABed text file.\n11. View grades of a student.\n12. Edit grades of a student for a course.\n13. Delete grades of a student for a course.\n14. List student wise (1 student) grade of courses.\n15. List course wise grade (1 course) of students.\n16. Award sheet (courses one by one, with students enrolled in it).\n17. Summary sheet (courses info, one by one, with one line for each student in it).\n18. Transcripts for a range of student.")
        choice=int(input("Enter your choice:"))

        if choice==1:
            print("Quitting the management system. GoodBye!")
            break

        elif choice==2:
            add_student()

        elif choice==3:
            roll=input("Enter roll number: ")
            view_student_by_roll_no(roll)

        elif choice==4:
            roll=input("Enter roll number: ")
            edit_student_by_roll_no(roll)

        elif choice==5:
            roll=input("Enter roll number: ")
            delete_student_by_roll_no(roll)

        elif choice==6:
            semester=int(input("Enter semester: "))
            list_students_by_semester(semester)

        elif choice==7:
            name=input("Enter name: ")
            list_students_by_name(name)

        elif choice==8:
            print_students_list()

        elif choice==9:
            add_grade_of_a_student_for_a_course()

        elif choice==10:
            file_path = input("Enter the path of the TABed text file: ")
            import_grades_from_file(file_path)

        elif choice==11:
            roll = input("Enter student's roll number: ")
            view_grades_of_a_student(roll)

        elif choice==12:
            pass

        elif choice==13:
            pass

        elif choice==14:
            roll = input("Enter student's roll number: ")
            list_student_wise_grade_of_courses(roll)

        elif choice==15:
            course = input("Enter course name: ")
            list_course_wise_grade_of_students(course)

        elif choice==16:
            award_sheet()

        elif choice==17:
            summary_sheet()

        elif choice==18:
            start_roll = input("Enter the starting roll number: ")
            end_roll = input("Enter the ending roll number: ")
            transcripts_for_a_range_of_student(start_roll,end_roll)

        else:
            break

if __name__=="__main__":
    main()