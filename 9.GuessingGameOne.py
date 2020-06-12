from random import randint


def try_to_guess_number():
    print("Welcome in my game! Try to guess my hidden number")
    randomNumber = randint(1, 9)
    shots = 1
    while True:
        guess = int(input("Your guess: "))
        if guess == randomNumber:
            print("You guessed it right!")
            print("You had " + str(shots) + " shots")
            break
        elif guess > randomNumber:
            print("Your number is too high")
            shots += 1
            continue
        elif guess < randomNumber:
            print("Your number is too low")
            shots += 1
            continue


try_to_guess_number()
