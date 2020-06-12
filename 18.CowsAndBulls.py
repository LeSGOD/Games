from random import randint

def play_cows_and_bulls():
    randomNumber = randint(1000, 9999)
    elements = [int(i) for i in str(randomNumber)]
    print(randomNumber)

    while True: 
        guess = input("Guess a number: ")
        items = [int(i) for i in str(guess)]
        bulls = 0
        cows = 0     
        for i in range(4):   
            if (items[i] == elements[i]):
                cows += 1
            elif items[i] in elements:
                bulls += 1
        
        if cows == 4:
            break

        print("{} cow, {} bulls".format(cows, bulls))


play_cows_and_bulls()