import random

def main():
    win = 0
    choice = 0
    previous = 0
    comp_wins = 0
    player_wins = 0
    player = 0
    rounds = 5

    print("Welcome to Rock-Paper-Scissors\n")
    print("Rock = 1, Paper = 2, Scissors = 3\n")
    rounds = int(input("Enter number of rounds: "))
    print("\n")

    for i in range(0, rounds):
        player = int(input("Enter your move:"))

        if (win == 1):
            choice = previous
        else :
            choice = random.randint(1,3)

        if (player == 1):

            if (choice == 1):
                print("Computer chose :", choice, "\n")
                print ("DRAW!\n")
                win = 0
            elif (choice == 2):
                print("Computer chose :", choice, "\n")
                print ("Player wins\n")
                player_wins += 1
                win = 0
            elif (choice == 3):
                print("Computer chose :", choice, "\n")
                print ("Computer wins!\n")
                comp_wins += 1
                win = 1
                previous = choice
            else :
                raise Exception ("Computer move ERROR\n")

        elif (player == 2):

            if (choice == 1):
                print("Computer chose :", choice, "\n")
                print ("Computer wins!\n")
                comp_wins += 1
                win = 1
                previous = choice
            elif (choice == 2):
                print("Computer chose :", choice, "\n")
                print ("DRAW!\n")
                win = 0
            elif (choice == 3):
                print("Computer chose :", choice, "\n")
                print ("Player wins\n")
                player_wins += 1
                win = 0
            else :
                raise Exception ("Computer move ERROR\n")
        elif (player == 3):

            if (choice == 1):
                print("Computer chose :", choice, "\n")
                print ("Player wins\n")
                player_wins += 1
                win = 0
            elif (choice == 2):
                print("Computer chose :", choice, "\n")
                print ("Computer wins!\n")
                comp_wins += 1
                win = 1
                previous = choice
            elif (choice == 3):
                print("Computer chose :", choice, "\n")
                print ("DRAW!\n")
                win = 0
            else :
                raise Exception ("COMPUTER MOVE ERROR")
        else:
            raise Exception ("PLAYER MOVE ERROR")

        choice = 0
        player = 0

    if (comp_wins > player_wins):
        print("Computer wins! ", comp_wins, " to ", player_wins)
    elif (comp_wins < player_wins):
        print("Player wins! ", comp_wins, " to ", player_wins)
    else :
        print("Nobody wins! ", comp_wins, " to ", player_wins)


main()
