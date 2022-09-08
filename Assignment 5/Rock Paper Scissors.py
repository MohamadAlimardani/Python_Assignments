
import sys
from tabulate import tabulate
import random as rnd
import colorama

colorama.init()
start_green = "\033[1;92m"
end_green = "\033[0;0m"

start_cyan = "\033[1;96m"
end_cyan = "\033[0;0m"

start_red = "\033[1;91m"
end_red = "\033[0;0m"

start_pink = "\033[1;95m"
end_pink = "\033[0;0m"

start_orange = "\033[1;93m"
end_orange = "\033[0;0m"

start_grey = "\033[1;90m"
end_grey = "\033[0;0m"

start_blue = "\033[1;94m"
end_blue = "\033[0;0m"

# 1 = Rock / 2 = Paper / 3 = Scissors

score_ai, score_player_vs_ai , rps_list , point_pp = 0, 0 , [start_green + "Rock" + end_green , start_green + "Paper" + end_green , start_green + "Scissors" + end_green] , [start_pink + "0" + end_pink , start_pink + "+1" + end_pink]
score_p1 , score_p2 , p1_p2= 0 , 0 , [start_orange + "- Player 1 -" + end_orange , start_orange + "- Player 2 -" + end_orange]

print("\n\nWelcome To Rock - Paper - Scissors Game !\n\n")

headers_start = [start_grey + "Choose an Option:" + end_grey]
table_start = [[start_cyan + "1.PvA (vs AI)" + end_cyan], [start_cyan + "2.PvP" + end_cyan] , [start_cyan + "Q.Exit" + end_cyan]]

inner_table = [[start_green + "1.Rock" + end_green], [start_green + "2.Paper" + end_green], [start_green + "3.Scissors" + end_green]]

while True:
    print(tabulate(table_start , headers_start , tablefmt="fancy_grid") , "\n")
    option_input = input("-Waiting For You're Desire: ")

    if option_input == "1": # PvA
        print("\n\n")
        wining_score_0 = int(input("How Many Points You Desire To Play? "))
        print("\n\n")
        while True:
            if score_ai == wining_score_0 or score_player_vs_ai == wining_score_0:
                if score_ai > score_player_vs_ai:
                    headers_final = [start_orange + "AI Has Won!" + end_orange , start_blue + "SCORES" + end_blue]
                    table_final = [[start_red + "AI" + end_red, start_pink + str(score_ai) + end_pink], [start_red + "Player" + end_red , start_pink + str(score_player_vs_ai) + end_pink]]
                    print("\n\n" + tabulate(table_final, headers_final, tablefmt="fancy_grid"), "\n\n")
                    score_player_vs_ai , score_ai = 0 , 0
                    break
                
                else:
                    headers_final = [start_orange + "Player Has Won!" + end_orange , start_blue + "SCORES" + end_blue]
                    table_final = [[start_red + "AI" + end_red, start_pink + str(score_ai) + end_pink], [start_red + "Player" + end_red , start_pink + str(score_player_vs_ai) + end_pink]]
                    print("\n\n" + tabulate(table_final, headers_final, tablefmt="fancy_grid"), "\n\n")
                    score_player_vs_ai , score_ai = 0 , 0
                    break
            
            else:
                print(tabulate(inner_table , headers_start , tablefmt="fancy_grid") , "\n")
                
                ai_menu = int(input("-Waiting For You're Desire: "))
                
                ai_guess = rnd.randint(1, 3)
                
                if ai_guess == ai_menu: # Draws
                    headers_PvA = [5 * " " + start_orange + "Draw!" + end_orange , start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[0]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    continue
                
                elif ai_menu == 1 and ai_guess == 2: # Rock x Paper
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[1]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    score_ai += 1
                    continue
                
                elif ai_menu == 1 and ai_guess == 3: # Rock x Scissors
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[0]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[1]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    score_player_vs_ai += 1
                    continue
                    
                elif ai_menu == 2 and ai_guess == 1: # Paper x Rock
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[0]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[1]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    score_player_vs_ai += 1
                    continue
        
                elif ai_menu == 2 and ai_guess == 3: # Paper x Scissors
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[1]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    score_ai += 1
                    continue
                
                elif ai_menu == 3 and ai_guess == 1: # Scissors x Rock
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[1]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    score_ai += 1
                    continue
                    
                elif ai_menu == 3 and ai_guess == 2: # Scissors x Paper
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvA = [[start_red + "AI" + end_red, start_green + rps_list[ai_guess-1] + end_green , point_pp[0]], [start_red + "Player" + end_red, start_green + rps_list[ai_menu-1] + end_green , point_pp[1]]]
                    print(tabulate(table_PvA, headers_PvA, tablefmt="fancy_grid"), "\n")
                    score_player_vs_ai += 1
                    continue
                
                else:
                    print("\nInvalid Option!\nPlease Choose Wisely.\n")
                    continue
                
    elif option_input == "2": # PvP
        print("\n\n")
        wining_score_1 = int(input("How Many Points You Desire To Play? "))
        print("\n\n")
        while True:
            if score_p1 == wining_score_1 or score_p2 == wining_score_1:
                if score_p1 > score_p2:
                    headers_final = [start_orange + "Player 1 Has Won!" + end_orange , start_blue + "SCORES" + end_blue]
                    table_final = [[start_red + "Player 1" + end_red, start_pink + str(score_p1) + end_pink], [start_red + "Player 2" + end_red , start_pink + str(score_p2) + end_pink]]
                    print("\n\n" + tabulate(table_final, headers_final, tablefmt="fancy_grid"), "\n\n")
                    score_p1 , score_p2 = 0 , 0
                    break
                
                else:
                    headers_final = [start_orange + "Player 2 Has Won!" + end_orange , start_blue + "SCORES" + end_blue]
                    table_final = [[start_red + "Player 1" + end_red, start_pink + str(score_p1) + end_pink], [start_red + "Player 2" + end_red , start_pink + str(score_p2) + end_pink]]
                    print("\n\n" + tabulate(table_final, headers_final, tablefmt="fancy_grid"), "\n\n")
                    score_p1 , score_p2 = 0 , 0
                    break
            
            else:
                headers_PvP = [2 * " " + p1_p2[0]]
                table_PvP = [headers_start , [start_green + "1.Rock" + end_green], [start_green + "2.Paper" + end_green], [start_green + "3.Scissors" + end_green]]
                print(tabulate(table_PvP , headers_PvP , tablefmt="fancy_grid") , "\n")
                player_1_input = int(input("-Waiting For You're Desire: "))
                
                headers_PvP = [2 * " " + p1_p2[1]]
                table_PvP = [headers_start , [start_green + "1.Rock" + end_green], [start_green + "2.Paper" + end_green], [start_green + "3.Scissors" + end_green]]
                print(tabulate(table_PvP , headers_PvP , tablefmt="fancy_grid") , "\n")
                player_2_input = int(input("-Waiting For You're Desire: "))
                
                if player_1_input == player_2_input: # Draws
                    headers_PvP_v2 = [3 * " " + start_orange + "Draw!" + end_orange , start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[0]], [start_red + "Player 2" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    continue
                
                elif player_1_input == 1 and player_2_input == 2: # Rock x Paper
                    headers_PvP_v2 = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[0]], [start_red + "Player 2" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[1]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    score_p2 += 1
                    continue
                
                elif player_1_input == 1 and player_2_input == 3: # Rock x Scissors
                    headers_PvP_v2 = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[1]], [start_red + "Player 2" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    score_p1 += 1
                    continue
                    
                elif player_1_input == 2 and player_2_input == 1: # Paper x Rock
                    headers_PvP_v2 = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[1]], [start_red + "Player 2" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    score_p1 += 1
                    continue
        
                elif player_1_input == 2 and player_2_input == 3: # Paper x Scissors
                    headers_PvP_v2 = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[0]], [start_red + "Player 2" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[1]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    score_p2 += 1
                    continue
                
                elif player_1_input == 3 and player_2_input == 1: # Scissors x Rock
                    headers_PvA = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[0]], [start_red + "Player 2s Score:" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[1]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    score_p2 += 1
                    continue
                    
                elif player_1_input == 3 and player_2_input == 2: # Scissors x Paper
                    headers_PvP_v2 = [start_red + start_blue + "CHOICES" + end_blue , start_blue + "SCORES" + end_blue]
                    table_PvP_v2 = [[start_red + "Player 1" + end_red, start_green + rps_list[player_1_input-1] + end_green , point_pp[1]], [start_red + "Player 2" + end_red, start_green + rps_list[player_2_input-1] + end_green , point_pp[0]]]
                    print(tabulate(table_PvP_v2, headers_PvP_v2, tablefmt="fancy_grid"), "\n")
                    score_p1 += 1
                    continue
                
                else:
                    print("\nInvalid Option!\nPlease Choose Wisely.\n")
                    continue
    
    elif option_input == "q" or option_input == "Q":
        sys.exit(1)
    
    else:
        print("Invalid Option!\nPlease Choose Wisely.")
        continue