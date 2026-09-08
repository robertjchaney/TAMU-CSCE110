import curses
import time
import random
import threading
from playsound import playsound


def play_dice_sound():
    playsound("C:\\Users\\ososb\\Downloads\\pythonProject\\Final Project\\mp3 Files\\rpg-dice-rolling-95182.mp3")
    pass
def roll_dice(stdscr):
    stdscr.nodelay(True)  # Don't wait for user input
    stdscr.clear()

    die_faces = { # Die faces dictionary
        1: """|‾‾‾‾‾|
|  •  |
|_____|""",
        2: """|‾‾‾•‾|
|     |
|_•___|""",
        3: """|‾‾‾•‾|
|  •  |
|_•___|""",
        4: """|‾•‾•‾|
|     |
|_•_•_|""",
        5: """|‾•‾•‾|
|  •  |
|_•_•_|""",
        6: """|‾•‾•‾|
| • • |
|_•_•_|""",
    }
    
    height, width = stdscr.getmaxyx()

    if width < 50 or height < 10: # Checks if the terminal is too small or too big
        stdscr.addstr(0, 0, "Terminal too small. Resize and try again.")
        stdscr.refresh()
        stdscr.getch()
        return

    for _ in range(10):  # Roll the dice 10 times
        dice_value1 = random.randint(1, 6)
        dice_value2 = random.randint(1, 6)
        dice_value3 = random.randint(1, 6)
        
        message = f"You rolled a {dice_value1}, {dice_value2}, and a {dice_value3}"
        
        stdscr.clear()
        stdscr.addstr(1, 10, "Rolling...\n")

        threading.Thread(target=play_dice_sound, daemon=True).start()

        for i, dice_value in enumerate([dice_value1, dice_value2, dice_value3]):
            for j, line in enumerate(die_faces[dice_value].splitlines()):
                stdscr.addstr(3 + j, 10 + i * 10, line)

        stdscr.refresh()
        time.sleep(0.15)
    
    stdscr.nodelay(False)  # Wait for user input again
    stdscr.addstr(8, 10, message)
#     rollAgain = input("Roll Again?")
    stdscr.getch()

curses.wrapper(roll_dice)

