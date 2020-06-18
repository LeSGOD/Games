from random import shuffle


suits = {"clubs": 1, "spades": 2, "diamonds": 3, "hearts": 4}
values = {"9": 0, "jack": 2, "queen": 3, "king": 4, "10": 10, "ace": 11}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.cardValue = values[value]
        self.cardSuit = suits[suit]

    def comparison(self, card2):
        if self.cardValue == card2.cardValue:
            if self.cardSuit > card2.cardSuit:
                return self
            else:
                return card2

        if self.cardValue > card2.cardValue:
            return self
        else:
            return card2

    def __str__(self):
        return self.value + " " + self.suit

    def __repr__(self):
        return self.value + " " + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        valuesItems = values.items()
        suitsItems = suits.items()
        for value in valuesItems:
            for suit in suitsItems:
                self.cards.append(Card(value[0], suit[0]))

        shuffle(self.cards)

    def pick_card_from_deck(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.deck = []
        self.name = name
        self.points = 0
        self.round = 0
        self.auction = 0

    def get_points(self):
        if self.auction > 0:
            if self.round > self.auction:
                self.points += self.auction
        else:
            self.points += self.round

    def __repr__(self):
        return "{} have {} in total".format(self.name, self.points)

    def players_cards(self):
        return "{} ".format(self.name) + str(self.deck)


def count_points_on_hand(deck):
    cardSum = 0
    if "king clubs" in deck and "queen clubs" in deck:
        cardSum += 40
    if "king spades" in deck and "queen spades" in deck:
        cardSum += 60
    if "king diamonds" in deck and "queen diamonds" in deck:
        cardSum += 80
    if "king hearts" in deck and "queen hearts" in deck:
        cardSum += 100

    deck = " ".join(deck)
    deck = deck.split(" ")
    items = values.items()

    valueItems = []
    for item in items:
        valueItems.append(item[0])

    cardsValues = []

    for x in deck:
        if x in valueItems:
            cardsValues.append(x)

    for x in cardsValues:
        cardSum += values[x]

    return cardSum


def distribution():
    deck = Deck()
    musikP = []
    musikL = []
    p1cards = []
    p2cards = []

    for _ in range(2):
        musikP.append(str(deck.cards.pop()))
    for _ in range(2):
        musikL.append(str(deck.cards.pop()))
    for _ in range(10):
        p1cards.append(str(deck.cards.pop()))
    for _ in range(10):
        p2cards.append(str(deck.cards.pop()))

    return (musikP, musikL, p1cards, p2cards)


def sort_cards_in_hand(deck):
    hearts = get_cards_suit("hearts", deck)
    diamonds = get_cards_suit("diamonds", deck)
    spades = get_cards_suit("spades", deck)
    clubs = get_cards_suit("clubs", deck)

    h = sort_suits(hearts)
    d = sort_suits(diamonds)
    s = sort_suits(spades)
    c = sort_suits(clubs)

    general = add_cards_to_general(c, s, d, h)

    general.reverse()
    return general


def sort_suits(suit):
    items = values.items()
    general = []
    for item in items:
        for i in suit:
            if item[0] in i:
                general.append(i)
    return general


def get_cards_suit(suit, deck):
    general = []
    for x in deck:
        if suit in x:
            general.append(x)
    return general


def add_cards_to_general(deck1, deck2, deck3, deck4):
    general = []
    for x in deck1:
        general.append(x)
    for x in deck2:
        general.append(x)
    for x in deck3:
        general.append(x)
    for x in deck4:
        general.append(x)
    return general


def game_prepare():
    distrib = distribution()
    musikL = distrib[0]
    musikP = distrib[1]
    player1Deck = distrib[2]
    player2Deck = distrib[3]

    player1Deck = sort_cards_in_hand(player1Deck)
    player2Deck = sort_cards_in_hand(player2Deck)
    musikL = sort_cards_in_hand(musikL)
    musikP = sort_cards_in_hand(musikP)

    return(musikL, musikP, player1Deck, player2Deck)


def auction(name1, name2):
    auction = 100
    print(str(name1 + " starting auction! 100"))
    while True:
        p1 = 0
        p2 = 0
        global response2
        response2 = int(
            input(str(name2 + " auction level {}: ".format(auction))))
        if response2 <= auction:
            p1 += 1
            break
        else:
            auction = response2
        global response1
        response1 = int(
            input(str(name1 + " auction level {}: ".format(auction))))
        if response1 <= auction:
            p2 += 1
            break
        else:
            auction = response1

    if p1 == 1:
        print("{} wins!".format(name1))
        response1 = auction
        response2 = 0
        return 1
    else:
        print("{} wins!".format(name2))
        response1 = 0
        response2 = auction
        return 0


def game():

    p1 = Player("Artur")
    p2 = Player("Irek")
    p1.auction = 0
    p2.auction = 0
    while p1.points < 1000 or p2.points < 1000:
        gp = game_prepare()

        musikL = gp[0]
        musikP = gp[1]
        p1.deck = gp[2]
        p2.deck = gp[3]

        print(p1.players_cards())
        print(p2.players_cards())
        print("\n")
        print("{} have {} points in your hand".format(p1.name,
                                                      count_points_on_hand(p1.deck)))
        print("{} have {} points in your hand".format(p2.name,
                                                      count_points_on_hand(p2.deck)))
        print("\n")

        X = auction("Artur", "Irek")

        if X == 1:
            response = input("Which musik you choose? (p/l)")
            if response == "p":
                p1.deck += musikP

            else:
                p1.deck += musikL

        if X == 0:
            response = input("Which musik you choose? (p/l)")
            if response == "p":
                p2.deck += musikP

            else:
                p2.deck += musikL

        print("\n")
        print(p1.players_cards())
        print(p2.players_cards())
        print("\n")
        print("{} have {} points in your hand".format(p1.name,
                                                      count_points_on_hand(p1.deck)))
        print("{} have {} points in your hand".format(p2.name,
                                                      count_points_on_hand(p2.deck)))
        print("\n")

        if len(p1.deck) > len(p2.deck):
            auctionPoints = int(input("How much you will win in this round: "))
            p1.auction = auctionPoints
            response1 = int(input("First card to return: "))
            response2 = int(input("First card to return: "))
            r1 = p1.deck.pop(response1)
            r2 = p1.deck.pop(response2)
        else:
            auctionPoints = int(input("How much you will win in this round: "))
            p2.auction = auctionPoints
            response1 = int(input("First card to return: "))
            response2 = int(input("First card to return: "))
            r1 = p2.deck.pop(response1)
            r2 = p2.deck.pop(response2)
        if len(musikL) > len(musikP):
            musikL.clear()
            musikL.append(r1)
            musikL.append(r2)
            print("returned cards" + str(musikL))

        else:
            musikP.clear()
            musikP.append(r1)
            musikP.append(r2)
            print("returned cards" + str(musikP))

        p1.auction = response1
        p2.auction = response2

        p1d = []
        p2d = []
        while len(p1.deck) > 0 and len(p2.deck) > 0:
            print("\n")
            print(p1.players_cards())
            print(p2.players_cards())
            print("\n")

            response1 = int(input("{} choose card: ".format(p1.name)))
            response2 = int(input("{} choose card: ".format(p2.name)))

            p1p = p1.deck.pop(response1)
            p2p = p2.deck.pop(response2)

            p1pp = p1p.split(" ")
            p2pp = p2p.split(" ")

            cardp1 = Card(p1pp[0], p1pp[1])
            cardp2 = Card(p2pp[0], p2pp[1])

            result = cardp1.comparison(cardp2)

            print("{} throw {} and {} throw {}".format(
                p1.name, p1p, p2.name, p2p))
            print("This battle wins {}".format(result))
            print("\n")

            if result == cardp1:
                p1d.append(p1p)
                p1d.append(p2p)
            else:
                p2d.append(p1p)
                p2d.append(p2p)

        p1.round = count_points_on_hand(p1d)
        p2.round = count_points_on_hand(p2d)

        p1.get_points()
        print(p1)

        p2.get_points()
        print(p2)

    if p1.points > p2.points:
        print("{} is a winner!".format(p1.name))
    else:
        print("{} is a winner!".format(p2.name))


game()
