import random 
import pyperclip 
import keyboard 
import time


ESC = 1
SCROLL_LOCK = 70

if __name__ == "__main__":
    while not keyboard.is_pressed(ESC): 
        link = "https://nhentai.net/g/"
        code = random.randint(10000, 80000)
        link += str(code)
        pyperclip.copy(link)
        if keyboard.is_pressed(SCROLL_LOCK):
            keyboard.press_and_release("ctrl+v")
            keyboard.press_and_release("enter")
        time.sleep(0.2)
