from random import randint


def dice_generator():
    dice1 = randint(1, 7)
    dice2 = randint(1, 7)
    return dice1, dice2


def game_on():
    banker_wins = False
    dice1, dice2 = dice_generator()
    print('The dices are %d and %d' % (dice1, dice2))
    if dice1 + dice2 == 7 or dice1 + dice2 == 11:
        banker_wins = False
    elif dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
        banker_wins = True
    else:
        dice11, dice22 = dice_generator()
        print('Player2: the dices are %d and %d' % (dice11, dice22))
        if dice11 + dice22 == 7:
            banker_wins = True
        elif dice1 == dice11 and dice2 == dice22:
            banker_wins = False
        else:
            game_on()
    return banker_wins


banker_wins = game_on()
if banker_wins:
    print('Banker wins')
else:
    print('Player wins')
