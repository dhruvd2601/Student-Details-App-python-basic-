students = []


class Student:

    school_name = "C.s.p.i.t."

    def __init__(self, name, student_id=51):
        #student = {"name": name, "student_id": student_id}
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HighschoolStudent(Student):
    school_name = "c.s.p.i.t. high collage"

    def get_school_name(self):
        return "This is high school student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + " -HS"


Man = HighschoolStudent("Man")
print(Man.get_name_capitalize())