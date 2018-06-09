students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name,last_name="modi", student_id=51, ):
    student = {"name":name, "student_id": student_id, "last_name": last_name}
    students.append(student)


def save_file(student):
    try:
        f= open("students.txt", "a") #a means we want to append some text to this file
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()

ask = input("do you want to enter new student?   ")

if ask in ["yes"] :
    student_name = input("Enter the student name: ")
    student_last_name = input("Enter student last name: ")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_last_name, student_id,)
    save_file(student_name)
    print_student_titlecase()
else:
    print_student_titlecase()
