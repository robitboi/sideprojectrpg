def get_choices(menu: str, legal_choices: tuple) -> str:
    user_choice = ""
    while user_choice not in legal_choices:
        print(menu)
        user_input = input("Your choice: ")
        if user_choice not in legal_choices:
            print("Not an option, select one of the available choices: ")
            print(legal_choices)
    return(user_choice)

if __name__ == "__main__":
    menu = "\nList of options:\n\n\t1 - Visit the Planet Express HQ\n"
    menu += "\t2 - Go to Fry's apartment\n\t3 - Visit the moon\n\n"
    selection = get_choices(menu, ("1", "2", "3"))