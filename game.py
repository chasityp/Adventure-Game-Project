"""
game.py

Demonstrates using the functions from gamefunctions.py in a small
interactive scenario. Allows entering a player name, purchasing items,
and encountering random monsters.
"""

import gamefunctions

def main():
    # Welcome the player
    player_name = input("Enter your name: ")
    print("\n")
    gamefunctions.print_welcome(player_name, 40)  # Width included

    # Show the shop menu
    print("\nWelcome to the shop! Here are the items available:")
    gamefunctions.print_shop_menu("Sword", 150, "Shield", 100)

    starting_money = 500  # Must be an int

    # Purchase attempts
    quantity, starting_money = gamefunctions.purchase_item(150, starting_money, 1)
    print(f"\nYou bought {quantity} Sword(s). Money remaining: ${starting_money}")

    quantity, starting_money = gamefunctions.purchase_item(100, starting_money, 3)
    print(f"You bought {quantity} Shield(s). Money remaining: ${starting_money}")

    quantity, starting_money = gamefunctions.purchase_item(150, starting_money, 2)
    print(f"You bought {quantity} Sword(s). Money remaining: ${starting_money}")

    # Encounter three random monsters
    print("\nYou encounter some monsters!")
    for i in range(3):
        monster = gamefunctions.new_random_monster()
        print(f"\nMonster {i+1}:")
        print(f"Name: {monster['name']}")
        print(f"Description: {monster['description']}")
        print(f"Health: {monster['health']}")
        print(f"Power: {monster['power']}")
        print(f"Money: {monster['money']}")

if __name__ == "__main__":
    main()
