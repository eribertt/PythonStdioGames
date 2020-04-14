"""The Monty Hall Problem, by Al Sweigart al@inventwithpython.com
A simulation of the Monty Hall game show problem.
More info at https://en.wikipedia.org/wiki/Monty_Hall_problem
This and other games are available at https://nostarch.com/XX
Tags: large, game, math, simulation"""
__version__ = 0
import random, sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

print('''The Monty Hall Problem, by Al Sweigart al@inventwithpython.com

In the Monty Hall game show, you can pick one of three doors. One door
has a new car for a prize. The other two doors have worthless goats:
{}
Say you pick Door #1.
Before the door you choose is opened, another door with a goat is opened:
{}
You can choose to either open the door you originally picked, or switch
to the other unopened door.

It may seem like it doesn't matter if you switch or not, but your odds
do improve if you switch doors! This program demonstrates the Monty Hall
problem by letting you do repeated experiments.

You can read an explanation of why switching is better at
https://en.wikipedia.org/wiki/Monty_Hall_problem
'''.format(ALL_CLOSED, THIRD_GOAT))

input('Press Enter to start...')


switchWins = 0
switchLosses = 0
stayWins = 0
stayLosses = 0
while True:  # Main program loop.
    # The computer picks which door has the car:
    doorThatHasCar = random.randint(1, 3)

    # Ask the player to pick a door:
    print(ALL_CLOSED)
    while True:  # Keep asking the player until they enter a valid door.
        print('Pick a door 1, 2, or 3 (or "quit" to stop):')
        response = input('> ').upper()
        if response == 'QUIT':
            # End the game.
            print('Thanks for playing!')
            sys.exit()

        if response == '1' or response == '2' or response == '3':
            break
    doorPick = int(response)

    # Figure out which goat door to show the player:
    while True:
        # Select a door that is a goat and not picked by the player:
        showGoatDoor = random.randint(1, 3)
        if showGoatDoor != doorPick and showGoatDoor != doorThatHasCar:
            break

    # Show this goat door to the player:
    if showGoatDoor == 1:
        print(FIRST_GOAT)
    elif showGoatDoor == 2:
        print(SECOND_GOAT)
    elif showGoatDoor == 3:
        print(THIRD_GOAT)

    print('Door {} contains a goat!'.format(showGoatDoor))

    # Ask the player if they want to switch:
    while True:  # Keep asking until the player enters Y or N.
        print('Do you want to switch doors? Y/N')
        switch = input('> ').upper()
        if switch == 'Y' or switch == 'N':
            break

    # Switch the player's door if they wanted to switch:
    if switch == 'Y':
        if doorPick == 1 and showGoatDoor == 2:
            doorPick = 3
        elif doorPick == 1 and showGoatDoor == 3:
            doorPick = 2
        elif doorPick == 2 and showGoatDoor == 1:
            doorPick = 3
        elif doorPick == 2 and showGoatDoor == 3:
            doorPick = 1
        elif doorPick == 3 and showGoatDoor == 1:
            doorPick = 2
        elif doorPick == 3 and showGoatDoor == 2:
            doorPick = 1

    # Open all the doors:
    if doorThatHasCar == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif doorThatHasCar == 3:
        print(THIRD_CAR_OTHERS_GOAT)

    print('Door {} has the car!'.format(doorThatHasCar))

    # Record wins and losses for switching and not switching:
    if doorPick == doorThatHasCar:
        print('You won!')
        if switch == 'Y':
            switchWins += 1
        elif switch == 'N':
            stayWins += 1
    else:
        print('Sorry, you lost.')
        if switch == 'Y':
            switchLosses += 1
        elif switch == 'N':
            stayLosses += 1

    # Calculate success rate of switching and not switching:
    totalSwitches = switchWins + switchLosses
    if totalSwitches != 0:  # Prevent zero-divide error.
        switchSuccess = round(switchWins / totalSwitches * 100, 1)
    else:
        switchSuccess = 0.0

    totalStays = stayWins + stayLosses
    if (stayWins + stayLosses) != 0:  # Prevent zero-divide.
        staySuccess = round(stayWins / totalStays * 100, 1)
    else:
        staySuccess = 0.0

    print()
    print('Switching:     ', end='')
    print('{} wins, {} losses, '.format(switchWins, switchLosses))
    print('success rate {}%'.format(switchSuccess))
    print('Not switching: ', end='')
    print('{} wins, {} losses, '.format(stayWins, stayLosses))
    print('success rate {}%'.format(staySuccess))
    print()
    input('Press Enter repeat the experiment...')
