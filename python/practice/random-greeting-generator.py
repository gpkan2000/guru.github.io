# Load the random package so we can use its functions
import random

# Create a variable that stores a list of greeting options
greetings = ["Hello", "Hi", "Hey", "Greetings", "Welcome", "Howdy"]

# Ask user for input and store their response in the 'name' variable
name = input("What's your name? \n")

# Use random.choice() to pick one greeting, combine with name, and display result
print(f"{random.choice(greetings)}, {name}! 🎉")
