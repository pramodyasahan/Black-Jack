from numpy import random
import os
from art import logo

def Deel_Card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return(random.choice(cards))

def Card_Sum(arr):
    return(sum(arr))

def Deal_Ace(arr):
    ace = False
    for x in arr:
        if x == 11:
            ace = True
    return ace

def End(ply, comp, scoreP, scoreC):
    print(f"Your final hand: {ply}, final score: {scoreP}")
    print(f"Computer's final hand: {comp}, final score: {scoreC}")




start = True
while start:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    os.system('clear')

    print(logo)
    if user_input.lower() == "y":
        start = True
    else:
        start = False

    player = []
    computer = []

    for x in range(2):
        player.append(Deel_Card())
        computer.append(Deel_Card())
    print(f"Your cards: {player}, current score: {Card_Sum(player)}")
    print(f"Computer's first card: {computer[0]}")

    player_score, computer_score = Card_Sum(player), Card_Sum(computer)

    game_going = True
    while game_going:

        user_input = input("Type 'y' to get another card, type 'n' to pass: ")

        if user_input.lower() == "y":
            player.append(Deel_Card())
            player_score = Card_Sum(player)
            print(f"Your cards: {player}, current score: {Card_Sum(player)}")
            print(f"Computer's first card: {computer[0]}")
            if Card_Sum(player) > 21:
                if Deal_Ace(player):
                    player_score = Card_Sum(player) - 10
                else:
                    game_going = False
                    End(player, computer, player_score, computer_score)
                    print("You went over. You lose 😭")
                    break
                if player_score > computer_score:
                    End(player, computer, player_score, computer_score)
                    print("You win 😃")
                elif player_score == computer_score:
                    End(player, computer, player_score, computer_score)
                    print("Draw 🙃")
                else:
                    End(player, computer, player_score, computer_score)
                    print("You lose 😤")
        else: 
            computer.append(Deel_Card())
            computer_score = Card_Sum(computer)
            print(f"Your cards: {player}, current score: {Card_Sum(player)}")
            print(f"Computer's first card: {computer[0]}")
            if Card_Sum(computer) > 21:
                if Deal_Ace(computer):
                    computer_score = Card_Sum(computer) - 10
                else:
                    game_going = False
                    End(player, computer, player_score, computer_score)
                    print("Opponent went over. You win 😁")
                    break
                if computer_score > player_score:
                    End(player, computer, player_score, computer_score)
                    print("You lose 😤")
                elif player_score == computer_score:
                    End(player, computer, player_score, computer_score)
                    print("Draw 🙃")
                else:
                    End(player, computer, player_score, computer_score)
                    print("You win 😃")
