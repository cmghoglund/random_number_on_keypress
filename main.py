# Program to generate random number 1-100 on every keypress by the user

# TODO Add capability to handle special keys (i.e., Ctrl, Alt, arrow keys, etc.)

import random
import platform

# Generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Check if the current platform is Windows
def is_windows():
    return platform.system() == 'Windows'

# Check if the current platform is Unix-based
def is_unix():
    return platform.system() in ['Darwin', 'Linux']

# Handle key presses on Windows
def handle_windows_key_press():
    import msvcrt

    while True:
        try:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                if key.lower() == 'q':
                    print()
                    break
                else:
                    print(generate_random_number())
        except KeyboardInterrupt:
            print()
            break

# Handle key presses on Unix-based systems
def handle_unix_key_press():
    import sys
    import tty
    import termios

    def getchar():
        file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_descriptor)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
        return ch

    while True:
        try:
            key = getchar()
            if key.lower() == 'q':
                print()
                break
            else:
                print(generate_random_number())
        except KeyboardInterrupt:
            print()
            break

# Main program
def main():
    print("\nPress any key (except 'q') to generate a random number between 1 and 100.")
    print("Pressing 'q' exits the program.\n")
    try:
        if is_windows():
            handle_windows_key_press()
        elif is_unix():
            handle_unix_key_press()
        else:
            print("Unsupported platform.")
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    main()
