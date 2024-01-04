def input_entity(entity_name):
    return tuple(input(f"Enter {entity_name} ID, name, and date of birth (comma-separated): ").split(', '))

def input_marks(students, selected_course):
    return {student[0]: input(f"Enter marks for {student[1]} in {selected_course[1]}: ") for student in students}

def list_entities(entities, entity_name):
    print(f"\nList of {entity_name}s:")
    for entity in entities:
        print(f"{entity_name} ID: {entity[0]}, Name: {entity[1]}")

def show_student_marks(selected_course, students, marks):
    print(f"\nStudent Marks for {selected_course[1]}:")
    for student in students:
        mark = marks.get(student[0], "N/A")
        print(f"Student ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}, Marks: {mark}")

def main():
    num_students = int(input("Enter the number of students: "))
    students = [input_entity("Student") for _ in range(num_students)]

    num_courses = int(input("Enter the number of courses: "))
    courses = [input_entity("Course") for _ in range(num_courses)]

    selected_course_id = input("Enter the course ID for marks: ")
    selected_course = next((course for course in courses if course[0] == selected_course_id), None)

    if selected_course:
        marks = input_marks(students, selected_course)

        list_entities(courses, "Course")
        list_entities(students, "Student")
        show_student_marks(selected_course, students, marks)
    else:
        print("Invalid course ID. Please select a valid course.")

if __name__ == "__main__":
    main()
