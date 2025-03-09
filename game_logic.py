from classes import *
# Function to create player character based on user input
def create_character():
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin\n")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. View Stats")
        print("9. Exit")
        choice = input("\nChoose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            player.display_specials_list()
            special = input("\nWhat special move? ")
            player.special_ability(special, wizard)
        elif choice == '3':
            player.display_stats()
            continue
        elif choice == '9':
            break
        else:
            print("\nInvalid choice, try again.\n")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            if not wizard.stunned:
                wizard.attack(player)
            else:
                print(f"\n{wizard.name} broke free!\n")
                wizard.stunned = False


        if player.health <= 0:
            print(f"\n{player.name} has been defeated!\n")
            break

    if wizard.health <= 0:
        print(f"\n{wizard.name} has been defeated by {player.name}!\n\n")

    print("\nDone..\nExiting...")