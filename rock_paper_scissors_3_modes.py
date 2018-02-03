from statistics import mode
import random

def main():

    choice = 0
    previous = 0
    comp_wins = 0
    player_wins = 0
    player = 0
    win = 0
    rounds = 5
    list_moves = []
    most_common = 0
    mode_choice = 0

    print("---------------------------------------------------------------------")
    print("Welcome to Rock-Paper-Scissors!\n")
    print("Rock = 1, Paper = 2, Scissors = 3\n")
    rounds = int(input("Enter number of rounds: "))
    print("")
    print("Mode of play will be randomly selected from :")
    print("1. Random move")
    print("2. Win-Stick, Lose-Switch")
    print("3. Most common player move")

    mode_choice = random.randint(1,3)
    print("Randomly chosen mode of play: " ,mode_choice, "\n")

    for i in range(0, rounds):
        player = 0
        while ((player < 1) | (player > 3)):
            player = int(input("Enter your move:"))
        list_moves.append(player)

        if (mode_choice == 1):
            choice = random_move()
        elif (mode_choice == 2):
            choice = win_stick_lose_switch(previous, win)
        elif (mode_choice == 3):
            choice = most_chosen_player_move(list_moves)
        else :
            raise Exception ("MODE_CHOICE ERROR")


        if (player == 1):
            print("Player chose ROCK!")

            if (choice == 1):
                print("Computer chose : ROCK!\n")
                print ("DRAW!\n")
                win = 0
            elif (choice == 2):
                print("Computer chose : PAPER!\n")
                print ("Computer wins!\n")
                comp_wins += 1
                win = 1
                previous = choice
            elif (choice == 3):
                print("Computer chose : SCISSORS\n")
                print ("Player wins!\n")
                player_wins += 1
                win = 0
            else :
                raise Exception ("Computer move ERROR\n")

        elif (player == 2):
            print("Player chose PAPER!")

            if (choice == 1):
                print("Computer chose : ROCK!\n")
                print ("Player wins\n")
                player_wins += 1
                win = 0
            elif (choice == 2):
                print("Computer chose : PAPER!\n")
                print ("DRAW!\n")
                win = 0
            elif (choice == 3):
                print("Computer chose : SCISSORS\n")
                print ("Computer wins!\n")
                comp_wins += 1
                win = 1
                previous = choice
            else :
                raise Exception ("Computer move ERROR\n")

        elif (player == 3):
            print("Player chose SCISSORS!")

            if (choice == 1):
                print("Computer chose : ROCK!\n")
                print ("Computer wins!\n")
                comp_wins += 1
                win = 1
                previous = choice
            elif (choice == 2):
                print("Computer chose : PAPER!\n")
                print ("Player wins\n")
                player_wins += 1
                win = 0
            elif (choice == 3):
                print("Computer chose : SCISSORS\n")
                print ("DRAW!\n")
                win = 0
            else :
                raise Exception ("MAKING COMPUTER MOVE ERROR")
        else:
            raise Exception ("PLAYER MOVE INPUT ERROR")

        choice = 0
        player = 0

    if (comp_wins > player_wins):
        print("Computer wins! ", comp_wins, " to ", player_wins)
    elif (comp_wins < player_wins):
        print("Player wins! ", comp_wins, " to ", player_wins)
    else :
        print("Nobody wins! ", comp_wins, " to ", player_wins)


# Move making functions

def random_move():
    return random.randint(1,3)

def win_stick_lose_switch(previous, win):
    if (win == 1):
        return previous
    else :
        return random.randint(1,3)

def most_chosen_player_move(list_moves):
    most_common = 0
    try:
        most_common = mode(list_moves)
    except StatisticsError:
        return random.randint(1,3)

    if (most_common == 1):
        return 3
    elif (most_common == 2):
        return 1
    else :
        return 2

main()
