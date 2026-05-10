import time
import os

def typewriter(text, delay=0.05):
    print(text, end='', flush=True)
    return ""

def read_file():
    with open("dreams.txt", "r") as dreamfile:
        content = dreamfile.read()
    return content

def rewrite_text(message):
    with open("dreams.txt", "w") as dreamfile:
        dreamfile.write(message)

def append_text(new_message):
    with open("dreams.txt", "a") as dreamfile:
        dreamfile.write(f"{new_message}\n")

def third_choice():
    while True:
        warning_choice = input(typewriter("Warning: You'll be overwriting the existing file. Proceed? Y/N: "))

        if warning_choice.lower() == "y":
            message = input("Enter your new inspiring message: ")
            rewrite_text(message)
            typewriter("\nDreams overwritten")
            break
        elif warning_choice.lower() == "n":
            typewriter("\nAction cancelled.")
            break
        else:
            typewriter("Invalid selecion. Please choose Y/N: ")
    
    os.system('cls' if os.name == 'nt' else 'clear')


def second_choice():
    new_message = input("Add a new inspiring message!: ")
    append_text(new_message)
    typewriter("\nYour inspiration has been added.")
    os.system('cls' if os.name == 'nt' else 'clear')


def first_choice():
    content = read_file()
    print("\n== Inpiring Messages ==")
    typewriter(f"{content}")

def main():
    while True:
        print("\n")
        print(">>> DREAMS FILE MANAGER <<<")
        print("1. Read inspiring messages.\n2. Add a new inspiring message\n3. Rewrite the entire file.\n4. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "4":
            break
        elif user_choice == "3":
            third_choice()
        elif user_choice == "2":
            second_choice()
        elif user_choice == "1":
            first_choice()

main()





