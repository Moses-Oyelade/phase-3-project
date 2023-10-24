from pyt.main import Area, User, Equipment
import inquirer
import pandas
import re

def function1a(session, search_option):
    print(" ")
    print("Search for work locations by duty or employee last name.")
    while search_option:
        print(" ")
        combo_search = input("Enter duty or employee last name: ")
        print(" ")
        int_pattern = r'\d'
        regex = re.compile(int_pattern)
        match = regex.search(combo_search)
        if combo_search == "Q":
            break
        elif match:
            print_combo_by_area_duty(session, area_duty=combo_search)
        elif not match:
            print_combo_by_area_duty(session, area_duty=combo_search)

def print_combo_by_area_duty(session, area_duty):
    combo = session.query(Area).filter(Area.duty == area_duty).first()
    if combo:
        print(f'Area: {combo.duty} Location: {combo.duty}')
    else:
        print("There is no matching Area duty in the database.")

def print_combo_by_last_name(session, last_name):
    users = (session.query(User).filter(User.last_name == last_name).all())
    if users:
        if len(users) == 1:
            user_combos = (session.query(Area).join(User).where(User.id == Area.user_id).filter(User.last_name == last_name).all())
            if user_combos:
                print("The selected employee works at the following area(s) assigned: ")
                print(" ")
                for combo in user_combos:
                    print(f'Area: {combo.duty} Location: {combo.loccation}')
            else:
                print(f"Last Name: {last_name} | This employee does not have any area assigned.")
        else:
            options = []
            print(f"There are multiple employees with the last name: {last_name}")
            print(" ")
            for user in users:
                option = (f'{last_name}, {user.first_name}', user.id)
                options.append(option)
            questions = [
                inquirer.List('employees',
                              message="Please select the correct employee: ",
                              choices=options,
                              ),
                              ]
            answers = inquirer.prompt(questions)
            selection = answers['employee']

            user_combos = (session.query(Area).join(User).where(User.id == Area.user_id).filter(Area.user_id == selection).all())
            if user_combos:
                print("The selected employee has the following area(s) assigned: ")
                print(" ")
                for combo in user_combos:
                    print(f'Duty: {combo.duty} Location: {combo.locationn}')
            else:
                print(f"Last Name: {last_name} | This employee does not have any Area assigned.")
    else:
        print(f"Last Name: {last_name} | There is no employee matching this name in the database.")

def function1b(session, search_option):
    print(" ")
    print("Search for equipment assignments by employee last name.")
    while search_option:
        print(" ")
        record = input("Enter employee last name: ")
        print(" ")
        if record == "Q":
            break
        else:
            print_employee_equipment(session, last_name=record)

def print_employee_equipment(session, last_name):
    users = session.query(User).filter(User.last_name == last_name).all()
    if users:
        if len(users) == 1:
            for users in users:
                equipment = (session.query(Equipment).filter(Equipment.user_id == user.id).all())
                if equipment:
                    print(f"This employer has the following equipment(s) assigned: ")
                    print(" ")
                    equipment_data = ([equipment.type for equipment in equipment])
                    df = (pandas.DataFrame(equipment_data, columns=["Equipment"]))
                    print(df.to_string(index=False))
                else:
                    print(f"Last Name: {last_name} | There are no equipments assigned to an employee matching the last name entered.")
        else:
            options = []
            print(f"There are multiple employees with the last name: {last_name}")
            print(" ")
            for user in users:
                option = (f'{last_name}, {user.first_name}', user.id)
                options.append(option)
            questions = [
                inquirer.List('employee',
                                message="Please select the correct employee: ",
                                choices=options,
                                ),
                                ]
            answers = inquirer.prompt(questions)
            selection = answers['employees']
            user_equipments = session.query(equipment).filter(Equipment.user_id == selection).all()
            if user_equipments:
                print(f"This user has the following equipment(s) assigned: ")
                print(" ")
                equipments = [equipment.type for equipment in user_equipments]
                df = (pandas.DataFrame(equipments, columns=["Equipment"]))
                print(df.to_string(index=False))
            else:
                print(f"Last Name: {last_name} | There are no equipments assigned to an employee matching the last name entered.")
    else:
        print(f"Last Name: {last_name} | There is no user matching this name in the database.")

def function1c(session, search_option):
    print(" ")
    print("Search for individual employees by employee last name.")
    while search_option:
        print(" ")
        record = input("Enter employee last name: ")
        print(" ")
        if record == "Q":
            break
        else:
            find_by_last_name(session, last_name=record)

def find_by_last_name(session, last_name):
    users = (session.query(User).filter(User.last_name == last_name).all())
    if users:
        user_data = ([(user.last_name, user.first_name, user.grade_level) for user in users])
        df = (pandas.DataFrame(user_data, columns=["Last Name", "First Name", "Gender"]))
        print(df.to_string(index=False))
    else:
        print(f"Last Name: {last_name} | There is no employee matching this name in the database.")