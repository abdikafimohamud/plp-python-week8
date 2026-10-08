import random
# Tool 1: To-Do List
# Keeps a list of tasks that changes while the program runs.
# The user can add a task, show all tasks, remove a task, or go back.
def todo_list(tasks):
    print("\n--- To-Do List ---")
    while True:
        action = input("add / show / remove / back: ").strip().lower()

        if action == "add":
            task = input("Task to add: ").strip()
            if task == "":
                print("A task cannot be empty.")
            else:
                tasks.append(task)
                print(f"Added '{task}'. You now have {len(tasks)} task(s).")

        elif action == "show":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                number = 1
                for task in tasks:
                    print(f"{number}. {task}")
                    number += 1

        elif action == "remove":
            task = input("Task to remove: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Removed '{task}'.")
            else:
                print("That task is not on your list.")

        elif action == "back":
            print("Returning to the main menu...")
            break

        else:
            print("Please type add, show, remove or back.")


# Tool 2: Number Guessing Game
# The computer picks a number from 1 to 20 and the user has 5 tries.
# After each guess the program says whether it was too low or too high.
def guessing_game():
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 20)
    max_tries = 5
    tries = 0
    won = False

    print(f"I am thinking of a number between 1 and 20. You have {max_tries} tries.")

    while tries < max_tries and not won:
        raw = input(f"Guess #{tries + 1}: ").strip()

        # Make sure the input is a whole number
        try:
            guess = int(raw)
        except ValueError:
            print("Please type a whole number.")
            continue

        tries += 1

        if guess == secret:
            won = True
            print(f"Correct! You got it in {tries} tr{'y' if tries == 1 else 'ies'}. Well done!")
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    if not won:
        print(f"Out of tries! The number was {secret}.")


# Tool 3: Simple Calculator
# Asks for two numbers and an operation, then prints the answer.
# It handles invalid numbers and division by zero without crashing.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Those were not valid numbers. Please try again.")
        return

    operation = input("Operation (+, -, *, /): ").strip()

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b
    else:
        print(f"'{operation}' is not a valid operation.")
        return

    print(f"{a:g} {operation} {b:g} = {result:g}")


# Tool 4: Name Formatter
# Takes a full name and shows it in different formats, plus the initials
# and the number of letters in the name.
def name_formatter():
    print("\n--- Name Formatter ---")
    name = input("Enter your full name: ").strip()

    if name == "":
        print("You did not type a name.")
        return

    initials = ""
    for part in name.split():
        initials += part[0].upper() + "."

    letters = len(name.replace(" ", ""))

    print(f"Title Case: {name.title()}")
    print(f"UPPER CASE: {name.upper()}")
    print(f"Initials:   {initials}")
    print(f"Your name has {letters} letters.")


# Main program: shows the menu again and again until the user chooses Quit.
def main():
    tasks = []  # the to-do list lives here so it is kept between visits

    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n========================================")
        print("   PERSONAL MINI-TOOLKIT")
        print("========================================")
        print("1. To-Do List")
        print("2. Number Guessing Game")
        print("3. Simple Calculator")
        print("4. Name Formatter")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            todo_list(tasks)
        elif choice == "2":
            guessing_game()
        elif choice == "3":
            calculator()
        elif choice == "4":
            name_formatter()
        elif choice == "5":
            print("Thanks for using the toolkit. Goodbye!")
            break
        else:
            print(f"'{choice}' is not on the menu. Please choose a number from 1 to 5.")


main()