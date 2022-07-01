## import os
import time
import random


win_dict = {}
p1_won = []
p2_won = []

while True:

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 1
    Win = 1
    Draw = -1
    Running = 0
    Stop = 1
    Game = Running
    Mark = 'X'
    player_list = []

    print("1 to play")
    print("2 to show score")
    print("3 Exit")
    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        def DrawBoard():
            print("     |     |   ")
            print("  %c  |  %c  |  %c  " % (board[1], board[2], board[3]))
            print("_____|_____|_____")
            print("     |     |   ")
            print("  %c  |  %c  |  %c  " % (board[4], board[5], board[6]))
            print("_____|_____|_____")
            print("     |     |   ")
            print("  %c  |  %c  |  %c  " % (board[7], board[8], board[9]))
            print("     |     |   ")

        def CheckPosition(x):
            if(board[x] == ' '):
                return True
            else:
                return False

        def total_win(li):
            total = 0
            if len(li) < 0:
                for ele in range(0, len(li)):
                    total = total + li[ele]
                    return total
            else:
                return len(li)

        def CheckWin():
            global Game

            if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
                Game = Win
            elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
                Game = Win
            elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
                Game = Win

            elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
                Game = Win
            elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
                Game = Win
            elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
                Game = Win

            elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
                Game = Win
            elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
                Game = Win

            elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
                Game = Draw
            else:
                Game = Running

        p1 = input("Player 1 Enter Your Name: ")
        player_list.append(p1)
        p2 = input("Player 2 Enter Your Name: ")
        player_list.append(p2)
        mark_p1 = ""
        mark_p2 = ""
        win_dict.update({p1: total_win(p1_won)})
        win_dict.update({p2: total_win(p2_won)})
        if p1:
            #     print(f"{p1}'s chance")
            mark_inp = input(f"{p1} Please Input Your Choice [X] or [0] : ")

        print()
        print()
        # toss = random.choice(player_list)
        # print(toss)
#         time.sleep(3)
        print()
        print()
        print()
        while(Game == Running):
            # os.system('cls')
            DrawBoard()
            if(player % 2 != 0):
                if mark_inp == "X":
                    mark_p1 = mark_inp
                    print(f"{p1}'s chance")
                    Mark = mark_p1

                elif mark_inp == "0" or mark_inp == "O" or mark_inp == "o":
                    mark_p1 = mark_inp
                    print(f"{p1}'s chance")
                    Mark = mark_p1

            else:
                if p2:
                    #             print(f"{p2}'s chance")
                    if mark_p1 == "X":
                        mark_p2 = "0"
                        print(f"{p2}'s chance")
                        Mark = mark_p2

                    elif mark_p1 == "0" or mark_p1 == "O" or mark_p1 == "o":
                        mark_p2 = "X"
                        print(f"{p2}'s chance")
                        Mark = mark_p2

            try:
                choice = int(
                    input("Enter the position between [1-9] where you want to mark : "))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                continue

            if choice > 0 and choice < 10:
                if(CheckPosition(choice)):
                    board[choice] = Mark
                    player += 1
                    CheckWin()

            else:
                print("valid Number")
                continue

        print()
        print()
        print()

        DrawBoard()
        if(Game == Draw):
            print("Game Draw")
        elif(Game == Win):
            player -= 1
            if(player % 2 != 0):
                count = 0
                print(f"{p1} Won the game")
                count += 1
                p1_won.append(count)
                win_dict.update({p1: total_win(p1_won)})
            else:
                count = 0
                print(f"{p2} Won the game")
                count += 1
                p2_won.append(count)
                win_dict.update({p2: total_win(p2_won)})

    elif ch == 2:
        print()
        print()
        print()
        print("Name" + ' : ' + "Score")
        for key, value in win_dict.items():
            print(key, ' : ', value)
        print()
        print()
        print()

    elif ch == 3:
        break

    else:
        print("Enter Valid Choice")
