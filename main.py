# Program to generate random number 1-100 on every keypress by the user

import random
import sys
import functions

# Generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Main program
def main():
    print("\nPress any key (except 'q') to generate a random number between 1 and 100.")
    print("Pressing 'q' exits the program.\n")

    while True:
        pressed_key = functions.get_pressed_key().lower()
        if pressed_key == 'q':
            print()
            sys.exit()

        print(generate_random_number())

if __name__ == "__main__":
    main()
