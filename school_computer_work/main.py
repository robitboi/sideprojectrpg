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

    print(f"\nYou selected {selection}")
    if selection == "1":
        planet_express_hq()
    elif selection == "2":
        apartment_fry()
    elif selection == "3":
        visit_moon()

def planet_express_hq():
    if selection == 1:
        print("Good news everyone! A visitor is here\n")
        print("Hello there! I'm Professor Farnswort\n Welcome to the Planet Express Headquarters. This is where all ")
        print(" the magic happens. Several deliveries are made out here everyday.")
        print("\n Why not stick around a bit and talk to the crew")

    if __name__ == "__main__":
        menu =  "\n People to talk to: \n\t1 - Leela\n\t2 - Fry"
        menu += "\n\t3 - Bender\n\t4 - Zoidberg\n\t5 - Back"
        selection = get_choices(menu, ("1", "2", "3", "4", "5"))
        print(f"You selected {selection}")
        return hq_people()

def hq_people():
    if selection == "1":
        print("I'm Leela. I'm the captain of the ship and I tell everyone what to do around here.")
        print(" Just between you and me, I think I should be working better. I'm surrounded")
        print(" by idiots here. Especially that beer guzzling robot Bender.")
        print(" Here take this, you might need it someday. Better to have it than not")
        #I plan on figuring out how I can have characters give you stuff and it adds it to
        #an inventory
    elif selection == "2":
        print("What's going on? I'm Fry. I'm the Professors great great great great, well, you get the idea.")
        print(" I got froze for a century and ended up in the future. Bender is my best friend.")
        print(" We do almost everything together. You seem pretty cool. Here just shut up and ")
        print("take my money!")
    elif selection == "3":
        print("Hey loser I'm Bender. I kinda hate everyone. I'm a bending unit but I don't really use ")
        print("it anymore. Wanna beer? You're old enough right? I'm kiddinng I don't care. And if ")
        print("anyone says anything they can bite my shiny metal ass!")
    elif selection == "4":
        print("Greetings. I'm Zoidberg. Doctor Zoidberg. Come to my office why not. ")
        print("I love all things smelly and gross. Take something for youself. You'll love it.")
    elif selection == "5":
        planet_express_hq()


def apartment_fry():
    if selection == 2:
       print("") 
    if __name__ == "__main__":
        menu =  "\n People to talk to: \n\t1 - Fry\n\t2 - Bender"
        menu += "\n\t3 - Seymour Butts\n\t4 - Back"
        selection = get_choices(menu, ("1", "2", "3", "4"))
        print(f"You selected {selection}")
        return (apartment_people)


def apartment_people():
    if selection == "1":
        print("Welcome to my apartment. This is where all the Fry magic happens. ")
        print("Over there is Bender's closet. It still weird to me that he sleeps in a closet. ")
        print("I guess robots will be robots. You should go talk to my dog, Seymour.")
    elif selection == "2":
        print("Bender here. ")
        print("This is my beautiful apartment. No not this big room, that tiny closet in the corner. ")
        print("I don't know why humans need so much room just to recharge. The most important part is ")
        print("of couese the fridge, where we keep all the 'adult' beverages.")
    elif selection == "3": 
        print("Arf arf arf arf. Ruff ruff.")
    elif selection == "4":
        apartment_fry()

def visit_moon():
    if selection == 3:
        print("")
    if __name__ == "__main__":
        menu =  "\n People to talk to: \n\t1 - Zap Brannigan\n\t2 - Don Bot"
        menu += "\n\t3 - Amy Wong\n\t4 - Back"
        selection = get_choices(menu, ("1", "2", "3", "4"))
        print(f"You selected {selection}")
        return moon_people()


def moon_people():
    if selection == "1":
        print("I'm Zap Brannigan! The universes most handsome and talented pilot. Don't stare too long, ")
        print("it may hurt your eyes how amazing I am. I'm here on the moon on a top secret mission. ")
        print("A mission to have fun at this theme park. Come Kif, adventure is to be had.")
    elif selection == "2":
        print("How's it goin'. I'm the Don Bot. I run the robot mafia on the Earth. I wouldn't try and ")
        print(" do anything sneaky around me, it won't go well. But if you need anyone 'taken care of' ")
        print(" you know who to call. ")
    elif selection == "3":
        print("I'm Amy Wong. I'm the Professors student and I'm trying to get my doctorate. I enjoy ")
        print("science a lot. My parents own a giant ranch and casino on the moon. I don't like them very much.")
    elif selection == "4":
        visit_moon()