"""
gamefunctions.py

Contains functions for a simple text-based adventure game. Functions
allow purchasing items, generating random monsters, printing a 
welcome message, and displaying a shop menu.
"""

import random

def purchase_item(itemPrice: int, startingMoney: int, quantityToPurchase: int = 1):
    """
    Calculate the quantity of items that can be purchased and the 
    remaining money.

    Parameters:
        itemPrice (int): Price of a single item.
        startingMoney (int): Money available to spend.
        quantityToPurchase (int): Desired quantity to purchase (default 1).

    Returns:
        tuple: Quantity actually purchased (int), money remaining (int).
    """
    max_affordable = startingMoney // itemPrice
    quantity_bought = min(quantityToPurchase, max_affordable)
    money_remaining = startingMoney - (quantity_bought * itemPrice)
    return quantity_bought, money_remaining

def new_random_monster():
    """
    Generate a random monster with attributes: name, description,
    health, power, and money.

    Returns:
        dict: A dictionary containing monster attributes:
            - name (str)
            - description (str)
            - health (int)
            - power (int)
            - money (int)
    """
    monsters = [
        {
            "name": "Goblin",
            "descriptions": [
                "This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.",
                "A goblin sneaks behind a rock, eyeing you with a mischievous grin.",
                "A goblin appears from the shadows, muttering strange words under its breath."
            ],
            "health_range": (5, 10),
            "power_range": (1, 5),
            "money_range": (10, 50)
        },
        {
            "name": "Vulture",
            "descriptions": [
                "You discover a vulture eating the remains of two orcs that appear to have killed each other. They were carrying a chest that contains a small treasure horde. You will need to scare off the vulture before you can take the treasure.",
                "A vulture circles above a small pile of bones, watching your every move.",
                "A vulture is perched on a tree branch, its eyes gleaming as it spots you."
            ],
            "health_range": (1, 3),
            "power_range": (1, 2),
            "money_range": (100, 2000)
        },
        {
            "name": "Troll",
            "descriptions": [
                "A massive troll lumbers toward you, its club swinging menacingly.",
                "A troll blocks your path, growling and stomping the ground.",
                "You hear heavy footsteps; a troll emerges from the trees, hungry for trouble."
            ],
            "health_range": (20, 40),
            "power_range": (10, 20),
            "money_range": (50, 150)
        }
    ]

    monster_template = random.choice(monsters)
    monster = {
        "name": monster_template["name"],
        "description": random.choice(monster_template["descriptions"]),
        "health": random.randint(*monster_template["health_range"]),
        "power": random.randint(*monster_template["power_range"]),
        "money": random.randint(*monster_template["money_range"])
    }

    return monster

def print_welcome(name: str, width: int):
    """
    Print a welcome message centered within a specified width.

    Parameters:
        name (str): Name of the player.
        width (int): Total width for centering the message.

    Returns:
        None
    """
    message = f"Hello, {name}!"
    print(message.center(width))

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    Display a formatted shop menu with two items and their prices.

    Parameters:
        item1Name (str): Name of the first item.
        item1Price (float): Price of the first item.
        item2Name (str): Name of the second item.
        item2Price (float): Price of the second item.

    Returns:
        None
    """
    border = "/----------------------\\"
    print(border)
    print(f"| {item1Name:<12} ${item1Price:>6.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>6.2f} |")
    print("\\----------------------/")

# -------------------------
# Test calls for all functions
# -------------------------

# Test purchase_item()
print("Testing purchase_item()")
p1 = purchase_item(123, 1000, 3)
p2 = purchase_item(123, 201, 3)
p3 = purchase_item(341, 2112)
print(p1)
print(p2)
print(p3)

# Test new_random_monster()
print("\nTesting new_random_monster()")
m1 = new_random_monster()
m2 = new_random_monster()
m3 = new_random_monster()
print(m1)
print(m2)
print(m3)

# Test print_welcome()
print("\nTesting print_welcome()")
print_welcome("Jeff", 20)
print_welcome("Audrey", 30)
print_welcome("Chasity", 25)

# Test print_shop_menu()
print("\nTesting print_shop_menu()")
print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
print_shop_menu("Sword", 149.99, "Shield", 99.5)
