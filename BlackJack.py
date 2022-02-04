import random
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

final_score = {
    "player": [],
    "computer": []
}


def find_sum(score_list):
    total = 0
    for score in score_list:
        total += score
    return total


def check_aces(user, score):
    if 11 in final_score[user]:
        return True


game_going = True
while game_going:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again.lower() == 'y':
        final_score = {
            "player": [],
            "computer": []
        }
        game_going = True
    elif play_again.lower() == 'n':
        game_going = False

    for x in range(2):
        final_score["player"].append(random.choice(cards))
    final_score["computer"].append(random.choice(cards))

    player_cards = final_score["player"]
    computer_cards = final_score["computer"]
    player_score = find_sum(final_score["player"])
    computer_score = find_sum(final_score["computer"])
    print(f"    Your card: {player_cards}, current score: {player_score}")
    print(f"    Computer's first card: {computer_score}")

    player_choice = True
    while player_choice:
        user_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_card.lower() == 'y':
            final_score["player"].append(random.choice(cards))
            player_cards = final_score["player"]
            player_score = find_sum(final_score["player"])
            print(f"    Your hand: {player_cards}, score: {player_score}")
            print(f"    Computer's hand: {computer_cards}, score: {computer_score}")
            if player_score > 21:
                if check_aces("player", player_score) == True:
                    final_score["player"].append(-10)
                else:
                    print(f"    Your final hand: {player_cards}, final score: {player_score}")
                    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You went over. You lose 😤")
                    player_choice = False

        elif user_card.lower() == 'n':
            computer_cards = final_score["computer"]
            computer_score = find_sum(final_score["computer"])
            above = True
            while above:
                final_score["computer"].append(random.choice(cards))
                computer_score = find_sum(final_score["computer"])
                if computer_score > 17:
                    above = False
            print(f"    Your hand: {player_cards}, score: {player_score}")
            print(f"    Computer's hand: {computer_cards}, score: {computer_score}")
            if computer_score > 21:
                if check_aces("computer", computer_score) == True:
                    final_score["computer"].append(-10)
                else:
                    print(f"    Your final hand: {player_cards}, final score: {player_score}")
                    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("Opponent went over. You win 😁")
                    player_choice = False
            elif player_score > computer_score:
                print(f"    Your final hand: {player_cards}, final score: {player_score}")
                print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Opponent went over. You win 😁")
                player_choice = False
            elif player_score == computer_score:
                print(f"    Your final hand: {player_cards}, final score: {player_score}")
                print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("It's a draw 🙂")
                player_choice = False
            else:
                print(f"    Your final hand: {player_cards}, final score: {player_score}")
                print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You went over. You lose 😤")
                player_choice = False
clear()