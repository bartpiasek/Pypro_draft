student = {"name": "Rolf", "grades": (80, 90, 93, 78, 64)}

def average(sequence):
    return sum(sequence) / len(sequence)

# print(average(student["grades"]))

# OOP
class Student:
    """
    """
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 80, 64, 87)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.name)
print(student.grades)

print(Student.average_grade(student))
print(student.average_grade())




# print(student.average())