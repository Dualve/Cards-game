class Card(object):
    """Одна игральная карта"""

    Ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    Suits = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """Рука: набор карт на руках у одного игрока."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        self.cards = []
        for suit in Card.Suits:
            for rank in Card.Ranks:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Карты в колоде закончились.")


deck1 = Deck()
print("Создана новвая колода.")
deck1.populate()
print("Вот эта колода: ")
print(deck1)
print("Перемешав колоду, получим это: ")
deck1.shuffle()
print(deck1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand,your_hand]
deck1.deal(hands,per_hand = 5)
print("Сейчас на руках у игроков по 5 карт: ")
print(my_hand)
print(your_hand)
deck1.clear()
