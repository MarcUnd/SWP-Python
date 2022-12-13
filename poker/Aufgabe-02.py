from random import randrange

#high Card, double, ..., royal flush
results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
realProbability = [0.501177, 0.4222569, 0.047539, 0.0221128, 0.003925, 0.001965, 0.001441, 0.00024, 0.000014, 0.000002]
posHands = ['High Card', 'Pair', 'Two pair', 'Three of a kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']

def getCardList(couCard):
    cardList = [i for i in range(52)]
    return cardList
        
def getHand(couCard):
    deck = getCardList(couCard)
    for i in range(5):
        g = randrange(couCard)
        deck[g], deck[(couCard - 1) - i] = deck[(couCard - 1) - i], deck[g]
    return deck[-5:]

def checkHands(cardHand):
    #get colour (0-3)
    colourArr = [x // 13 for x in cardHand]
    #get value (0=2, 2=3, ..., 12=A)
    valueArr = [x % 13 for x in cardHand]
    #print("Farben: ",colourArr)
    #print("Werte: ",valueArr)
    frequent = max(valueArr, key=valueArr.count)
    couFrequent = valueArr.count(frequent)
    valueArr.sort()
    #print("Anzahl Gleicher Karten: ",couFrequent)
        
    match couFrequent:
        case 1:
            if 5 == colourArr.count(colourArr[0]):
                if valueArr[4] - 4 == valueArr[0]:
                    if valueArr[4] == 12:
                        #print("Royal Flush")
                        results[9] += 1
                        return
                    #print("Straight Flush")
                    results[8] += 1
                    return
                results[5] += 1
                #print("Flush")
            elif (valueArr[4] - 4 == valueArr[0]):
                results[4] += 1
                #print("Straight")
            else:
                results[0] += 1
                #print("high Card")
            return
        case 2:
            if len(set(valueArr)) == 3:
                results[2] += 1
                #print("two pair")
                return
            results[1] += 1
            #print("pair")
            return
        case 3:
            if len(set(valueArr)) == 2:
                results[6] += 1
                #print("full house")
                return
            results[3] += 1
            #print("three of a kind")
            return
        case 4:
            results[7] += 1
            #print("4 of a Kind")
            return 
    pass

def doOften(couIterations):
    for _i in range(couIterations):
        h = getHand(52)
        checkHands(h)
    checkProbability(couIterations)

def checkProbability(couIterations):
    probs = []
    for i in results:
        print(posHands[results.index(i)],": ", i)
        probs.append(i/couIterations)
    print("Berechnete Wahrscheinlichkeiten:\t",probs)
    
def main():
    #hand = getHand(52)
    #checkHands(hand)
    repetitions = input("Anzahl Wiederholungen: ")
    doOften(int(repetitions))
    print("Tatsächliche Wahrscheinlichkeiten:\t",realProbability)

if __name__ == '__main__':
    main()