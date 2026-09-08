# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  Project
# Date: 11/13/24
import random
from turtle import *
import curses
import time
import threading
import os
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

def play_menu_music():
    playsound("Final Project\\mp3 Files\\Terraria Music - Jungle-[AudioTrimmer.com].mp3")
def stop_menu_music():
    playsound(None)
def zanzibar_thunder():
    playsound("Final Project\\mp3 Files\\natural-thunder-113219-[AudioTrimmer.com] (1).mp3")
def play_victory_sound():
    playsound("Final Project\\mp3 Files\\Happy Wheels victory green screen-[AudioTrimmer.com].mp3")
def play_dice_sound():
    playsound("Final Project\\mp3 Files\\rpg-dice-rolling-95182.mp3")


hideturtle()

def mainMenu():
    screen.bgpic("C:\\Users\\casho\\Downloads\\School\\(2024-2025) College Freshmen\\ENGR-102\\ZyBooks Chapter Labs\\Project\\Game Menu.gif")
    threading.Thread(target=play_menu_music, daemon=True).start()
    # pen = Turtle()
    # pen.hideturtle()
    # pen.penup()
    # pen.color('#00ff1a')

    # pen.goto(-500,-150)
    # pen.write('Play', align = 'center', font=("Oswald", 60, "bold"))

    # pen.goto(-165,-150)
    # pen.write('Rules', align = 'center', font=("Oswald", 60, "bold"))

    # pen.goto(170,-150)
    # pen.write('Credits', align = 'center', font=("Oswald", 60, "bold"))

    # pen.goto(510,-100)
    # pen.write('Game', align = 'center', font=("Oswald", 60, "bold"))
    # pen.goto(510,-200)
    # pen.write('History', align = 'center', font=("Oswald", 60, "bold"))

    # pen.color('#ef8b3e')
    # pen.goto(0,-480)
    # pen.write('Press 1-4 to continue', align = 'center', font=("Oswald", 50, "bold"))

def playMenu():
    bye()
    threading.Thread(target=stop_menu_music, daemon=True).start()

def rulesMenu():
    screen = Screen()
    screen.setup(1.0, 1.0)
    screen.bgpic("C:\\Users\\casho\\Downloads\\School\\(2024-2025) College Freshmen\\ENGR-102\\ZyBooks Chapter Labs\\Project\\Game Menu No Buttons.gif")

    pen = Turtle()
    pen.hideturtle()

    # Create a turtle for writing
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("#ef8b3e")

    # Define the credits as a list of strings
    credits = [
        'Welcome to Zanzibar\'s Dice Game',
        'The following rules are designed to create a fast paced version of the classic game',
        '-----------------------------------------------------------------------------------',
        'The game is played with 2 or more players',
        'Each of the players starts with 5 chips',
        'The goal of the game is to try and get rid of all of your chips',
        'To get rid of your chips, you just simply have to not be the loser',
        '',
        'The loser of each round is the person with the lowest score',
        'If you are the loser every other player will give you 1 - 4 chips depending on the winners score',
        'Your score is based off of the dice you roll',
        '',
        'REGULAR SCORING (+ 1 CHIP TO LOSER)',
        '1 = 100',
        '2 = 2',
        '3 = 3', 
        '4 = 4',
        '5 = 5',
        '6 = 60',
        'SPECIAL SCORES (+ 4 CHIPs TO LOSER)',
        '4 - 5 - 6 = 500',
        '1 - 2 - 3 = 490',
        'THREE OF A KIND (+ 3 CHIPs TO LOSER)',
        '1 - 1 - 1 = 499',
        '2 - 2 - 2 = 498',
        '3 - 3 - 3 = 497',
        '4 - 4 - 4 = 496',
        '5 - 5 - 5 = 495',
        '6 - 6 - 6 = 494',
        

    ]

    def scroll_text(text_lines, start_y, step_delay=0.01, font=("Oswald", 30)):
        count = 0

        pen.clear()  # Clear any existing text
        y = start_y  # Start at the specified y-coordinate
        
        for i in range(21 * (len(text_lines) + 1)):  # Allow blank frame after last line scrolls off
            pen.clear()  # Clear the screen for smooth animation
            y += 5  # Move all text upwards
            for idx, line in enumerate(text_lines):
                pen.goto(0, y - idx * 75)  # Position each line with a vertical offset
                pen.write(line, align="center", font=font)
            screen.update()  # Refresh the screen for the new positions
            time.sleep(step_delay)  # Pause for smooth animation
            count += 1
            # print(count)

        # Disable screen auto-refresh for smoother animation
    screen.tracer(0)

    # Scroll the credits
    scroll_text(credits, start_y=-400, step_delay=0.1)

    # Wait after the credits finish
    mainMenu()

def creditMenu():
    # Set up the screen
    screen = Screen()
    screen.setup(1.0, 1.0)
    screen.bgpic("C:\\Users\\casho\\Downloads\\School\\(2024-2025) College Freshmen\\ENGR-102\\ZyBooks Chapter Labs\\Project\\Game Menu No Buttons.gif")

    # Create a turtle for writing
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("#ef8b3e")

    # Define the credits as a list of strings
    credits = [
        "Brought To You By",
        "-----------------",
        "Cash Ostberg",
        "Robert Chaney",
        "Colby Hudson",
        "",
        "Special Thanks To",
        "-----------------",
        "Professor Ball",
        "Benicio Silva",
        "Jayden VanAusdall",
        "Evan Romeu",
        "The Internet",
        "",
        "Thank You For Playing"
    ]

    def scroll_text(text_lines, start_y, step_delay=0.01, font=("Oswald", 60)):
        count = 0

        pen.clear()  # Clear any existing text
        y = start_y  # Start at the specified y-coordinate
        
        for i in range(25 * (len(text_lines) + 1)):  # Allow blank frame after last line scrolls off
            pen.clear()  # Clear the screen for smooth animation
            y += 5  # Move all text upwards
            for idx, line in enumerate(text_lines):
                pen.goto(0, y - idx * 75)  # Position each line with a vertical offset
                pen.write(line, align="center", font=font)
            screen.update()  # Refresh the screen for the new positions
            time.sleep(step_delay)  # Pause for smooth animation
            count += 1
            # print(count)
            
        
        

    # Disable screen auto-refresh for smoother animation
    screen.tracer(0)

    # Scroll the credits
    scroll_text(credits, start_y=-200, step_delay=0.1)

    # Wait after the credits finish
    mainMenu()

def gameHistory():
    os.startfile("C:\\Users\\casho\\Downloads\\School\\(2024-2025) College Freshmen\\ENGR-102\\ZyBooks Chapter Labs\\Zanzibar's Dice Game.txt")

# Create the screen
screen = Screen()
screen.setup(1.0, 1.0)
mainMenu()

# Listen for key presses and bind them to functions
screen.listen()
screen.onkey(playMenu, "1")  # Press "1" to display Menu 1
screen.onkey(rulesMenu, "2")  # Press "2" to display Menu 2
screen.onkey(creditMenu, "3")  # Press "3" to display Menu 3
screen.onkey(gameHistory, "4")  # Press "4" to display Menu 4

# Keep the program running
screen.mainloop()

def diceRoll():                     # get 3 random numbers 0 - 6 to simulate 3 dice being rolled
    roll = [random.randint(1, 6) for i in range(3)]
    # roll = [1,1,1]
    roll.sort()
    return roll

def roll_dice_animation(stdscr):
    stdscr.clear()
    stdscr.nodelay(False)  # Wait for user input after displaying the final result

    die_faces = {  # Die faces dictionary
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

    if width < 50 or height < 10:  # Check if the terminal is too small
        stdscr.addstr(0, 0, "Terminal too small. Resize and try again.")
        stdscr.refresh()
        stdscr.getch()
        return None

    # Animation: Roll the dice 10 times
    for _ in range(10):
        # Update dice values during the animation loop
        dice_value1 = random.randint(1, 6)
        dice_value2 = random.randint(1, 6)
        dice_value3 = random.randint(1, 6)
        
        stdscr.clear()
        threading.Thread(target=play_dice_sound, daemon=True).start()
        stdscr.addstr(1, 10, "Rolling...\n")

        
        for i, dice_value in enumerate([dice_value1, dice_value2, dice_value3]):
            for j, line in enumerate(die_faces[dice_value].splitlines()):
                stdscr.addstr(3 + j, 10 + i * 10, line)

        stdscr.refresh()
        time.sleep(0.15)  # Add delay for animation effect

    # Final roll
    final_roll = diceRoll()
    dice_value1, dice_value2, dice_value3 = final_roll

    # Display final roll result
    stdscr.clear()
    stdscr.addstr(1, 10, "Final Roll:\n")
    for i, dice_value in enumerate(final_roll):
        for j, line in enumerate(die_faces[dice_value].splitlines()):
            stdscr.addstr(3 + j, 10 + i * 10, line)

    message = f"You rolled a {dice_value1}, {dice_value2}, and a {dice_value3}"

    stdscr.addstr(8, 10, message)
    stdscr.addstr(10, 10, "Press any key to return")
    stdscr.refresh()

    # Wait for any key press to quit
    stdscr.getch()

    return final_roll

def getPoints(playerRoll):          # convert the players dice roll to points
    diceToPoints = {
        1 : 100,
        2 : 2,
        3 : 3,
        4 : 4,
        5 : 5,
        6 : 60
    }
    points = 0

    if playerRoll == [4,5,6]:
        points += 500
        threading.Thread(target=zanzibar_thunder, daemon=True).start()
        print('You rolled a Zanzibar!')
    elif len(list(set(playerRoll))) == 1:
        diceToPoints = {
            1 : 499,
            2 : 498,
            3 : 497,
            4 : 496,
            5 : 495,
            6 : 494
        }
        points += diceToPoints.get(playerRoll[0])
    elif playerRoll == [1,2,3]:
        points += 493
    else:
        for i in playerRoll:
            points += diceToPoints.get(i)

    return points
    
def getChips(playerPoints, PlayerChips):
    # Find all players with the lowest score
    lowest_score = min(playerPoints)
    lowest_scorers = [i for i, score in enumerate(playerPoints) if score == lowest_score]
    chipsChange = 0

    # Determine chipsChange based on playerPoints
    if 493 in playerPoints:
        chipsChange = 4
    elif 500 in playerPoints:
        chipsChange = 4
    elif any(x in playerPoints for x in range(494, 500)):
        chipsChange = 3
    else:
        chipsChange = 1

    # Add chipsChange to all players except the lowest scorers
    for i in range(len(PlayerChips)):
        if i not in lowest_scorers:
            PlayerChips[i] -= chipsChange

    # Deduct the correct amount of chips for each lowest scorer
    for scorer in lowest_scorers:
        PlayerChips[scorer] += chipsChange * (len(PlayerChips) - len(lowest_scorers))

    return PlayerChips

def print_table(playerPoints, playerChips, numPlayers, playerNames):
    header = ''
    for i in range(numPlayers):
        header += playerNames[i] + (' ' * (11 - len(playerNames[i])))
    separator = "-" * (22)

    # Data rows
    points_row = " | ".join([f"{points:>7}" for points in playerPoints])
    chips_row = " | ".join([f"{chips:>7}" for chips in playerChips])

    # print(header)
    return (" " * 13 + header) + '\n' + (" " * 8 + separator) + '\n' + (f"{'Points':<10}" + points_row) + '\n' + (f"{'Chips':<10}" + chips_row)

def print_die_faces(roll):
    """Prints the die faces for the given roll."""
    die_faces = {
        1: ["|‾‾‾‾‾|", "|  •  |", "|_____|"],
        2: ["|‾‾‾•‾|", "|     |", "|_•___|"],
        3: ["|‾‾‾•‾|", "|  •  |", "|_•___|"],
        4: ["|‾•‾•‾|", "|     |", "|_•_•_|"],
        5: ["|‾•‾•‾|", "|  •  |", "|_•_•_|"],
        6: ["|‾•‾•‾|", "| • • |", "|_•_•_|"],
    }

    # Split faces of each die into lines
    dice_lines = [die_faces[d] for d in roll]

    # Print the faces side by side
    for i in range(3):  # Each die has 3 rows
        print("   ".join(dice_lines[j][i] for j in range(3)))

def diceGame():
    numPlayers = int(input('How many people are playing: '))
    playerNames = []
    playerChips = []
    playerPoint = []

    # Collect player names
    for i in range(numPlayers):
        name = input(f"Enter Player {i + 1}'s name: ")
        playerNames.append(name)
        playerChips.append(5)  # Initialize chips for each player

    maxNumRolls = 2
    firstRound = True
    while any(i > 0 for i in playerChips):  # Game ends when no chips are left
        playerChips = [max(0, chips) for chips in playerChips]

        if any(i == 0 for i in playerChips):  # Check if any player's chips are 0
            print('Game over')
            winner_index = playerChips.index(max(playerChips))  # Get the index of the winner
            threading.Thread(target=play_victory_sound, daemon=True).start()
            print(f'{playerNames[winner_index]} LOSES!')
            
            # Write results to the file
            with open('Zanzibar\'s Dice Game.txt', 'a') as file:
                # # Get the current time as a struct_time object
                # current_time = time.localtime()
                # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

                # file.write(formatted_time, '\n')
                # file.write(print_table(playerPoint, playerChips, numPlayers, playerNames))
                file.write(f'\n{playerNames[winner_index]} LOSES!\n')
                
            break

        if firstRound == True:
            print()
            print('First Round '.center(40, "_"))
            firstRound = False
        else:
            print()
            print('Next Round '.center(40, "_"))
            

        for i in range(numPlayers):
            title = f" {playerNames[i]}'s turn "
            print(title.center(40, "-"))
            turn = 1
            playing = True
            while playing == True:
                time.sleep(2)
                if __name__ == "__main__":
                    roll = curses.wrapper(roll_dice_animation)

                print_die_faces(roll)
                print(f"{playerNames[i]} rolled a {roll[0]}, {roll[1]}, and {roll[2]}")

                if turn <= maxNumRolls:
                    rollAgain = input('Do you want to roll again (Yes/No): ').upper()
                    if rollAgain in ['NO', 'N']:
                        playerPoint.append(getPoints(roll))
                        print()
                        print(f"{playerNames[i]} ended with {playerPoint[-1]} points in {turn} turns")
                        playing = False
                    else:
                        turn += 1
                else:
                    playerPoint.append(getPoints(roll))
                    print()
                    print(f"{playerNames[i]} ended with {playerPoint[-1]} points in {turn} turns")
                    break
                print('\n')
        
        # Update chips and display table
        playerChips = getChips(playerPoint, playerChips)
        print(print_table(playerPoint, playerChips, numPlayers, playerNames))
        print()
        time.sleep(5)
        playerPoint = []  # Reset points for the next round

menuTitle = 'Welcome to Zanzibar\'s Dice Game'
print(menuTitle)
print()

diceGame()