import platform

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
                return key
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
            return key
        except KeyboardInterrupt:
            print()
            break

def get_pressed_key():
    try:
        if is_windows():
            pressed_key = handle_windows_key_press()
            return pressed_key
        elif is_unix():
            pressed_key = handle_unix_key_press()
            return pressed_key
        else:
            print()
            sys.exit()
    except Exception:
        print()
        pass
