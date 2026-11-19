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
    print("")

def suit_value(card):
    suits=["spades", "clubs", "hearts", "diamonds"]
    for i in range(len(suits)):
        if (card.suit==suits[i]):
            return i

def sort_cards(cards, total_swaps):
    for i in range(len(cards)-1):
        j=0
        switched=True
        while(j<=i and switched):
            print("Comparing cards " + str(cards[i+1-j].value) + " of " + cards[i+1-j].suit + " and " + str(cards[i-j].value) + " of " + cards[i-j].suit)
            current_card=cards[i+1-j]
            previous_card=cards[i-j]
            if (current_card.value<previous_card.value):
                cards[i-j]=current_card
                cards[i+1-j]=previous_card
                print("Swapping")
                j+=1
                total_swaps+=1
                display_cards(cards)

            elif (current_card.value==previous_card.value):
                if (suit_value(current_card)<suit_value(previous_card)):
                    cards[i-j]=current_card
                    cards[i+1-j]=previous_card
                    print("Swapping")
                j+=1
                total_swaps+=1
                display_cards(cards)
            else:
                print("No swap")
                switched=False  

            print("")
    return cards, total_swaps
        
# main program
cards = [card() for index in range(10)]
allcards = [card() for index in range(52)]

allcards = build_deck()
cards = draw_cards(allcards)
display_cards(cards)

total_swaps=0

cards, total_swaps = sort_cards(cards, total_swaps)
display_cards(cards)
print(str(total_swaps) + " swaps were required to sort the cards.")