import copy

def full_run(cards):
    cards.sort(key=lambda card: card.rank.value)
    last = cards[0].rank.value
    for i in cards[1:]:
        if i.rank.value != last + 1:
            return False
        else:
            last += 1
    return True


def seq_pairs(cards):
    points = 0
    pair = cards[0].rank.value
    for i in cards[1:]:
        if i.rank.value == pair:
            points += 2
        else:
            return points
    return points


def peg_score(prev_cards, new_card, cur_val):
    info = [0, 0]
    peg_len = len(prev_cards)
    prev_cards.append(new_card)
    combined = copy.deepcopy(prev_cards)
    if cur_val + new_card.value == 15 or cur_val + new_card.value == 31:
        info[0] += 2

    if peg_len >= 3:
        info[0] += seq_pairs(combined[peg_len - 4 :])
    elif peg_len >= 2:
        info[0] += seq_pairs(combined[peg_len - 3 :])
    elif peg_len == 1:
        info[0] += seq_pairs(combined[peg_len - 2 :])
    additive = [] 
    for i in combined[::-1]:
        score = 0
        additive.append(i)
        if len(additive) > 2:
            check = seq_pairs(additive)
            if check > score:
                score = check
    info[0] += score

    
    info[1] = cur_val + new_card.value

    return info

"""def computer_pegging():
    if cur_val == 31:
                input("31 was reached so the pegging will reset to 0.")
                cur_val = 0
                go = False
            if go == True:
                if len(p2_pegging) > 0:
                    if len(prev_cards) > 0:
                        card = pegging(cur_val, prev_cards[len(prev_cards) -1], p2_pegging)
                    else:
                        card = pegging(cur_val, [], p2_pegging)
                    if card == -1:
                        go == False
                        cur_val = 0
                        prev_cards = []
                        last_player = 2
                    else:
                        (p2_score, val) = peg_score(prev_cards, card, cur_val)
                        player2_score[0] += p2_score + 1
                        cur_val = val
                        p2_pegging.remove(card)
                else:
                    last_player = 2
                    cur_val = 0
                    prev_cards = []
                    go = False
            else:
                if len(p2_pegging) > 0:
                    if len(prev_cards) > 0:
                        card = pegging(cur_val, prev_cards[len(prev_cards) - 1], p2_pegging)
                    else:
                        card = pegging(cur_val, [], p2_pegging)
                    if card == -1:
                        go = True
                        p1_peg_score += 1
                        last_player = 2
                    else:
                        (p2_score, val) = peg_score(prev_cards, card, cur_val)
                        player2_score[0] += p2_score
                        cur_val = val
                        p2_pegging.remove(card)
                        last_player = 2
                else:
                    last_player = 2
                    go = False
            if card == -1:
                print(f"The computer couldn't play.")
            else:
                print(f"Computer Played: {card}")
            print(f"The current value is: {cur_val}")"""
            