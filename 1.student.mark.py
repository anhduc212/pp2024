class Student:
    def __init__(self, student_id, name, dob):
        self.student_id, self.name, self.dob = student_id, name, dob

class Course:
    def __init__(self, course_id, name):
        self.course_id, self.name = course_id, name

def input_entity(entity_name):
    return tuple(input(f"Enter {entity_name} ID, name, and date of birth (comma-separated): ").split(', '))

def input_marks(students, selected_course):
    return {student.student_id: input(f"Enter marks for {student.name} in {selected_course.name}: ") for student in students}

def list_entities(entities, entity_name):
    print(f"\nList of {entity_name}s:")
    for entity in entities:
        print(f"{entity_name} ID: {entity.course_id}, Name: {entity.name}")

def show_student_marks(selected_course, students, marks):
    print(f"\nStudent Marks for {selected_course.name}:")
    for student in students:
        mark = marks.get(student.student_id, "N/A")
        print(f"Student ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}, Marks: {mark}")

def main():
    students = [Student(*input_entity("Student")) for _ in range(int(input("Enter the number of students: ")))]
    courses = [Course(*input_entity("Course")) for _ in range(int(input("Enter the number of courses: ")))]

    selected_course_id = input("Enter the course ID for marks: ")
    selected_course = next((course for course in courses if course.course_id == selected_course_id), None)

    if selected_course:
        marks = input_marks(students, selected_course)

        list_entities(courses, "Course")
        list_entities(students, "Student")
        show_student_marks(selected_course, students, marks)
    else:
        print("Invalid course ID. Please select a valid course.")

if __name__ == "__main__":
    main()
