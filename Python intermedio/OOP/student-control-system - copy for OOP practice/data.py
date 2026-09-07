import csv
from class_student import Student

def export_students_to_csv(filepath,students):
        if not students:
                print("There are no students to export.")
                return

        students_as_dicts = []

        for student in students:
                student_dict = {
                "full_name": student.full_name,
                "section": student.section,
                "spanish_grade": student.spanish_grade,
                "english_grade": student.english_grade,
                "social_studies_grade": student.social_studies_grade,
                "science_grade": student.science_grade,
                }

                students_as_dicts.append(student_dict)

        with open(filepath, "w", encoding="utf-8", newline="") as file:

                headers = students_as_dicts[0].keys()

                writer = csv.DictWriter(file, fieldnames= headers)

                writer.writeheader()

                writer.writerows(students_as_dicts)

                print("Students exported succesfully.")



def import_students_from_csv(filepath):
        imported_students = []

        try:
                with open(filepath, "r", encoding="utf-8") as file: 

                        reader = csv.DictReader(file)

                        for row in reader:
                                row["spanish_grade"] = int(row["spanish_grade"])
                                row["english_grade"] = int(row["english_grade"])
                                row["social_studies_grade"] = int(row["social_studies_grade"])
                                row["science_grade"] = int(row["science_grade"])

                                student_obj = Student(
                                        row["full_name"],
                                        row["section"],
                                        row["spanish_grade"],
                                        row["english_grade"],
                                        row["social_studies_grade"],
                                        row["science_grade"],
                                )

                                imported_students.append(student_obj)

                print("Students imported successfully.")

                return imported_students

        except FileNotFoundError:
                print("There is no exported file yet.")

                return imported_students