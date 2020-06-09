from random import shuffle, randint


suits = ["clubs", "spades", "diamonds", "hearts"]
values = ["2", "3", "4", "5", "6", "7", "8",
          "9", "10", "jack", "queen", "king", "ace"]

pSuits = {"clubs": 1, "spades": 2, "diamonds": 3, "hearts": 4}
pValues = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
           "9": 8, "10": 9, "jack": 10, "queen": 11, "king": 12, "ace": 13}


class Card:
    def __init__(self, value, suit):
        self.value = value

        self.suit = suit
        self.pValue = pValues[value]
        self.pSuit = pSuits[suit]

    def comparison(self, card2):
        if self.pValue == card2.pValue:
            if self.pSuit > card2.pSuit:
                return 0
            else:
                return 1

        if self.pValue > card2.pValue:
            return 0
        else:
            return 1

    def __str__(self):
        return self.value + " " + self.suit

    def __repr__(self):
        return self.value + " " + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(values[i], suits[j]))

        shuffle(self.cards)

    def pick_card_from_deck(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

    def __repr__(self):
        return self.name


def drawn_the_card(p1, p1c, p2, p2c):
    return str(p1) + " drew " + str(p1c) + " and " + str(p2) + " drew " + str(p2c)


def game():
    print("Welcome in card game called war")
    p1 = Player("Arthur")
    p2 = Player("Veronica")
    deck = Deck()

    while len(deck.cards) > 0:
        prepare = input("Prepare your self for next fight!\n")
        p1c = deck.pick_card_from_deck()
        p2c = deck.pick_card_from_deck()

        print(str(p1) + " drew " + str(p1c))
        print(str(p2) + " drew " + str(p2c) + "\n")
        result = p1c.comparison(p2c)

        if result == 0:
            print("###########################")
            print("This battle wins " + str(p1))
            print("###########################")
            p1.wins += 1
        else:
            print("###########################")
            print("This battle wins " + str(p2))
            print("###########################")
            p2.wins += 1

    if p1.wins > p2.wins:
        print("This war is over! " + str(p1) + " win!")
        print("score: {} - {}".format(p1.wins, p2.wins))
    elif p1.wins < p2.wins:
        print("This war is over! " + str(p2) + " win!")
        print("score: {} - {}".format(p2.wins, p1.wins))
    elif p1.wins == p2.wins:
        print("war never ends in a draw and a coin toss will determine the victory")
        response = int(
            input("Which side of the coin you choose? (head : 0 or reverse tails: 1) /n"))
        winner = randint(0, 1)
        if response == winner:
            print("This war is over! " + str(p1) + " win!")
        else:
            print("This war is over! " + str(p2) + " win!")


game()
