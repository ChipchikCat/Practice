import random, sys


HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)
BACKSIDE = "backside"


def main():
    print("""Блэк_джэк
    Правила игры:
    Игрок, который набирает 21 очко, сразу заявляет об этом и забирает из банка свой выигрыш. 
    Если игрок набрал более 21 очка, то он обязан показать свои карты и заплатить долг в банк 
    (за сокрытие перебора игрок платит вдвойне). Банкир последним заявляет на что он идет 
    и после чего все игроки открывают свои карты.""")

    money = 5000
    while True:
        if money <= 0:
            print("Ты проиграл!")
            print("Хорошо, что ты не играл на реальные деньги.")
            print("Спасибо за игру.")
            sys.exit()

        print("Деньги:", money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Ставка:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Ставка увеличена до {bet}")
                print("Ставка:", bet)
            
            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"Вы 'drew' a {rank} {suit}")
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue
            
            if move in ("S", "D"):
                break
        
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Ход Дилера...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Нажмите Enter для продолжения...")
                print("\n\n")

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print(f"Дилеры обанкротились! Вы выиграли {bet}")
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("Вы проиграли!")
            money -= bet
        elif playerValue > dealerValue:
            print(f"Вы виграли {bet}")
            money += bet
        elif playerValue == dealerValue:
            print("Ничья, ставка возвращается к вам.")

        input("Нажмите Enter для продолжения...")
        print("\n\n")


def getBet(maxBet):
    while True:
        print(f"Сколько вы ставите (1-{maxBet}, или пас )")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Спасибо за игру!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("Дилер:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("Дилер: ???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print("Игрок:", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            rank, suit = card
            rows[1] += (f"|{rank.ljust(2)} |")
            rows[2] += (f"| {suit} |")
            rows[3] += (f"|_{rank.rjust(2, '_')} |")

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ["(H)it", "(S)tand"]
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePromt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()