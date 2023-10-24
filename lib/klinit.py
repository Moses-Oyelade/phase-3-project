#!/usr/bin/env python3

import os, shutil

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pyt.main import Equipment, Area, User

from subfunctions.function1 import (function1a, function1b, function1c)
from subfunctions.function2 import (function2a, function2b)
from subfunctions.function3 import (function3a, function3b)

class Cli:
    def __init__(self):
        self.users = [user for user in session.query(User)]
        self.areas = [area for area in session.query(Area)]
        self.equipments = [equipment for equipment in session.query(Equipment)]
        self.session = session
        self.main_menu()

    def main_menu(self):
        print(" ")
        user_name = input("Enter Your Name: ")
        while user_name:
            print(" ")
            print(f"~~ Welcome to KLiN'iT, {user_name}! ~~")
            print(" ")
            print("Please select from the following options:")
            print(" ")
            print("Press S to search the database.")
            print("Press P to print records.")
            print("Press C to create new data entries.")
            print(" ")
            print("Press Q to quit.")
            print(" ")
            user_choice = input("What would you like to do next? ")
            if user_choice == "S" or user_choice == "s":
                Cli.function1(self, user_choice)
            elif user_choice == "P" or user_choice == "p":
                Cli.function2(self, user_choice)
            elif user_choice == "C" or user_choice == "c":
                Cli.function3(self, user_choice)
            elif user_choice == "Q":
                break
            else:
                print("Invalid option entered. Please select from the list of options or press Q to quit.")
                
    def function1(self, user_choice):
        while user_choice:
            print(" ")
            print("SEARCH QUERIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Search for work locations by location or employee's last name.")
            print("b: Search for equipment assignments by employee's last name.")
            print("c: Search for individual employee by employee's last name.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                function1a(session, search_option)
            elif search_option == "b":
                function1b(session, search_option)
            elif search_option == "c":
                function1c(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, c, or press Q to quit.")
    
    def function2(self, user_choice):
        while user_choice:
            print(" ")
            print("PRINT QUERIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Print a list of employees by position including a final count of employees.")
            print("b: Count the number of equipments in inventory.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                function2a(session, search_option)
            elif search_option == "b":
                function2b(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")

    def function3(self, user_choice):
        while user_choice:
            print(" ")
            print("CREATE NEW DATA ENTRIES:")
            print(" ")
            print("Select from the following options:")
            print(" ")
            print("a: Add new employee to database.")
            print("b: Add new equipmnet to database.")
            print(" ")
            print("Press Q to exit to main menu.")
            print(" ")
            search_option = input("Selection: ")
            if search_option == "a":
                function3a(session, search_option)
            elif search_option == "b":
                function3b(session, search_option)
            elif search_option == "Q":
                break
            else:
                print("Invalid option, please select a, b, or press Q to quit.")
    
   
if __name__ == "__main__":
    engine = create_engine("sqlite:///pyt/klinint_users.db")
    session = Session(engine, future=True)
    Cli()






