import structs

def score(hand_cards, starter):
    total = 0
    for i in range(4):
        if hand_cards[i].face == structs.Face.JACK and hand_cards[i].suit == starter.suit:
            total += 1



def count15s(cards, sum):
    if sum == 15:
        return 2
    elif len(cards) == 0:
        return 0
    else:
        return count15s(cards[1:], sum) + count15s(cards[1:], sum + cards[0])

def runs(cards):

def maxrun(cards, length, prev):
    if prev == -1:
        return max(maxrun(cards[1:], 1, cards[0]), maxrun(cards[0] + cards[2:], 1, cards[1]), maxrun(cards[:2] + cards[3:], 1, cards[2]), maxrun(cards[:3] + cards[4:], 1, cards[3]), maxrun(cards[:4] + cards[5], 1, cards[4]), maxrun(cards[:5], 1, cards[5]))
    elif len(cards) == 0:
        return length
    else:
        for i in cards:
            if i == prev + 1:
                maxrun()
    