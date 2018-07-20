import random

class Die(object):
    def __init__(self,sides):
        self.sides = sides
        
    def roll(self):
        return random.randint(1,self.sides)

class Deck(object):
    def shuffle(self):
        suits = ["spades","Hearts","Clubs","Diamonds"]
        ranks = ["1","2","3""4","5","6","7","8","9","10","jack","queen","king"]
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank+ " of " + suit)
        
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()
    
class Greeter(object):
    
    def __init__(self,name):
        self.name = name
    
    def hello(self):
        print("Hello " + self.name)
    
    def Goodbye(self):
        print("Goodbye " + self.name)

g = Greeter("Rahul")

g.hello()
g.Goodbye()

d = Die(8)
print(d.roll())
print(d.roll())

deck = Deck()
deck.shuffle()
print(deck.deal())
print(deck.deal())

# copy of string in python
string = "Rahul"
string2 = string[:]
print(string2)