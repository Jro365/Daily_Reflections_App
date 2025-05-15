"""
App: Daily Reflections App
Description:A command-line journal app that lets users add, view, and read reflections. Entries are timestamped and saved to a text file using basic file I/O and Python functions.
Author:Jaime Rodriguez
Date:April 2025
"""
"""
Change Log:
- 2025-04-15: Initial version created based on pseudocode
- No known bugs or logic errors encountered at this time
"""

import os
from datetime import datetime

def main():
    print("Welcome to the Daily Reflections Journal App.")
    journal_file_name = 'daily_reflections.txt'
    configure_file(journal_file_name)

    while True:
        journal_menu()
        user_choice = get_journal_choice()

        if user_choice == '1':
            add_entry(journal_file_name)
        elif user_choice == '2':
            most_recent(journal_file_name, 5)
        elif user_choice == '3':
            read_all(journal_file_name)
        elif user_choice == '4':
            print("Thank you for reflecting today. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

    print("Your reflections are safely stored.")

def journal_menu():
    print("\n1) Add New Reflection")
    print("2) View Most Recent Reflections")
    print("3) Read All Reflections")
    print("4) Exit")

def configure_file(journal_file_name):
    if not os.path.exists(journal_file_name):
        with open(journal_file_name, 'w') as file:
            file.write(f"Reflection Journal Created: {datetime.now()}\n")
        print("New journal file created.")
    else:
        with open(journal_file_name, 'a') as file:
            file.write(f"Journal Accessed: {datetime.now()}\n")
        print("Journal ready.")

def get_journal_choice():
    return input("\nEnter your choice (1-4): ")

def add_entry(journal_file_name):
    new_entry = input("\nWrite your reflection for today:\n")
    with open(journal_file_name, 'a') as file:
        file.write(f"{new_entry} — {datetime.now()}\n")
    print("Reflection added.")

def most_recent(journal_file_name, n_lines):
    if os.path.exists(journal_file_name):
        with open(journal_file_name, 'r') as file:
            lines = file.readlines()
        recent_lines = lines[-n_lines:]

        print("\nMost Recent Reflections:")
        for line in recent_lines:
            print(line.strip())

        with open(journal_file_name, 'a') as file:
            file.write(f"Recent Reflections Viewed: {datetime.now()}\n")

def read_all(journal_file_name):
    if os.path.exists(journal_file_name):
        with open(journal_file_name, 'r') as file:
            lines = file.readlines()

        print("\nAll Reflections:")
        for line in lines:
            print(line.strip())

        with open(journal_file_name, 'a') as file:
            file.write(f"All Reflections Read: {datetime.now()}\n")

if __name__ == "__main__":
    main()
