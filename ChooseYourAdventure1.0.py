# Programmer: Jordan Gibbs
# Date: 3.15.2024
# Program: Choose Your Adventure

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
            "3": "encounter a training opportunity"
        }
    }

    # Welcome message
    print("Welcome to the Guy Game!")
    print("\nA Day of", player["name"] + ":")
    print(player["name"], "is just a guy who has",
          str(player["strength"]) + " strength. His goal is to get as strong as possible.")
    print("It was just a regular day, and", player["name"], "was sitting at home looking for something to do.")
    print("He came up with three options:")

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
            elif choice == "3":
                encounter_training_opportunity(player)

            # Random event
            random_event(player)

        else:
            print("Invalid choice. Please try again.")

def go_get_ice_cream(player):
    player["strength"] -= 1
    print("\n", player["name"], "goes to get ice cream at Dairy Queen and loses 1 strength. His strength is now", player["strength"], ".")

def go_to_weight_room(player):
    player["strength"] += 1
    print("\n", player["name"], "went to the weight room! He worked out his arms and legs and increased his strength to", player["strength"], ".")

def encounter_training_opportunity(player):
    print("\n", player["name"], "encounters a training opportunity!")
    decision = input("Do you want to (train/forgo training): ").lower()
    if decision == "train":
        player["strength"] += random.randint(1, 3)
        print("\n", player["name"], "takes advantage of the training opportunity and gains strength. His strength is now", player["strength"], ".")
    elif decision == "forgo training":
        player["strength"] -= random.randint(1, 3)
        print("\n", player["name"], "decides to forgo training and loses some strength. His strength is now", player["strength"], ".")
    else:
        print("\nInvalid input. No training effect.")

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
    elif event_chance == 5:
        print("\nOh no! While exploring, a wild animal appears and scares", player["name"], ". He loses some strength due to the fright.")
        player["strength"] -= random.randint(1, 3)
        print("His strength decreases to", player["strength"], ".")

if __name__ == "__main__":
    main()