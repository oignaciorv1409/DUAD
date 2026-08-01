def get_valid_grade(subject):
        while True:
                grade = input(f"Please enter {subject} grade between 0 and 100: ")
                try:
                        convert_to_int = int(grade)

                        if 0 <= convert_to_int <= 100:
                                return convert_to_int
                        else:
                                print("Grade must be between 0 and 100.")

                except ValueError:
                        print("Please enter a valid number. Do not enter letters.")


def create_student():
        full_name = input("Please enter full name: ")
        section = input("Please enter section name: ")

        spanish_grade = get_valid_grade("Spanish")
        english_grade = get_valid_grade("English")
        social_studies_grade = get_valid_grade("Social Studies")
        science_grade = get_valid_grade("Science")

        
        student_profile = {
                        "full_name": full_name,
                        "section": section,
                        "spanish_grade": spanish_grade,
                        "english_grade": english_grade,
                        "social_studies_grade": social_studies_grade,
                        "science_grade": science_grade,
                }

        return student_profile


def add_students (students):
        while True:

                str_quantity = input("How many students are your adding? ")
                try: 
                        students_quantity = int(str_quantity)
                        if students_quantity > 0:
                                break
                        else:
                                print("Please enter a number greater than 0.")
                except ValueError:
                        print("Please enter a valid number.")

        for i in range(students_quantity):
                new_student = create_student()
                students.append(new_student)

        print("You have added the students correctly.")


def show_students(students):
        if not students:
                print("There are no students registered.")
                return
        
        for student in students:
                print("-" * 40)
                print(f"Full name: {student['full_name']}")
                print(f"Section: {student['section']}")
                print(f"Spanish grade: {student['spanish_grade']}")
                print(f"Snglish grade: {student['english_grade']}")
                print(f"Social studies grade: {student['social_studies_grade']}")
                print(f"Science grade: {student['science_grade']}")


def calculate_student_average(student_grade):
        sum_total = (
                student_grade["spanish_grade"]
                + student_grade["english_grade"]
                + student_grade["social_studies_grade"]
                + student_grade["science_grade"]
        )

        average = sum_total / 4

        return average


def show_general_average(students):
        if not students:
                print("There are no students registered.")
                return

        general_avg = 0

        for student_grades in students:
                student_average = calculate_student_average(student_grades)

                general_avg = student_average + general_avg

        general_avg = general_avg / len(students)

        print(F"The general average for all students is {general_avg}.")


def show_top_3_students (students):
        if not students:
                print("There are not students registered.")
                return

        sorted_students = sorted(
                students,
                key=calculate_student_average,
                reverse=True
        )

        top_3_students = sorted_students[:3]

        for student_avg_grade in top_3_students:
                top3_student_average = calculate_student_average(student_avg_grade)

                print("-" * 40)
                print(f"Full name: {student_avg_grade['full_name']}")
                print(f"Section: {student_avg_grade['section']}")
                print(f"Average: {top3_student_average}")        