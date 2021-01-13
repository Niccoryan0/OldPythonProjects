import random
options = ['rock', 'paper', 'scissors']
while True:
    choice = input('Rock, paper, or scissors?: ').lower()
    comp = random.choice(options)
    print(f"Your opponent chose: {comp.title()}")
    if choice == 'rock' or choice == 'r':
        if comp == 'rock':
            print("It's a tie!")
        elif comp == 'scissors':
            print("You won!")
        elif comp == 'paper':
            print("You lost!")
        else:
            print("Error")
    if choice == 'scissors' or choice == 's':
        if comp == 'scissors':
            print("It's a tie!")
        elif comp == 'paper':
            print("You won!")
        elif comp == 'rock':
            print("You lost!")
        else:
            print("Error")
    if choice == 'paper' or choice == 'p':
        if comp == 'paper':
            print("It's a tie!")
        elif comp == 'rock':
            print("You won!")
        elif comp == 'scissors':
            print("You lost!")
        else:
            print("Error")
    while True:
        again = input("Would you like to play again? y/n: ").lower()
        if again in ('y', 'n'):
            break
        else:
            print("Invalid input")
    if again == 'y':
        continue
    elif again == 'n':
        print("Thanks for playing!")
        break
        