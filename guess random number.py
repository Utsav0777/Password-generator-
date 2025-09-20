import random
number_to_guess = random.randint(1,100)

attempts = 0
guessed_number = None

print("WELCOME TO 'GUESS NUMBER GAME!'")
while True:
    try:

        guess = int(input("ENTER YOUR GUESS NUMBER BETWEEN 1-100:"))
        attempts +=1

        if guess<number_to_guess:
            print("too low! try again.")
        elif guess>number_to_guess:
            print("too high! try again.")
        else:
            print(f"CONGRATULATION! YOU GUSSED THE NUMBER IN {attempts} ATTEMPTS.")
            break
    except ValueError :
        print("Please enter a vaild number.")

