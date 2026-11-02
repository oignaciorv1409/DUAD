def show_menu():
        menu = {
                "1": "Add Students",
                "2": "Show Students",
                "3": "Show top 3 students",
                "4": "Show general average",
                "5": "Export data to CSV",
                "6": "Import data from CSV",
                "7": "Exit",
        }

        option = ""

        while True:
                title = "Student Control System"
                print("=" * 40)
                print(title.center(40))
                print("=" * 40)

                for key, value in menu.items():
                        print(f"{key}. {value}")

                option = input("Please choose an option from menu: ")

                if option in menu:
                        return option
                else:
                        print("Please enter a valid option from menu.")