"""
game.py

Adventure Game with:
- Shop and purchasing items
- Inventory management
- Equipping weapons
- Monster encounters with durability and consumables
"""

import gamefunctions
import random

# -------------------------------
# GLOBAL VARIABLES
# -------------------------------
inventory = []

player = {
    "name": "",
    "hp": 30,
    "gold": 50,
    "equipped_weapon": None
}

# Example shop items
shop_items = [
    {"name": "sword", "type": "weapon", "damage": 10, "maxDurability": 10, "currentDurability": 10, "price": 150},
    {"name": "holy amulet", "type": "consumable", "effect": "autoDefeatMonster", "price": 200},
    {"name": "buckler", "type": "shield", "maxDurability": 6, "currentDurability": 6, "price": 100},
]

# -------------------------------
# SHOP & INVENTORY FUNCTIONS
# -------------------------------
def show_shop():
    print("\n🛒 Welcome to the Shop! Here’s what we have:")
    for i, item in enumerate(shop_items, start=1):
        print(f"{i}. {item['name'].title()} ({item['type']}) - ${item['price']}")
    print("0. Exit Shop")

def buy_item():
    show_shop()
    choice = input("Choose an item number to buy: ")

    if choice == "0":
        return

    try:
        index = int(choice) - 1
        item = shop_items[index]
        if player['gold'] >= item['price']:
            player['gold'] -= item['price']
            inventory.append(item.copy())
            print(f"✅ You purchased a {item['name']}! Gold remaining: {player['gold']}")
        else:
            print("❌ Not enough gold!")
    except (ValueError, IndexError):
        print("❌ Invalid choice.")

def show_inventory():
    if not inventory:
        print("\n🎒 Your inventory is empty.")
        return
    print("\n🎒 Your Inventory:")
    for i, item in enumerate(inventory, start=1):
        if item['type'] == "weapon":
            print(f"{i}. {item['name'].title()} ({item['type']}) - Durability: {item['currentDurability']}/{item['maxDurability']}")
        else:
            print(f"{i}. {item['name'].title()} ({item['type']})")

def equip_item():
    weapons = [item for item in inventory if item['type'] == "weapon"]
    if not weapons:
        print("\n⚔️ You have no weapons to equip.")
        return

    print("\n⚔️ Choose a weapon to equip:")
    for i, weapon in enumerate(weapons, start=1):
        print(f"{i}. {weapon['name'].title()} (Durability: {weapon['currentDurability']}/{weapon['maxDurability']})")
    print("0. Cancel")

    choice = input("Enter number: ")
    if choice == "0":
        return

    try:
        index = int(choice) - 1
        player["equipped_weapon"] = weapons[index]
        print(f"✅ You equipped the {weapons[index]['name']}!")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")

# -------------------------------
# MONSTER ENCOUNTER
# -------------------------------
def encounter_monster():
    print("\n👹 A monster appears!")
    monster = gamefunctions.new_random_monster()
    print(f"Name: {monster['name']}")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}")
    print(f"Power: {monster['power']}")
    print(f"Money: {monster['money']}")

    # Check for consumables that auto-defeat monsters
    for item in inventory:
        if item.get("effect") == "autoDefeatMonster":
            print(f"✨ Your {item['name']} glows and defeats the monster instantly!")
            inventory.remove(item)
            player['gold'] += monster['money']
            print(f"You gain ${monster['money']}! Total gold: {player['gold']}")
            return

    # Fight with equipped weapon if available
    weapon = player.get("equipped_weapon")
    if weapon:
        print(f"⚔️ You attack the monster with your {weapon['name']}!")
        weapon['currentDurability'] -= 1
        print(f"🪓 Weapon durability is now {weapon['currentDurability']}/{weapon['maxDurability']}")
        if weapon['currentDurability'] <= 0:
            print(f"💥 Your {weapon['name']} breaks!")
            inventory.remove(weapon)
            player['equipped_weapon'] = None
        print(f"🏆 You defeated the monster and earned ${monster['money']}!")
        player['gold'] += monster['money']
    else:
        print("😨 You have no weapon! You take damage!")
        player['hp'] -= monster['power']
        print(f"💔 Your HP is now {player['hp']}")

# -------------------------------
# MAIN GAME LOOP
# -------------------------------
def main():
    player['name'] = input("Enter your name: ")
    print(f"\nWelcome, {player['name']}! Let's begin your adventure!\n")

    while True:
        print(f"\nCurrent HP: {player['hp']}, Gold: {player['gold']}")
        print("What would you like to do?")
        print("1) Visit Shop")
        print("2) Show Inventory")
        print("3) Equip Weapon")
        print("4) Leave town (Fight Monster)")
        print("5) Sleep (Restore HP for 5 Gold)")
        print("6) Quit")

        choice = input("> ")

        if choice == "1":
            buy_item()
        elif choice == "2":
            show_inventory()
        elif choice == "3":
            equip_item()
        elif choice == "4":
            encounter_monster()
        elif choice == "5":
            player['hp'], player['gold'] = gamefunctions.sleep(player['hp'], player['gold'])
        elif choice == "6":
            print("Goodbye, adventurer!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
