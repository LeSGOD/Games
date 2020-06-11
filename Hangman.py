def hangman(word):

    print("Welcome in my game, called Hangman! Good luck & Have fun :)")
    print("If you want to end the game type \"q\" \n")

    # Hangman stages
    stages = [
        "_______",
        "|  |   ",
        "|  0   ",
        "| /|\  ",
        "| / \  ",
        "|      "
    ]

    "sets the word length to determine the winner"
    leng = len(word)

    "Creating visual board for user"
    board = ("__ ") * leng

    "creating list which will be use to replace guessed letters "
    x = board.split()

    """
    winPoints are responsible for counting how many times user guessed the letter. If winPoints == leng then user will win the game
    losePoints are responsible for tracking the hangman path. Are used for printing the appropriate amount of stages

    """

    winPoints = 0
    losePoints = 0

    while True:

        r = str(input(" \n Guess the letter: "))

        if r == "q":
            break

        if winPoints == leng:
            print("My congratulations you won!")
            break

        if r not in word:
            losePoints += 1
            print("This letter is not in this word! ")

            if losePoints == 6:
                print("You lost! Good try")
                for i in range(losePoints):
                    print(stages[i])
                break

        while r in word:
            answear = list(word)

            winPoints += 1
            number = word.index(r)
            answear[number] = "$"

            word = ("").join(answear)

            x[number] = r
            board = (" ").join(x)

        print(board + ("\n"))

        for i in range(losePoints):
            print(stages[i])


hangman("alibaba")
