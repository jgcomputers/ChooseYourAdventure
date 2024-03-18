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
    print("Welcome to the Adventure Game!")
