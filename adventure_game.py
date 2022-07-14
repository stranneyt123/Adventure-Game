import time
import random
character_choice = ()
possible_enemies = ("troll", "witch", "goblin", "yeti", "wizard")
enemy = random.choice(possible_enemies)
inventory = []


def print_pause(string):
    print(string)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, that choice is invalid. Try again!')


def victory():
    print_pause("You are victorious! You return to your town a hero")
    choice = valid_input("Would you like to play again? \n", ['yes', 'no'])
    if choice == 'yes':
        global enemy
        enemy = random.choice(possible_enemies)
        game_round()
    elif choice == 'no':
        print_pause("bye")
        quit()


def loss():
    print_pause("You are dead")
    choice = valid_input("Would you like to play again? \n", ['yes', 'no'])
    if choice == 'yes':
        global enemy
        enemy = random.choice(possible_enemies)
        game_round()
    elif choice == 'no':
        print_pause("bye")
        quit()


def first_choice():
    print_pause("You find yourself in a creepy derelict village")
    print_pause(f"Rumor has it a wicked {enemy} calls this place home")
    choice = valid_input("Press 1 to knock on the door of the creepy house: \n"
                         "Press 2 to enter the cave: \n", ['1', '2'])
    if choice == '1':
        print_pause("You knock on the door of the creepy house")
        house()
    elif choice == '2':
        print_pause("You enter the cave")
        cave()


def house():
    choice = valid_input(f"A {enemy} opens the door, what do you do? "
                         "Fight or flee? \n", ['fight', 'flee'])
    if choice == 'fight':
        if 'big ass sword of doom' in inventory:
            print_pause(f"You swing your big sword of doom at the "
                        f"{enemy}, it dies, well done!")
            victory()
        else:
            print_pause("Your current dagger is not enough "
                        "to defeat the enemy, "
                        "he kills you and you die")
            loss()

    elif choice == 'flee':
        print_pause("You flee back to the village")
        first_choice()


def cave():
    choice = valid_input("You enter the weird looking cave, in the corner of "
                         "your eye you spot something shiny\n"
                         "Do you investigate, or leave the cave? \n",
                         ['investigate', 'leave'])
    if choice == 'investigate':
        print_pause("Upon investigation you find the big"
                    "sword of doom, huzah!\n"
                    "You return to the village\n")
        inventory.append("big sword of doom")
        first_choice()
    elif choice == 'leave':
        print_pause("You leave the cave")
        first_choice()


def game_round():
    first_choice()


game_round()
