from dataclasses import dataclass
@dataclass
class card():
    value : int = 0
    suit : str = ""

ace_of_d = card()
ace_of_d.suit="diamonds"
ace_of_d.value=1

def suit_value(card):
    suits=["spades", "clubs", "hearts", "diamonds"]
    for i in range(len(suits)):
        if (card.suit==suits[i]):
            return i

if (suit_value(ace_of_d)>2):
    print("3")

        
