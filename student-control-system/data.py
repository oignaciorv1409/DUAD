import csv

def export_students_to_csv(filepath,students):
        if not students:
                print("There are no students to export.")
                return

        with open(filepath, "w", encoding="utf-8", newline="") as file:

                headers = students[0].keys()

                writer = csv.DictWriter(file, fieldnames= headers)

                writer.writeheader()

                writer.writerows(students)

                print("Students exported succesfully.")



def import_students_from_csv(filepath):
        