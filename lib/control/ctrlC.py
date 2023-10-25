from byt.main import User, Equipment

def function3a(session, search_option):
    print(" ")
    print("Add new employee to database.")
    while search_option:
        print(" ")
        last_name = input("Enter employee last name: ")
        if last_name == "Q":
            break
        else:
            first_name = input("Enter employee first name: ")
            position = input("Enter employee position: ")
            if position == "Supervisor" or position == "Team lead" or position == "Hygiene-clerk":
                print(" ")
                print(f"Last Name: {last_name} | First Name: {first_name} | Position: {position}")
                print(" ")
                confirm = input("Confirm add above employee to database? n/Y: ")
                if confirm == "n":
                    print(" ")
                    print("Employee NOT added to database.")
                elif confirm == "Y":
                    add_user(session, User(first_name=first_name, last_name=last_name, potision=position))
                    print(" ")
                    print("New employee successfully added to database!")
                elif confirm == "Q":
                    break
                else:
                    print (" ")
                    print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")
            else:
                print(" ")
                print(f"You entered position: {position}, which is an invalid option.")
                print("Please enter Supervisor, Team lead or Hygiene-clerk for position.")

def add_user(session, user):
    session.add(user)
    session.commit()

def function3b(session, search_option):
    print(" ")
    print("Add new equipment to database.")
    while search_option:
        print(" ")
        type = input("Enter equipment type: ")
        if type == "Q":
            break
        else:
            print(" ")
            print(f"Type: {type}")
            print(" ")
            confirm = input("Confirm add above equipment to database? n/Y: ")
            if confirm == "n":
                print(" ")
                print("Equipment NOT added to database.")
            elif confirm == "Y":
                add_equipment(session, Equipment(type=type))
                print(" ")
                print("New equipment successfully added to database!")
            elif confirm == "Q":
                break
            else:
                print("Invalid entry. Please enter n/Y or press Q to exit to main menu.")

def add_equipment(session, equipment):
    session.add(equipment)
    session.commit()