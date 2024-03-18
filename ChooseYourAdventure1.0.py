# Programmer: Jordan Gibbs
# Date: 3.15.2024
# Program: Choose Your Adventure

# import libraries here:
import time

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

if __name__ == "__main__":
    main()