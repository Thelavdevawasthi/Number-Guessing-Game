# I am thinking of a number. Try to guess the number I am thinking: 24 
# Too Low!!! Guess Again: 50
# Too High!!! Guess Again: 42
# Correct you did it. Do you want to play again? [Yes, No]
import random

def guessnumber():
    return random.randint(1,10)


play = True

user_num = int(input("I am thinking of a number. Try to guess the number I am thinking: "))
while play:
    random_num = guessnumber()
    if user_num > random_num:
        print("Too High!!!")
    elif user_num < random_num:
        print("Too Low!!!")
    elif user_num == random_num:
        print("You guess it correct.")
    
    message = input("Do you want to play again?[Yes/No]: ")
    if message.upper() == "YES":
        user_num = int(input(" Guess Again:"))
    else:
        play = False

print("Thanks for playing.")
