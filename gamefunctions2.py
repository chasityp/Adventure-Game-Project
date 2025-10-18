# gamefunctions.py

import random

def purchase_item(price, money, quantityToPurchase=1):
    """
    Attempt to purchase a given quantity of items at a specific price.
    Returns: (number of items purchased, leftover money)
    """
    max_can_afford = money // price
    num_purchased = min(quantityToPurchase, max_can_afford)
    leftover_money = money - (num_purchased * price)
    return num_purchased, leftover_money


def new_random_monster(force_type=None):
    """
    Creates and returns a random monster as a dictionary with attributes.
    If force_type is given ("Goblin", "Vulture", or "Orc"), that monster is created.
    """
    monsters = [
        {
            "name": "Goblin",
            "description": "This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.",
            "health_range": (5, 15),
            "power_range": (2, 6),
            "money_range": (50, 200),
        },
        {
            "name": "Vulture",
            "description": "You discover a vulture eating the remains of two orcs that appear to have killed each other. "
                           "They were carrying a chest that contains a small treasure horde. You will need to scare off "
                           "the vulture before you can take the treasure.",
            "health_range": (1, 3),
            "power_range": (1, 2),
            "money_range": (500, 1500),
        },
        {
            "name": "Orc",
            "description": "A fierce orc blocks your path, wielding a large axe and grinning menacingly.",
            "health_range": (20, 40),
            "power_range": (5, 10),
            "money_range": (100, 400),
        }
    ]

    if force_type:
        monster_template = next(m for m in monsters if m["name"] == force_type)
    else:
        monster_template = random.choice(monsters)

    monster = {
        "name": monster_template["name"],
        "description": monster_template["description"],
        "health": random.randint(*monster_template["health_range"]),
        "power": random.randint(*monster_template["power_range"]),
        "money": random.randint(*monster_template["money_range"]),
    }
    return monster


# ==============================
# Demonstration Functions
# ==============================

def demo_purchase_item():
    print("=== purchase_item() Demonstrations ===")
    num_purchased, leftover = purchase_item(123, 1000, 3)
    print(num_purchased, leftover)   # Expect 3, 631

    num_purchased, leftover = purchase_item(123, 201, 3)
    print(num_purchased, leftover)   # Expect 1, 78

    num_purchased, leftover = purchase_item(341, 2112)  # default quantity = 1
    print(num_purchased, leftover)   # Expect 1, 1771

    num_purchased, leftover = purchase_item(3141, 2112)
    print(num_purchased, leftover)   # Expect 0, 2112


def demo_new_random_monster():
    print("\n=== new_random_monster() Demonstrations ===")
    # Force one Goblin, one Orc, and one Vulture for testing
    for forced_type in ["Goblin", "Orc", "Vulture"]:
        monster = new_random_monster(forced_type)
        print(f"Monster: {monster['name']}")
        print(f"  Description: {monster['description']}")
        print(f"  Health: {monster['health']}")
        print(f"  Power: {monster['power']}")
        print(f"  Money: {monster['money']}\n")


# ==============================
# Run Demos
# ==============================
if __name__ == "__main__":
    demo_purchase_item()
    demo_new_random_monster()

