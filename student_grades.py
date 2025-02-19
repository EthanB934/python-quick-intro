# Initialize an Empty Dictionary

student_grades = {}

# Write a function that adds a student and their grade to the dictionary


# Adds a new key-value pair to student_grades dictionary
def add_student_and_grade(student, grade):
    student_grades[student] = grade
    print(f"{student} has been added to the dictionary. \nGrade: {grade}")


# Removes a student key-value pair by deleting key
def remove_student(student):
    if student in student_grades:
        del student_grades[student]
        print(f"{student} has been removed from the dictionary")
    else:
        print(f"{student} was not found in registry")


# Lists all key value pairs in dictionary
def display_students():
    print("Current Students and Their Grades:")
    for student, grade in student_grades.items():
        print(f"Student {student}, Grade: {grade}")


# Allows update of grade value to corresponding student
def update_grade(student, grade):
    if student in student_grades:
        student_grades[student] = grade
        print(f"{student}'s grade has been updated!")
    else:
        print("Student not found in registry")


def find_student_grade(student):
    if student in student_grades:
        print(student_grades[student])
    else:
        print(f"{student} not found in registry")


# finds average grade among all students
def find_average_grade():
    average_grade = 0
    for student, grade in student_grades.items():
        average_grade += grade
    print(f"{average_grade}")


add_student_and_grade("Ethan", 86)
add_student_and_grade("Adam", 95)
add_student_and_grade("Hannah", 98)

display_students()

# update_grade("Bobby", 93)
find_average_grade()

remove_student("Ethan")
# remove_student("Bobby")

# display_students()

# find_student_grade("Hannah")

find_average_grade()
