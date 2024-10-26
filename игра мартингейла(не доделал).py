import random




HEADS = 'heads'
TAILS = 'tails'
COIN_FLIPPER = [HEADS,TAILS]


def flip_coin():
    return random.choice(COIN_FLIPPER)


def play_martingale(starting_funds,min_bet,max_bet):
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet


    while current_bet > 0:
        print('==========')
        steps_to_loose +=1
        current_funds -= current_bet
        print(f'current_funds =',current_funds)
        flip_coin_value = flip_coin()


        if flip_coin_value == HEADS:
            win = current_bet * 2
            current_funds += win
            current_bet = min_bet
        else:
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return steps_to_loose


print(play_martingale(10000,1,1000))
