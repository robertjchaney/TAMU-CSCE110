baseDeck = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A"]
finalDeck = []
def createSuit (deck, suit):
    """TAKES BASEDECK INPUT AND RETURNS SUITED DECK"""
    for face in range (len(baseDeck)):
        temp = deck[face] + suit
        finalDeck.append(temp)

print(finalDeck)
createSuit(baseDeck, "♠")