
import random
from game_data import data
from art import logo,vs

# choosing random celebrities for comparison

# comparison of followers

winning = True
greater_followers = 0
score = 0
winning_a = 0

while winning:
    random.shuffle(data)
    choice_a = data[0]
    choice_b = data[1]
    print(logo)

    print(f"Compare A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a['country']}")
    print(vs)
    print(f"Compare B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b['country']}")


    ans = input("Who has more followers? Type 'A' or 'B':    ")
    followers_1 = choice_a['follower_count']
    followers_2 = choice_b['follower_count']
    if followers_1 > followers_2:
        greater_followers = followers_1
    elif followers_1 < followers_2:
        greater_followers = followers_2

    if ans == "A" and greater_followers == followers_1:
        score += 1
        print(f"You're right!,Current score: {score}")
        winning_a = choice_a

    elif ans == "B" and greater_followers == followers_2:
        score += 1
        print(f"You're right!,Current score: {score}")
        winning_a = choice_b

    else:
        print(f"Sorry,that's wrong. Final score: {score}")
        winning = False
