import menu
import actions
import data

def main ():
        students = []

        while True: 
                option = menu.show_menu()

                if option == "1":
                        actions.add_students(students)

                elif option == "2":
                        actions.show_students(students)

                elif option == "3":
                        actions.show_top_3_students(students)

                elif option == "4":
                        actions.show_general_avg(students)

                elif option == "5":
                        data.export_students_to_csv(students)

                elif option == "6":
                        students = data.import_students_from_csv()

                elif option == "7":
                        print("Thanks for using student control system!")

                        break

main()
