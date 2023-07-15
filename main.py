"""
Basic program to troll your friends
Fire the content of a certain file while scroll lock button
Press Esc to exit the program 
"""

import keyboard
import pyperclip
import time

SCROLL_LOCK = 70
ESC = 1

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

    cooldown = float(input("cd => "))
    
    with open(filename, "r") as file:
        content = file.read()
        pyperclip.copy(content)

    while running:
        while keyboard.is_pressed(SCROLL_LOCK):
            keyboard.press_and_release("ctrl+v+enter")
            time.sleep(cooldown)
            
