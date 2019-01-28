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

class Unprintable_Card(Card):
    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """Карта , которую можно положить лицом или рубашкой вверх."""
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card,self).__init__(rank,suit)
#функция super()  вызывает метод инит из класса КАРД(надкласса = базовый класс = родительский)
#вторая часть команды вызывает инит базвого класса с аргументами , которые будут переданны
#в параметры РЭНК и СЬЮТ
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card,self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

card1 = Card("A","c")
card2 = Unprintable_Card("A","d")
card3 = Positionable_Card("A","h")
print("Объект Сard: ")
print(card1)
print("Объект Unprintable_Card: ")
print(card2)
print("Объект Positionable_Card: ")
print(card3)
card3.flip()
print("Объект Positionable_Card после переворота: ")
print(card3)

