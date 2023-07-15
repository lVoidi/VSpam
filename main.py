"""
Basic program to troll your friends
Fire the content of a certain file while scroll lock button
Press Esc to exit the program 
"""

import keyboard
import pyperclip

SCROLL_LOCK = 70
ESC = 1


def start_spam(content: str) -> None:
    """
    This function will start spamming the input of the user
    """
    pass


running = True


def exit_program() -> None:
    global running
    running = False


if __name__ == "__main__":
    keyboard.add_hotkey(ESC, exit_program)
    print("Welcome to the ultimate useless program")
    filename = input(
        "name of the file which content you wan't to spam (make sure it is in the folder): "
    )
    with open(filename, "r") as file:
        content = file.read()
        pyperclip.copy(content)
        callback, args = start_spam, (content)
        keyboard.add_hotkey(SCROLL_LOCK, callback=callback, args=args)

    while running:
        pass
