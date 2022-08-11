
loop_counter = 0
win = 0
lose = 0
draw = 0
score = 0
number_list = ["First Home" , "Second Home" , "Third Home" , "Fourth Home" , "First Away" , "Second Away" , "Third Away" , "Fourth Away"]

while loop_counter < 8:
    print("Enter the result of the " + number_list[loop_counter] + " match: " + "\n1.Win!" + "\n2.Draw!" + "\n3.Lose!")
    match_result = input()
    loop_counter += 1

    if match_result == '1' or match_result == 'Win' or match_result == 'win' or match_result == 'w' or match_result == 'W':
        win += 1
        score += 3
        continue
    
    elif match_result == '2' or match_result == 'Draw' or match_result == 'draw' or match_result == 'd' or match_result == 'D':
        draw += 1
        score += 1
        continue
    
    elif match_result == '3' or match_result == 'Lose' or match_result == 'lose' or match_result == 'l' or match_result == 'L':
        lose += 1
        continue
    
    else:
        loop_counter -= 1
        print("Invalid option!!\nPlease ReEnter You're option please: ")
        continue

print("Result of the football league of women:\nTeam:Football-Rezvan\n\n\n" + "" + "Matches Played" + 5 * " " + "Win" + 5 * " " + "Draw" + 5 * " " + "Lose" + 5 * " " + "Score" + "\n" + 52 * "-" + "\n" + 7 * " " + str(loop_counter) + 12 * " " + str(win) + 7 * " " + str(draw) + 8 * " " + str(lose) + 9 * " " + str(score) + "\n\n\n")