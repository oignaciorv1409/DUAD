def get_valid_grade():
        while True:
                grade = input("Please enter grade between 0 and 100: ")
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

        spanish_grade = get_valid_grade()
        english_grade = get_valid_grade()
        social_studies_grade = get_valid_grade()
        science_grade = get_valid_grade()

        
        student_profile = {
                        "full_name": full_name,
                        "section": section,
                        "spanish_grade": spanish_grade,
                        "english_grade": english_grade,
                        "social_Studies_grade": social_studies_grade,
                        "science_grade": science_grade,
                }

        return student_profile