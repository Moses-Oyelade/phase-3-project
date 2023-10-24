from pyt.main import User, Equipment
import pandas

def function2a(session, search_option):
    print(" ")
    print("Print a list of employee by position including a final count of employee.")
    print(" ")
    print("Press Q to exit to main menu.")
    while search_option:
        print(" ")
        position = input("Enter position: ")
        if position == "Supervisor" or position == "Team lead" or position == "Hygiene-clerk":
            print_users_by_position(session, position=position)
            print(" ")
            count_users_by_position(session, position=position)
        elif position == "Q":
            break
        else:
            print(f"You entered: {position}, which is invalid. Please enter Supervisor, Team lead or Hygiene-clerk to print employees by position.")

def print_users_by_position(session, position):
    users = (session.query(User).filter(User.grade_level == position)).all()
    user_data = ([(user.first_name, user.last_name) for user in users])
    df = (pandas.DataFrame(user_data, columns=["First Name", "Last Name"]))
    print(df.to_string(index=False))

def count_users_by_position(session, position):
    position_count = (session.query(User).filter(User.position == position).count())
    print(f"There are {position_count} employee(s) in grade {position}.")

def function2b(session, search_option):
    print(" ")
    print("Count the number of equipments in inventory.")
    print(" ")
    print("Press Q to exit to main menu.")
    while search_option:
        print(" ")
        equipment = input("Enter equipment type: ")
        equipment_types = ["Scrubbing-machine", "Vaccum-sucker", "Pressure-washer", "Telescopic-pole", "Mops", "Squee-gee", "soft-brush", "Glass-cleaner", "Drain-rods", "Truck", "Grass-Trimer", "Scaffolding", "K-rod"]
        if equipment in equipment_types:
            print(" ")
            count_equipments(session, equipment=equipment)
        elif equipment == "Q":
            break
        else:
            print(f"You entered: {equipment}, which is invalid.")
            print("Please select from the following list of eequipments:")
            print([record for record in equipment_types])

def count_equipments(session, equipment):
    equipment_count = session.query(Equipment).filter(Equipment.type.like(equipment)).count()
    if  equipment_count> 0:
        print(f"There are {equipment_count} {equipment}(s) in the database.")
    if equipment_count == 0:
        print("None of this equipment type are currently in the database.")