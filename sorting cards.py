from dataclasses import dataclass
import random
@dataclass
class card():
    suit : str = ''
    value : int = 0

def build_deck():
    # setup all cards and return ten of them
    thesecards = [card() for index in range(52)]
    suits = ['hearts', 'clubs','diamonds','spades']
    count = 0
    for s in range(0,4):
        for index in range(1,14):
            thesecards[count].suit = suits[s]
            thesecards[count].value = index
            count += 1
    return thesecards

def draw_cards(thesecards):
    dealtcards = [card() for index in range(10)]
    selectednums = []
    # pick 10 to return
    for index in range(10):
        selectednum = random.randint(0,51)
        while selectednum in selectednums:
            selectednum = random.randint(0,51)
        selectednums.append(selectednum)
        dealtcards[index] = thesecards[selectednum]
    return dealtcards

def display_cards(cardarray):
    for index in range(len(cardarray)):
        output = cardarray[index].suit
        output = output + " : " + str(cardarray[index].value)
        print(output)

def sort_cards(cards):
    for i in range(len(cards)-1):
        j=0
        switched=True
        while(j<=i and switched):
            current_card=cards[i+1-j]
            previous_card=cards[i-j]
            if (current_card.value<previous_card.value):
                cards[i-j]=current_card
                cards[i+1-j]=previous_card
                j+=1

            elif (current_card.value==previous_card.value):
                if (current_card.suit=="spades"):
                    current_suit=0
                elif (current_card.suit=="clubs"):
                    current_suit=1
                elif (current_card.suit=="hearts"):
                    current_suit=2
                else:
                    current_suit=3

                if (previous_card.suit=="spades"):
                    previous_suit=0
                elif (previous_card.suit=="clubs"):
                    previous_suit=1
                elif (previous_card.suit=="hearts"):
                    previous_suit=2
                else:
                    previous_suit=3

                if (current_suit<previous_suit):
                    cards[i-j]=current_card
                    cards[i+1-j]=previous_card
                j+=1
            else:
                switched=False   
    return cards 
        
# main program
cards = [card() for index in range(10)]
allcards = [card() for index in range(52)]
allcards = build_deck()
cards = draw_cards(allcards)
cards = sort_cards(cards)
display_cards(cards)