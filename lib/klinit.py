#!/usr/bin/env python3

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from byt.main import Equipment, Area, User

from control.ctrlA import (function1a, function1b, function1c)
from control.ctrlB import (function2a, function2b)
from control.ctrlC import (function3a, function3b)

class Cli:
    def __init__(self):
        self.users = [user for user in session.query(User)]
        self.areas = [area for area in session.query(Area)]
        self.equipments = [equipment for equipment in session.query(Equipment)]
        self.session = session
        self.main_menu()

    def main_menu(self):
        print(" ")
        user_name = input(f"{Fore.GREEN}{Style.BRIGHT}Enter Your Name: ")
        while user_name:
            print(" ")
            print(f"{Fore.LIGHTWHITE_EX}~~ Welcome to {Fore.GREEN}{Style.BRIGHT}KLiN'iT,{Fore.BLUE}{Style.BRIGHT} {user_name}! {Fore.LIGHTWHITE_EX}~~")
            print(" ")
            print("Please select from the following options:")
            print(" ")
            print("Press S to search the database.")
            print("Press P to print records.")
            print("Press C to create new data entries.")
            print(" ")
            print(f"{Fore.RED}{Style.BRIGHT}Press Q to quit.")
            print(" ")
            user_choice = input(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}What would you like to do next? ")
            if user_choice == "S" or user_choice == "s":
                Cli.function1(self, user_choice)
            elif user_choice == "P" or user_choice == "p":
                Cli.function2(self, user_choice)
            elif user_choice == "C" or user_choice == "c":
                Cli.function3(self, user_choice)
            elif user_choice == "Q":
                break
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid option entered. Please select from the list of options or press Q to quit.")
                
    def function1(self, user_choice):
        while user_choice:
            print(" ")
            print(f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT}SEARCH QUERIES:")
            print(" ")
            print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Select from the following options:")
            print(" ")
            print("a: Search for work locations by location or employee's last name.")
            print("b: Search for equipment assignments by employee's last name.")
            print("c: Search for individual employee by employee's last name.")
            print(" ")
            print(f"{Fore.RED}Press Q to exit to main menu.")
            print(" ")
            search_option = input(f"{Fore.YELLOW}Selection: ")
            if search_option == "a":
                function1a(session, search_option)
            elif search_option == "b":
                function1b(session, search_option)
            elif search_option == "c":
                function1c(session, search_option)
            elif search_option == "Q":
                break
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid option, please select a, b, c, or press Q to quit.")
    
    def function2(self, user_choice):
        while user_choice:
            print(" ")
            print(f"{Fore.BLUE}{Style.BRIGHT}PRINT QUERIES:")
            print(" ")
            print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Select from the following options:")
            print(" ")
            print("a: Print a list of employees by position including a final count of employees.")
            print("b: Count the number of equipments in inventory.")
            print(" ")
            print(f"{Fore.RED}Press Q to exit to main menu.")
            print(" ")
            search_option = input(f"{Fore.YELLOW}Selection: ")
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
            print(f"{Fore.GREEN}{Style.BRIGHT}CREATE NEW DATA ENTRIES:")
            print(" ")
            print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Select from the following options:")
            print(" ")
            print("a: Add new employee to database.")
            print("b: Add new equipmnet to database.")
            print(" ")
            print(f"{Fore.RED}Press Q to exit to main menu.")
            print(" ")
            search_option = input(f"{Fore.YELLOW}Selection: ")
            if search_option == "a":
                function3a(session, search_option)
            elif search_option == "b":
                function3b(session, search_option)
            elif search_option == "Q":
                break
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid option, please select a, b, or press Q to quit.")
    
   
if __name__ == "__main__":
    engine = create_engine("sqlite:///byt/main.db")
    session = Session(engine, future=True)
    Cli()






