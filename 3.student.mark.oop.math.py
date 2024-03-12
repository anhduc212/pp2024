import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course, marks):
        self.marks[course.course_id] = marks

    def calculate_gpa(self):
        total_credits = 0
        weighted_sum = 0

        for course_id, marks in self.marks.items():
            course = next((c for c in courses if c.course_id == course_id), None)
            if course:
                total_credits += course.credits
                weighted_sum += course.credits * math.floor(float(marks))

        if total_credits == 0:
            return 0

        gpa = weighted_sum / total_credits
        return round(gpa, 1)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_entity(self, entity_name):
        data = input(f"Enter {entity_name} ID, name, and credits (comma-separated): ").split(', ')
        if entity_name == "Student":
            entity = Student(*data)
            self.students.append(entity)
        elif entity_name == "Course":
            entity = Course(*data)
            self.courses.append(entity)
        return entity

    def input_marks(self, selected_course):
        return {student.student_id: math.floor(float(input(f"Enter marks for {student.name} in {selected_course.name}: ")))
                for student in self.students}

    def list_entities(self, entities, entity_name):
        print(f"\nList of {entity_name}s:")
        for entity in entities:
            print(entity)

    def show_student_marks(self, selected_course):
        print(f"\nStudent Marks for {selected_course.name}:")
        for student in self.students:
            mark = student.marks.get(selected_course.course_id, "N/A")
            print(f"{student}, Marks: {mark}")

    def calculate_average_gpa(self, student):
        gpa = student.calculate_gpa()
        print(f"\nAverage GPA for {student.name}: {gpa}")

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)

    def curses_ui(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()

        stdscr.addstr(0, 0, "School Management System (Curses UI)", curses.A_BOLD)

        height, width = stdscr.getmaxyx()
        input_prompt = "Press 'q' to quit, 's' to sort students by GPA: "
        stdscr.addstr(height - 1, 0, input_prompt, curses.A_BOLD)

        while True:
            key = stdscr.getch()

            if key == ord('q'):
                break
            elif key == ord('s'):
                self.sort_students_by_gpa()
                stdscr.clear()
                stdscr.addstr(0, 0, "School Management System (Curses UI)", curses.A_BOLD)
                self.list_entities(self.students, "Student")

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
            for student in self.students:
                marks = self.input_marks(selected_course)
                student.add_marks(selected_course, marks)

            self.list_entities(self.courses, "Course")
            self.list_entities(self.students, "Student")
            self.show_student_marks(selected_course)

            self.calculate_average_gpa(self.students[0])  # Calculate average GPA for the first student

            curses.wrapper(self.curses_ui)  # Run curses UI
        else:
            print("Invalid course ID. Please select a valid course.")


if __name__ == "__main__":
    school = School()
    school.main()
