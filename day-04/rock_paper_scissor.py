rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

users_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors.\n"))
if users_choice == 0 :
    print(rock)
elif users_choice == 1 :
    print(paper)
elif users_choice == 2 :
    print(scissors)
else:
    print("Choose a valid choice.")

import random

print("Computer Chose\n")
random_index = random.randint(0,2)
if random_index == 0:
    print(rock)
elif random_index == 1:
    print(paper)
else:
    print(scissors)


if users_choice == random_index:
    print ("It's a draw")
elif users_choice == 0 and random_index == 1:
    print("You lose ")
elif users_choice == 1 and random_index == 2:
    print("You lose ")
elif users_choice == 2 and random_index == 0:
    print('You lose')
else:
    print("You win")





