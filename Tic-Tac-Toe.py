# #!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on August 11, 2021
# Last edited on August 22, 2021
# Runs the tic-tac-toe game


import os
import sys
import random


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def game_startup():
    # Function for startup
    game_state = False
    screen_clear()
    print("Welcome to Malcolm's Tic-Tac-Toe game!")
    start_var = (input("Press b for intructions\nPress a to start "))
    if start_var == "a":
        main()
    elif start_var == "b":
        intructions()
    screen_clear()
    return game_state


def game_terminatation(game, team):
    # Function for ending the game
    screen_clear()
    print("Game Over!")
    if game == 0:
        print("{}'s Wins!".format(team))
    if game == 1:
        print("No contest")
    end_var = (input("Press a to restart\nPress b to exit "))
    if end_var == "a":
        game_startup()
    if end_var == "b":
        sys.exit()
    else:
        print("Unknown input")
        game_terminatation(team)


def intructions():
    # Function for intructions
    screen_clear()
    print("To start your turn, enter a location from 1-9: ")
    print("1|2|3\n4|5|6\n7|8|9")
    return_key = (input("Press any button to return to the home screen "))
    screen_clear()
    main()


def grid_creation():
    # Function for grid generation
    row_list = []
    start_state = " "
    for row_number in range(0, 3):
        row = []
        row_list.append(row)
        for column_number in range(0, 3):
            row.append(start_state)
    for row in row_list:
        print("|".join(row))
    return row_list


def game_logic(row_list, player_slot, team):
    # Function for the tic-tac-toe game logic
    player_slot -= 1
    game = -1
    row1 = row_list[0]
    row2 = row_list[1]
    row3 = row_list[2]
    slot1 = row1[0]
    slot2 = row1[1]
    slot3 = row1[2]
    slot4 = row2[0]
    slot5 = row2[1]
    slot6 = row2[2]
    slot7 = row3[0]
    slot8 = row3[1]
    slot9 = row3[2]
    slot_list = []
    slot_list.append(slot1)
    slot_list.append(slot2)
    slot_list.append(slot3)
    slot_list.append(slot4)
    slot_list.append(slot5)
    slot_list.append(slot6)
    slot_list.append(slot7)
    slot_list.append(slot8)
    slot_list.append(slot9)
    slot_list[player_slot] = team
    column1 = [slot_list[0], slot_list[1], slot_list[2]]
    column2 = [slot_list[3], slot_list[4], slot_list[5]]
    column3 = [slot_list[6], slot_list[7], slot_list[8]]
    row_1 = [slot_list[0], slot_list[3], slot_list[6]]
    row_2 = [slot_list[1], slot_list[4], slot_list[7]]
    row_3 = [slot_list[2], slot_list[5], slot_list[8]]
    diagonal1 = [slot_list[0], slot_list[4], slot_list[8]]
    diagonal2 = [slot_list[2], slot_list[4], slot_list[6]]
    if column1.count("x") > 2:
        game = 0
    if column1.count("0") > 2:
        game = 0
    if column2.count("x") > 2:
        game = 0
    if column2.count("0") > 2:
        game = 0
    if column3.count("x") > 2:
        game = 0
    if column3.count("0") > 2:
        game = 0
    if row_1.count("x") > 2:
        game = 0
    if row_1.count("0") > 2:
        game = 0
    if row_2.count("x") > 2:
        game = 0
    if row_2.count("0") > 2:
        game = 0
    if row_3.count("x") > 2:
        game = 0
    if row_3.count("0") > 2:
        game = 0
    if diagonal1.count("x") > 2:
        game = 0
    if diagonal1.count("0") > 2:
        game = 0
    if diagonal2.count("x") > 2:
        game = 0
    if diagonal2.count("0") > 2:
        game = 0
    if slot_list.count(" ") == 0:
        game = 1
    if game > -1:
        game_terminatation(game, team)
    return slot_list


def grid_changes(slot_list):
    # Function for changes to the original grid based on game logic
    counter = -1
    new_list = []
    for row_number in range(0, 3):
        row = []
        new_list.append(row)
        for column_number in range(0, 3):
            counter = counter + 1
            row.append(slot_list[counter])
    for row in new_list:
        print("|".join(row))
    return new_list


def cpu_process(move_list, turn_counter, row_list, cpu_move_list):
    # Function for cpu moves
    # Figure this shit out holy fuck
    while True:
        cpu_win_cond = []
        player_win_cond = []
        last_move = []
        defend = -1
        win_cond = -1
        move = 0
        cpu_move = 0
        slot_1_adj = (2, 4, 5)
        slot_2_adj = (1, 3, 5)
        slot_3_adj = (2, 5, 6)
        slot_4_adj = (1, 5, 7)
        slot_5_adj = (1, 2, 3, 4, 6, 7, 8, 9)
        slot_6_adj = (3, 5, 9)
        slot_7_adj = (4, 5, 8)
        slot_8_adj = (5, 7, 9)
        slot_9_adj = (5, 6, 8)
        slot_adjs = []
        slot_adjs.append(slot_1_adj)
        slot_adjs.append(slot_2_adj)
        slot_adjs.append(slot_3_adj)
        slot_adjs.append(slot_4_adj)
        slot_adjs.append(slot_5_adj)
        slot_adjs.append(slot_6_adj)
        slot_adjs.append(slot_7_adj)
        slot_adjs.append(slot_8_adj)
        slot_adjs.append(slot_9_adj)
        row1 = row_list[0]
        row2 = row_list[1]
        row3 = row_list[2]
        slot1 = row1[0]
        slot2 = row1[1]
        slot3 = row1[2]
        slot4 = row2[0]
        slot5 = row2[1]
        slot6 = row2[2]
        slot7 = row3[0]
        slot8 = row3[1]
        slot9 = row3[2]
        slot_list = []
        slot_list.append(slot1)
        slot_list.append(slot2)
        slot_list.append(slot3)
        slot_list.append(slot4)
        slot_list.append(slot5)
        slot_list.append(slot6)
        slot_list.append(slot7)
        slot_list.append(slot8)
        slot_list.append(slot9)
        column1 = [slot_list[0], slot_list[1], slot_list[2]]
        column2 = [slot_list[3], slot_list[4], slot_list[5]]
        column3 = [slot_list[6], slot_list[7], slot_list[8]]
        row_1 = [slot_list[0], slot_list[3], slot_list[6]]
        row_2 = [slot_list[1], slot_list[4], slot_list[7]]
        row_3 = [slot_list[2], slot_list[5], slot_list[8]]
        diagonal1 = [slot_list[0], slot_list[4], slot_list[8]]
        diagonal2 = [slot_list[2], slot_list[4], slot_list[6]]
        # If statements for win options
        if column1.count("0") == 2:
            if column1.count(" ") == 1:
                win_cond = 0
                cpu_win_cond.append(column1)
        if column2.count("0") == 2:
            if column2.count(" ") == 1:
                win_cond = 1
                cpu_win_cond.append(column2)
        if column3.count("0") == 2:
            if column3.count(" ") == 1:
                win_cond = 2
                cpu_win_cond.append(column3)
        if row_1.count("0") == 2:
            if row_1.count(" ") == 1:
                win_cond = 3
                cpu_win_cond.append(row_1)
        if row_2.count("0") == 2:
            if row_2.count(" ") == 1:
                win_cond = 4
                cpu_win_cond.append(row_2)
        if row_3.count("0") == 2:
            if row_3.count(" ") == 1:
                win_cond = 5
                cpu_win_cond.append(row_3)
        if diagonal1.count("0") == 2:
            if diagonal1.count(" ") == 1:
                win_cond = 6
                cpu_win_cond.append(diagonal1)
        if diagonal2.count("0") == 2:
            if diagonal2.count(" ") == 1:
                win_cond = 7
                cpu_win_cond.append(diagonal2)
        # If statements for defend options
        if column1.count("x") == 2:
            if column1.count(" ") == 1:
                defend = 0
                player_win_cond.append(column1)
        if column2.count("x") == 2:
            if column2.count(" ") == 1:
                defend = 1
                player_win_cond.append(column2)
        if column3.count("x") == 2:
            if column3.count(" ") == 1:
                defend = 2
                player_win_cond.append(column3)
        if row_1.count("x") == 2:
            if row_1.count(" ") == 1:
                defend = 3
                player_win_cond.append(row_1)
        if row_2.count("x") == 2:
            if row_2.count(" ") == 1:
                defend = 4
                player_win_cond.append(row_2)
        if row_3.count("x") == 2:
            if row_3.count(" ") == 1:
                defend = 5
                player_win_cond.append(row_3)
        if diagonal1.count("x") == 2:
            if diagonal1.count(" ") == 1:
                defend = 6
                player_win_cond.append(diagonal1)
        if diagonal2.count("x") == 2:
            if diagonal2.count(" ") == 1:
                defend = 7
                player_win_cond.append(diagonal2)
        if turn_counter == 2:
            if 5 == move_list[0]:
                move = random.randint(1, 9)
            else:
                move = 5
        if turn_counter >= 4:
            adj_check = True
            last_move = cpu_move_list[0] - 1
            last_move_adj = slot_adjs[last_move]
            for var1 in move_list:
                for var2 in last_move_adj:
                    if var2 == var1:
                        adj_check = False
                        break
                    break
            for var1 in cpu_move_list:
                for var2 in last_move_adj:
                    if var2 == var1:
                        adj_check = False
                        break
                    break
            if win_cond >= 0:
                if win_cond == 0:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 1
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 1
                if win_cond == 1:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 4
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 1
                if win_cond == 2:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 7
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 1
                if win_cond == 3:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 1
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 3
                if win_cond == 4:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 2
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 3
                if win_cond == 5:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 3
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 3
                if win_cond == 6:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 1
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 4
                if win_cond == 7:
                    win_slot = cpu_win_cond[0]
                    loop_counter = 3
                    for var in win_slot:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 2
            elif defend >= 0:
                if defend == 0:
                    def_cond = player_win_cond[0]
                    loop_counter = 1
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 1
                if defend == 1:
                    def_cond = player_win_cond[0]
                    loop_counter = 4
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 1
                if defend == 2:
                    def_cond = player_win_cond[0]
                    loop_counter = 7
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 1
                if defend == 3:
                    def_cond = player_win_cond[0]
                    loop_counter = 1
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 3
                if defend == 4:
                    def_cond = player_win_cond[0]
                    loop_counter = 2
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 3
                if defend == 5:
                    def_cond = player_win_cond[0]
                    loop_counter = 3
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 3
                if defend == 6:
                    def_cond = player_win_cond[0]
                    loop_counter = 1
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 4
                if defend == 7:
                    def_cond = player_win_cond[0]
                    loop_counter = 3
                    for var in def_cond:
                        if var == " ":
                            move = loop_counter
                            break
                        loop_counter += 2
            elif adj_check == True:
                last_move = move_list[0] - 1
                last_move_adj = slot_adjs[last_move]
                move = random.choice(last_move_adj)
            else:
                move = random.randint(1,9)
        return move




def main():
    # Function for UI
    game_mode = input("Press a for a player vs player match\nPress b for player vs Ai match: ")
    if game_mode == "a":
        game_mode = 0
    elif game_mode == "b":
        game_mode = 1
    else:
        print("Unknown input")
        main()
    turn_counter = 1
    users_moves = []
    slot_location = 0
    cpu_move_list = []
    move_list = []
    row_list = grid_creation()
    while True:
        slot_check = True
        if game_mode == 0:
            # Section for pvp game
            if (turn_counter % 2) == 0:
                print("Player 2's turn")
                team = "0"
            else:
                print("Player 1's turn")
                team = "x"
            player_slot_location = (input("Which box?: "))
            try:
                slot_location = int(player_slot_location)
                try:
                    slot_location in range(0, 9)
                    users_moves.append(slot_location)
                    if users_moves.count(slot_location) > 1:
                        print("That spot is taken, choose another location")
                        continue
                    slot_list = game_logic(row_list, slot_location, team)
                    row_list = grid_changes(slot_list)
                    turn_counter += 1
                except Exception:
                    print("{} is not a number from 1-9".format(slot_location))
                    continue
            except Exception:
                print("{} is not an integer".format(player_slot_location))
                continue
        if game_mode == 1:
            # Section for pvCPU game
            if (turn_counter % 2) == 1:
                print("Player 1's turn")
                team = "x"
                player_slot_location = (input("Which box?: "))
                try:
                    slot_location = int(player_slot_location)
                    try:
                        slot_location in range(0, 9)
                        for var in move_list:
                            if slot_location == var:
                                slot_check = False
                                break
                        for var in cpu_move_list:
                            if slot_location == var:
                                slot_check = False
                                break
                        if slot_check == False:
                            print("You cannot move there")
                            continue
                        move_list.append(slot_location)
                        slot_list = game_logic(row_list, slot_location, team)
                        row_list = grid_changes(slot_list)
                        turn_counter += 1
                    except Exception:
                        print("{} is not a number from 1-9")
                        continue
                except Exception:
                    print("{} is not an integer".format(player_slot_location))
                    continue
            else:

                print("CPU's Turn")
                team = "0"
                while True:
                    slot_check = True
                    cpu_location = cpu_process(move_list, turn_counter, row_list, cpu_move_list)
                    cpu_move_list.append(cpu_location)
                    if cpu_location == slot_location:
                        continue
                    for var in move_list:
                        if cpu_location == var:
                               slot_check = True
                        else:
                            slot_check = False
                    else:
                        slot_check = False
                    if slot_check == False:
                        break
                slot_list = game_logic(row_list, cpu_location, team)
                row_list = grid_changes(slot_list)
                turn_counter += 1


if __name__ == "__main__":
    game_startup()
