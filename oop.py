from random import shuffle


class Circle():
    pi = 3.14

    def __init__(self, radius=1) -> None:
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius


myC = Circle(2)
# print(myC.radius)

# Inheritance


class Animal():
    def __init__(self) -> None:
        pass

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print('Eating')


class Dog(Animal):
    def __init__(self) -> None:
        Animal.__init__(self)
        print("Dog")

    def __str__(self) -> str:
        return "dog"

    def __len__(self) -> int:
        return 4

    def __del__(self):
        print("Dog deleted")


SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self) -> None:
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    def __init__(self, cards) -> None:
        self.cards = cards

    def __str__(self) -> str:
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed :{}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Returns True if the player still has cards in their hand
        """
        return len(self.hand.cards) > 0


print("Welcome to the game, let's play")

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# player
comp = Player("computer", Hand(half1))

name = input("what is your name")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("New round")
    print(user.name + " has the count " + str(len(user.hand.cards)))
    print(comp.name+' has the count ' + str(len(comp.hand.cards)))
    print('\n')

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

# ERROR AND EXCEPTION
try:
    f = open('simple.txt', 'w')
    f.write('Test')
except IOError:
    print('error opening simple.txt')
else:
    f.close()
finally:
    print('finally')
