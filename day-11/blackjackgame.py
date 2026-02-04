cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

cards_drawn = []
total_score = 0
computer_hand = []

game =  True
while game:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
    if start == "y":
        print(r"""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """)

        random.shuffle(cards)
        cards_drawn += cards[0], cards[1]
        computer_hand = [cards[2]]
        total_computer_hand=0
        total_score = cards_drawn[0] + cards_drawn[1]
        print(f"Your cards: {cards_drawn}, current score: {total_score}\nComputer's first card: {computer_hand}")
        continue_game = True
        while continue_game:
            process = input("Type 'y' to get another card , type 'n' to pass:  ")
            if process == "y":
                continue_game = True
                cards_drawn.append(cards[3])
                total_score += cards_drawn[2]
                print(f"Your cards: {cards_drawn}, current score {total_score}\nComputer's first card: {computer_hand}")
                if total_score > 21:
                    print(
                        f"Your final hard: {cards_drawn}, final score: {total_score}\nComputer's final card: {computer_hand}, final score: {computer_hand}")
                    print("You went over. You lose 😭")
                    continue_game = False
            elif process == "n":
                if  17 <= total_computer_hand > 21:
                    random_number = random.randint(1, 10)
                    computer_hand = [cards[2], cards[random_number]]
                    total_computer_hand += computer_hand[0] + computer_hand[1]


                print(
                    f"Your final hand:  {cards_drawn} , final score: {total_score}\nComputer's final hand: {computer_hand}, final score: {total_computer_hand}")
                if total_computer_hand > total_score:
                    print("You Lose")
                elif total_computer_hand < total_score:
                    print("You Win")
                elif total_computer_hand == total_score:
                    print("It's a draw")
                continue_game = False







    else:
        print("Fuck off")
        game = False
