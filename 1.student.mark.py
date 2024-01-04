class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

def input_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    return Student(student_id, name, dob)

def input_course():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return Course(course_id, name)

def input_marks(students, selected_course):
    marks = {}
    for student in students:
        mark = input(f"Enter marks for {student.name} in {selected_course.name}: ")
        marks[student.student_id] = mark
    return marks

def main():
    # Input number of students
    num_students = int(input("Enter the number of students: "))

    # Input student information
    students = []
    for _ in range(num_students):
        student = input_student()
        students.append(student)

    # Input number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Input course information
    courses = []
    for _ in range(num_courses):
        course = input_course()
        courses.append(course)

    # Select a course
    selected_course_id = input("Enter the course ID you want to input marks for: ")
    selected_course = next((course for course in courses if course.course_id == selected_course_id), None)

    if selected_course:
        # Input marks for students in the selected course
        marks = input_marks(students, selected_course)

        # Print the entered information
        print("\nEntered Information:")
        for student in students:
            print(f"\nStudent ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"DoB: {student.dob}")
            print(f"{selected_course.name} Marks: {marks[student.student_id]}")
    else:
        print("Invalid course ID. Please select a valid course.")

if __name__ == "__main__":
    main()
