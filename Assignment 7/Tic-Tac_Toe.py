
from tabulate import tabulate as tbt
import random as rnd
import sys
import os
import pyfiglet
import colorama
import time as tm
colorama.init()

start_red = "\033[1;91m"
end_red = "\033[0;0m"

start_blue = "\033[1;94m"
end_blue = "\033[0;0m"

start_green = "\033[1;92m"
end_green = "\033[0;0m"

start_orange = "\033[1;93m"
end_orange = "\033[0;0m"

start_grey = "\033[1;90m"
end_grey = "\033[0;0m"

start_cyan = "\033[1;96m"
end_cyan = "\033[0;0m"

start_pink = "\033[1;95m"
end_pink = "\033[0;0m"

p1 = start_red + "X" + end_red
p2 = start_blue + "O" + end_blue
board = [[None for j in range(3)] for i in range(3)]

def clear_board():  # Clearing Board
    n = len(board)
    for i in range(n):
        for j in range(n):
            board[i][j] = None

def show_board():  # Printing Board
    board_show = [[board[0][0], start_green + "┃" + end_green, board[0][1], start_green + "┃" + end_green, board[0][2]],
                  [start_green + "━" + end_green, start_green + "━" + end_green,
                   start_green + "━" + end_green, start_green + "━" + end_green,
                   start_green + "━" + end_green],
                  [board[1][0], start_green + "┃" + end_green, board[1]
                      [1], start_green + "┃" + end_green, board[1][2]],
                  [start_green + "━" + end_green, start_green + "━" + end_green,
                   start_green + "━" + end_green, start_green + "━" + end_green,
                   start_green + "━" + end_green],
                  [board[2][0], start_green + "┃" + end_green, board[2][1], start_green + "┃" + end_green, board[2][2]]]
    print()
    for i in range(5):
        for j in range(5):
            if board_show[i][j] == None:
                print(" ", end=" ")

            else:
                print(board_show[i][j], end=" ")

        print()
    print()

def Main_Menu():  # Printing Main Menu
    headers = [start_grey + "Choose an Option" + end_grey]
    table = [[start_grey + "1." + end_grey + start_cyan + "PvA" + end_cyan],
             [start_grey + "2." + end_grey + start_cyan + "PvP" + end_cyan],
             [start_grey + "Q." + end_grey + start_cyan + "Exit" + end_cyan]]

    print(tbt(table, headers, tablefmt="fancy_grid"), "\n")
    option = input("-Waiting For You're Desire: ")
    return option

def Player(n, p1_p2):  # Players Moves
    while True:
        if n == 1 or n == 2:
            row, col = list(map(int, input(
                f"\n- Player {n} - \nEnter Row and Columns to Fix spot: ").split()))
            row -= 1
            col -= 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == None:
                    board[row][col] = p1_p2
                    os.system("cls")
                    print(f"\n- Player {n} -")
                    show_board()
                    break

                else:
                    os.system("cls")
                    print("Its Already Taken!")
                    show_board()
                    continue

            else:
                os.system("cls")
                print("Invalid Input!")
                show_board()
                continue

        elif n == 0:
            row, col = list(
                map(int, input(f"\n- Player - \nEnter Row and Columns to Fix spot: ").split()))
            row -= 1
            col -= 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == None:
                    board[row][col] = p1_p2
                    os.system("cls")
                    print("\n- Player -")
                    show_board()
                    break

                else:
                    os.system("cls")
                    print("Its Already Taken!")
                    show_board()
                    continue

            else:
                os.system("cls")
                print("Invalid Input!")
                show_board()
                continue

def AI():  # AI Moves
    while True:
        row = rnd.randint(0, 2)
        col = rnd.randint(0, 2)

        if board[row][col] == None:
            board[row][col] = p2
            os.system("cls")
            print("\n- AI -")
            show_board()
            break

def is_player_win(player):  # Checking Win Conditions
    n = len(board)
    # Check Horizontaly
    for i in range(len(board)):
        win = True
        for j in range(len(board)):
            if board[i][j] != player:
                win = False
                break

        if win:
            return True

    # Check Vertically
    for i in range(len(board)):
        win = True
        for j in range(len(board)):
            if board[j][i] != player:
                win = False
                break

        if win:
            return True

    # Checking Diagonals
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break

    if win:
        return True

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break

    if win:
        return True

    return False

def is_board_filled():  # Cheching Draws
    for row in board:
        for item in row:
            if item == None:
                return False
    return True

def convert_seconds(seconds):  # Converts Seconds
    return tm.strftime("%M:%S", tm.gmtime(seconds))

os.system("cls")
while True:
    option = Main_Menu()
    os.system("cls")

    if option == "1": # PvA
        start = tm.time()
        turn = rnd.randint(0, 1) # 0 = Player , 1 = AI
        while True:
            if turn == 0: # Player's First Turn
                Player(0 , p1) # - X -

                if is_player_win(p1): # Player 1 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format(" Player \n      Won      " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("Draw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break
                
                tm.sleep(1.5)
                AI() # - O -

                if is_player_win(p2): # Player 2 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format("      AI     \n   Won   " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("Draw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

            else: # AI's First Turn
                AI() # - O -

                if is_player_win(p2): # Player 2 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format("      AI     \n   Won   " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("Draw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                Player(0 , p1) # - X -

                if is_player_win(p1): # Player 1 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format(" Player \n      Won      " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("Draw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

        stop = tm.time()
        print("Time Spent:" , convert_seconds(stop - start))

    elif option == "2": # PvP
        start = tm.time()
        turn = rnd.randint(0, 1) # 0 = Player 1 , 1 = Player 2
        while True:
            if turn == 0: # Player 1's First Turn
                Player(1 , p1) # - X -

                if is_player_win(p1): # Player 1 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format("Player 1\n       Won       " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("Draw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                Player(2 , p2) # - O -

                if is_player_win(p2): # Player 2 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format("Player 2\n       Won       " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("Draw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

            else: # Player 2's First Turn
                Player(2 , p2) # - O -

                if is_player_win(p2): # Player 1 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format("\nPlayer 2\n       Won       " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("\nDraw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                Player(1 , p1) # - X -

                if is_player_win(p1): # Player 2 Won
                    os.system("cls")
                    result = pyfiglet.figlet_format("\nPlayer 1\n       Won       " + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

                if is_board_filled(): # Draw
                    os.system("cls")
                    result = pyfiglet.figlet_format("\nDraw!" + "\n" , font = "banner3-d")
                    print(start_pink + result + end_pink)
                    clear_board()
                    break

        stop = tm.time()
        print("Time Spent:" , convert_seconds(stop - start))

    elif option.lower() == "q": # Exit
        sys.exit(1)

    else: # Invalid Option
        result = pyfiglet.figlet_format("Invalid!" + "\n" , font = "banner3-d")
        print(start_pink + result + end_pink)
        continue