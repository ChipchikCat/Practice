import random, sys

JAPANESE_NUMBERS = {1: "ICHI", 2: "NI", 3: "SAN",
                    4: "SHI", 5: "GO", 6: "ROKU"}

print("""В игре используются два стандартных шестигранных кубика, которые дилер
встряхивает в бамбуковой чашке или миске. Затем чашку переворачивают на пол. 
Затем игроки делают ставки на то, будет ли сумма чисел, отображаемых на двух 
кубиках, «Cho» (четным) или «Han» (нечетным). Затем дилер убирает чашку, 
показывая кости. Победители забирают свои деньги.""")

purse = 5000
while True:
    print("У тебя есть", purse, "мон. Сколько ты ставишь? (или ВЫЙТИ?)")
    while True:
        pot = input("> ")
        if pot.upper() == "QUIT":
            print("Спасибо за игру!")
            sys.exit
        elif not pot.isdecimal():
            print("Пожалуйста введите число.")
        elif int(pot) > purse:
            print("У вас недостаточно денег, чтобы сделать эту ставку.")
        else:
            pot = int(pot)
            break
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("Раздающий крутит чашку, и вы слышите стук костей.")
    print("Крупье бьет чашку об пол, все еще накрывая")
    print("кости и просит вашу ставку.")
    print()
    print("CHO (чётное) or HAN (нечётное).")

    while True:
        bet = input("> ").upper()
        if bet != "CHO" and bet != "HAN":
            print("Пожалуйста, введите 'CHO' или 'HAN'.")
            continue
        else:
            break

    print("Дилер поднимает чашку, чтобы показать:")
    print(" ", JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("  ", dice1, "-", dice2)


    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = "CHO"
    else:
        correctBet = "HAN"
    
    playerWon = bet == correctBet

    if playerWon:
        print("Ты выиграл! Ты забираешь", pot, "мон.")
        purse = purse + pot
        print("Дом собирает", pot // 10, "плату.")
        purse = purse - (pot // 10)
    else:
        purse = purse - pot
        print("Ты проиграл!")
    if purse == 0:
        print("У тебя закончились деньги!")
        print("Спасибо за игру!")
        sys.exit()


