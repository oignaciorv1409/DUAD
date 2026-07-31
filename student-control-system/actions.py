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
                        "social_Studies_grade": social_studies_grade,
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
        
        while True:
                for student in students:
                        print("-" * 40)
                        print(f"full name: {student['full_name']}")
                        print(f"section: {student['section']}")
                        print(f"spanish grade: {student['spanish_grade']}")
                        print(f"english grade: {student['english_grade']}")
                        print(f"social studies grade: {student['social_studies_grade']}")
                        print(f"science grade: {student['science_grade']}")


def calculate_student_average(student_grade):
        sum_total = (
                student_grade["spanish_grade"]
                + student_grade["english_grade"]
                + student_grade["social_studies_grade"]
                + student_grade["science_grade"]
        )

        average = sum_total / 4

        return average