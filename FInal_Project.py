import os
# This is a simple Code Compiler Program using python.
# It shows information and runs an example based on user choices.

def main():
    while True:  # Loop forever until the user chooses to exit
        # Clear the screen for a clean look (Windows only; use 'clear' on Mac/Linux)
        os.system('cls')
        
        # Welcome message and menu
        print("Welcome to My Code Compiler")
        print("Greetings User! What would you like to do?")
        print("-------------------------------------------------------")
        print("\nChoose an option: ")
        print("1 - FUNCTIONS")
        print("2 - ESCAPE SEQUENCES")
        print("3 - LOOPS")
        print("4 - CONDITIONAL STATEMENTS")
        print("5 - LISTS")
        print("6 - EXIT PROGRAM")

        
  # Get the user's choice
        choice = input("Enter your choice (1, 2, 3, 4): ")
        
        # Check what the user chose and call the right function
        if choice == "1":
            input(print("What would you like to choose?: "))
            print("1 - Print Function")
            print("2 - Input Function")
            print("3 - Def Function")
            print("4 - Eval Function")
        elif choice == "1":
                print("The print function allows the user to output information from the program to the user or developer.\n Hello World")
                continue
        elif choice == "2":
                print("The input function allows the user to input a data in the console and the program reads it")
                input(print("What is your name?: "))
                continue
        elif choice == "3":
                print("It is the essential mechanism for creating a named, reusable block of code.")
                continue
        elif choice == "4":
                print("The eval function  Its primary purpose is to allow dynamic execution of code from strings, such as in calculators, configuration parsers, or interactive shells.")
                something = eval(input("Input number"))
                print("The data type of something is", type(something))
                continue

        
        
    
                
                

        
          
    else:
            print("Oops! That's not a valid choice. Please try 1, 2, 3, 4.")
            input("Press any key to try again...")  # Wait before showing menu again