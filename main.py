"""
Basic program to troll your friends
Fire the content of a certain file while scroll lock button
Press Esc to exit the program 
"""

import pyperclip
import keyboard
import random
import time

SCROLL_LOCK = 70
ESC = 1

running = True
randomize = False

def exit_program() -> None:
    global running
    running = False


if __name__ == "__main__":
    keyboard.add_hotkey(ESC, exit_program)
    print("Welcome to the ultimate useless program")

    cooldown = float(input("cd => "))
    randomize = bool(input("Randomize from a charset? (1=yes, 0=no): "))
    
    content = ""
    if not randomize:
        filename = input(
                "name of the file which content you wan't to spam (make sure it is in the folder): "
            )
        with open(filename, "r") as file:
            content = file.read()
        pyperclip.copy(content)
    else:
        length = int(input("your content length?"))
        
    while running:
        while keyboard.is_pressed(SCROLL_LOCK):
            if randomize:
                charset_content = []
                with open("charset.txt", "r", encoding="utf-8") as charset:
                    charset_content = list(charset.read())
                content = ''.join(random.choice(charset_content) for _ in range(length))
                pyperclip.copy(content)
            keyboard.press_and_release("ctrl+v")
            keyboard.press_and_release("enter")
            time.sleep(cooldown)
            