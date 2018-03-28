# Gabriel Winkler
# March 22nd - 27th, 2018
# This program will play a game of rock, paper, scissors until
# the user would like to quit.

# Imports...
import random

# Function / methods

def main():
    computer = 0
    player = 0
    playAgain = "yes"
    wins = 0
    losses = 0
    ties = 0
    totalGames = 0
    

    while playAgain == "yes" or playAgain == "y":
        print("To play, enter either rock, paper, or scissors!")
        computer = randChoice()
        print("Rock, paper, scissors, SHOOT!")
        player = userChoice(player)

        print("The computer chose " + str(computer) + ".")
        print("You chose " + str(player) + ".")

        wins, losses, ties = decideWinner(computer, player, wins, losses, ties)
        

        playAgain = str(input("Would you like to play again? y/n: "))
        totalGames = totalGames + 1

    print("Out of " + str(totalGames) + " games, here's how you did:")
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))


def randChoice():
    choice = random.randint(1,3)
    if choice == 1:
        choice = "rock"
    elif choice == 2:
        choice = "paper"
    else:
        choice = "scissors"
    return choice

def userChoice(player):
    while True:
        try:
            player = int(input("Enter rock (1), paper (2), or scissors (3): "))
        except ValueError:
            print("Your input could not be understood. Please enter 1, 2, or 3.")
            continue
        else:
            if player == 1:
                player = "rock"
            elif player == 2:
                player = "paper"
            else:
                player = "scissors"
            print("Let's see...")
            break
    return player
    

def decideWinner(computer, player, wins, losses, ties):
    if computer == "rock" and player == "paper":
        wins += 1
        print("You win!")
    elif computer == "paper" and player == "scissors":
        wins += 1
        print("You win!")
    elif computer == "scissors" and player == "rock":
        wins += 1
        print("You win!")
    elif computer == "rock" and player == "scissors":
        losses += 1
        print("You lose...")
    elif computer == "paper" and player == "rock":
        losses += 1
        print("You lose...")
    elif computer == "scissors" and player == "paper":
        losses += 1
        print("You lose...")
    elif computer == player:
        ties += 1
        print("You tied!")
    
    #print("Wins: " + str(wins))
    #print("Losses: " + str(losses))
    #print("Ties: " + str(ties))
    return wins, losses, ties





# Function call for main

main()
