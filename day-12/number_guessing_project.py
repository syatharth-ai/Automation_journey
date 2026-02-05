import random



def guess_number(number_0, number_1):
    if number_0 > number_1:
        print("Too high!\nGuess again.")
    elif number_0 < number_1:
        print("Too low!\nGuess again.")
    elif number_0 == number_1:
        print("You guessed the number!\n You win!")



EASY = 10
HARD = 5
print("""      o__ __o                                                         o       o                                                                     o                                  
     /v     v\                                                       <|>     <|>                                                                   <|>                                 
    />       <\                                                      < >     / >                                                                   / >                                 
  o/                o       o     o__  __o       __o__    __o__       |      \o__ __o      o__  __o       \o__ __o    o       o   \o__ __o__ __o   \o__ __o       o__  __o   \o__ __o  
 <|       _\__o__  <|>     <|>   /v      |>     />  \    />  \        o__/_   |     v\    /v      |>       |     |>  <|>     <|>   |     |     |>   |     v\     /v      |>   |     |> 
  \\          |    < >     < >  />      //      \o       \o           |      / \     <\  />      //       / \   / \  < >     < >  / \   / \   / \  / \     <\   />      //   / \   < > 
    \         /     |       |   \o    o/         v\       v\          |      \o/     o/  \o    o/         \o/   \o/   |       |   \o/   \o/   \o/  \o/      /   \o    o/     \o/       
     o       o      o       o    v\  /v __o       <\       <\         o       |     <|    v\  /v __o       |     |    o       o    |     |     |    |      o     v\  /v __o   |        
     <\__ __/>      <\__ __/>     <\/> __/>  _\o__</  _\o__</         <\__   / \    / \    <\/> __/>      / \   / \   <\__ __/>   / \   / \   / \  / \  __/>      <\/> __/>  / \       
                                                                                                                                                                                       
                                                                                                                                                                                       
                                                                                                                                                                                       """)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
game_level = input("Choose a difficulty. Type 'easy' or 'hard':   ").lower()
guess_true = True
number = random.randint(1, 100)
if game_level == "easy":
    while guess_true:
        print(f"You have {EASY} attempts remaining to guess the number.")
        guess = int(input("Make a guess:  "))
        EASY -= 1
        guess_number(guess, number)
        if  guess == number:
            guess_true = False
        if EASY == 0:
            guess_true = False
            print("You are out of attempts\n You lose!")

else:
    while guess_true:
        print(f"You have {HARD} attempts remaining to guess the number.")
        guess = int(input("Make a guess:  "))
        HARD -= 1
        guess_number(guess, number)
        if guess == number:
            guess_true = False
        if HARD == 0:
            guess_true = False
            print("You are out of attempts\n You lose!")






