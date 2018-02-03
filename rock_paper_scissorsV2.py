import random
from statistics import mode

def main():
    choice = 0
    previous = 0
    comp_wins = 0
    player_wins = 0
    player = 0
    rounds = 5
    list_moves = []
    most_common = 0

    print("Welcome to Rock-Paper-Scissors\n")
    print("Rock = 1, Paper = 2, Scissors = 3\n")
    rounds = int(input("Enter number of rounds: "))
    print("\n")

    for i in range(0, rounds):
        player = int(input("Enter your move:"))
        list_moves.append(player)
        
        try:
            most_common = mode(list_moves)
        except StatisticsError:
            choice = random.randint(0,4)
        
        if (most_common == 1):
            choice = 3
        elif (most_common == 2):
            choice = 1
        else :
            choice = 2
            
        if (player == 1):

            if (choice == 1):
                print("Computer chose :", choice, "\n")
                print ("DRAW!\n")
            elif (choice == 2):
                print("Computer chose :", choice, "\n")
                print ("Player wins\n")
                player_wins += 1
            elif (choice == 3):
                print("Computer chose :", choice, "\n")
                print ("Computer wins!\n")
                comp_wins += 1
            else :
                raise Exception ("Computer move ERROR\n")

        elif (player == 2):

            if (choice == 1):
                print("Computer chose :", choice, "\n")
                print ("Computer wins!\n")
                comp_wins += 1
            elif (choice == 2):
                print("Computer chose :", choice, "\n")
                print ("DRAW!\n")
            elif (choice == 3):
                print("Computer chose :", choice, "\n")
                print ("Player wins\n")
                player_wins += 1
            else :
                raise Exception ("Computer move ERROR\n")
        elif (player == 3):

            if (choice == 1):
                print("Computer chose :", choice, "\n")
                print ("Player wins\n")
                player_wins += 1
            elif (choice == 2):
                print("Computer chose :", choice, "\n")
                print ("Computer wins!\n")
                comp_wins += 1
            elif (choice == 3):
                print("Computer chose :", choice, "\n")
                print ("DRAW!\n")
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


main()
