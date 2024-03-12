class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name, dob):
        self.course_id = course_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}"


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_entity(self, entity_name):
        data = input(f"Enter {entity_name} ID, name, and date of birth (comma-separated): ").split(', ')
        if entity_name == "Student":
            entity = Student(*data)
            self.students.append(entity)
        elif entity_name == "Course":
            entity = Course(*data)
            self.courses.append(entity)
        return entity

    def input_marks(self, selected_course):
        return {student.student_id: input(f"Enter marks for {student.name} in {selected_course.name}: ")
                for student in self.students}

    def list_entities(self, entities, entity_name):
        print(f"\nList of {entity_name}s:")
        for entity in entities:
            print(entity)

    def show_student_marks(self, selected_course):
        print(f"\nStudent Marks for {selected_course.name}:")
        for student in self.students:
            mark = self.marks.get(student.student_id, "N/A")
            print(f"{student}, Marks: {mark}")

    def main(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            self.input_entity("Student")

        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            self.input_entity("Course")

        selected_course_id = input("Enter the course ID for marks: ")
        selected_course = next((course for course in self.courses if course.course_id == selected_course_id), None)

        if selected_course:
            self.marks = self.input_marks(selected_course)

            self.list_entities(self.courses, "Course")
            self.list_entities(self.students, "Student")
            self.show_student_marks(selected_course)
        else:
            print("Invalid course ID. Please select a valid course.")


if __name__ == "__main__":
    school = School()
    school.main()
