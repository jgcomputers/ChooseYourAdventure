# Programmer: Jordan Gibbs
# Date: 3.15.2024
# Program: Choose Your Adventure

# import libraries here:
import time
import random

def main():
    # Initialize player attributes
    player = {
        "name": "Guy",
        "strength": 6,
        "max_strength": 10,
        "actions": {
            "1": "go get ice cream",
            "2": "go to the weight room",
        }
    }

    # Welcome message
    print("Welcome to the Guy Game!")
    print("\nA Day of", player["name"] + ":")
    print(player["name"], "is just a guy who has",
          str(player["strength"]) + " strength. His goal is to get as strong as possible.")
    print("It was just a regular day, and", player["name"], "was sitting at home looking for something to do.")
    print("He came up with two options, go get ice cream or go to the weight room.")

    # Game loop
    while player["strength"] > 0 and player["strength"] < player["max_strength"]:
        print("\nOptions:")
        for key, value in player["actions"].items():
            print(key + ". " + value)

        # Get user choice
        choice = input("Enter your choice: ")

        # Process user choice
        if choice in player["actions"]:
            if choice == "1":
                go_get_ice_cream(player)
            elif choice == "2":
                go_to_weight_room(player)

            # Random event
            random_event(player)

        else:
            print("Invalid choice. Please try again.")

def go_get_ice_cream(player):
    player["strength"] -= 1
    print("\n" + player["name"], "goes to get ice cream at Dairy Queen and loses 1 strength. His strength is now", player["strength"], ".")

    # Random event chance
    if random.randint(1, 10) <= 3:
        print("\nWhile enjoying the ice cream, a bird poops on", player["name"], "'s head!")
        player["strength"] -= 1
        print(player["name"], "loses 1 more strength due to the unfortunate event. His strength is now", player["strength"], ".")

def random_event(player):
    # Simulate random events
    event_chance = random.randint(1, 10)
    if event_chance <= 2:
        print("\nA stray dog approaches", player["name"], "and follows him home. The dog becomes his loyal companion and boosts his morale!")
        player["strength"] += 1
        print("His strength increases to", player["strength"], ".")
    elif event_chance >= 9:
        print("\nWhile walking, a tree branch falls narrowly missing", player["name"], ". The adrenaline rush boosts his strength!")
        player["strength"] += 2
        print("His strength increases to", player["strength"], ".")


def go_to_weight_room(player):
    player["strength"] += 1
    print("\n", player["name"],
          "went to the weight room! He worked out his arms and legs and increased his strength to", player["strength"],
          "!")

    # Random event chance
    if random.randint(1, 10) <= 2:
        print("\nAt the weight room, a fellow gym-goer challenged", player["name"], "to a push-up contest!")
        if random.randint(0, 1) == 1:
            print(player["name"], "won the contest and gained 2 strength!")
            player["strength"] += 2
        else:
            print(player["name"], "lost the contest and felt demotivated, losing 1 strength.")
            player["strength"] -= 1
        print("His strength is now", player["strength"], "!")


if __name__ == "__main__":
    main()