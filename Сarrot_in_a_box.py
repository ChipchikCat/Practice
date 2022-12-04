import random

input("Нажмите Enter для начала...")

p1Name = input("Игрок 1, введите своё имя: ")
p2Name = input("Игрок 2, введите своё имя: ")
playerNames = p1Name[:11].center(11) + "   " + p2Name[:11].center(11)

print(""" Здесь две коробки:
    __________     __________
   /        /|    /        /|
  *--------* |   *--------* |
  |  RED   | |   |  GOLD  | |
  |  BOX   | /   |  BOX   | /
  *--------*     *--------*  """)

print()
print(playerNames)
print()
print(p1Name + ", перед вами КРАСНАЯ коробка.")
print(p2Name + ", перед вами ЗОЛОТАЯ коробка.")
print()
print(p1Name + ", ты заглядываешь в свою коробку")
print(p2Name.upper() + ", закрой свои глаза и не подсматривай!")
input("Когда " + p2Name + " закроет глаза, нажмите Enter...  ")
print()

print(p1Name + " вот что внутри вашей коробки:")

if random.randint(1, 2) == 1:
    carrotInFirstbox = True
else:
    carrotInFirstbox = False

if carrotInFirstbox:
    print("""
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|     __________
  /    ||   /|    /        /|
 *---------* |   *--------* |
 |   RED   | |   |  GOLD  | |
 |   BOX   | /   |  BOX   | /
 *---------*     *--------* 
    (морковка!)""")
    print(playerNames)
else:
    print("""
                                    
  _________
 |         |
 |         |
 |_________|     __________
 /        /|    /        /|
*--------* |   *-------- *|
|   RED  | |   |  GOLD  | |
|   BOX  | /   |  BOX   | /
*--------*     *--------*
     (нет морковки!)""")
    print(playerNames)

input("Нажмите Enter для продолжения...")

print("\n" * 100)
print(p1Name + ", скажи " + p2Name + " открыть глаза.")
input("Нажмите Enter что бы продолжить...")

print()
print(p1Name + ",скажите одно из следующих предложений, чтобы " + p2Name + ".")
print("  1) В моей коробке есть морковь.")
print("  2) В моей коробке нет моркови.")
print()
input("Нажмите нажмите Enter, чтобы продолжить...")

print()
print(p2Name + ", ты хочешь поменяться коробками с " + p1Name + "? ДА/НЕТ")
while True:
    response = input("> ").upper()
    if not (response.startswith("ДА") or response.startswith("НЕТ")):
        print(p2Name + " , пожалуйста введите 'ДА' или 'НЕТ'.")
    else:
        break

firstBox = "RED "
secondBox = "GOLD"

if response.startswith("ДА"):
    carrotInFirstbox = not carrotInFirstbox
    firstBox, secondBox = secondBox, firstBox

print(f"""Здесь две коробки:
  __________      ___________
 /         /|    /          /|
*----------*|    *----------*|
|{firstBox}||   |{secondBox}||
|   BOX    |/   | BOX       |/
*----------*    *-----------*  """)

print(playerNames)

input("Нажмите Enter, чтобы выявить победителя...")
print()

if carrotInFirstbox:
    print(f"""
     __________     _____VV_____
    |          |   |     VV     |
    |          |   |     VV     |
    |__________|   |_____||_____|
   /          /|   /     ||    /|
   *----------*|   *-----------*|
   |{firstBox}||   |{secondBox}||
   |   BOX    |/   |   BOX     |/
   *----------*    *-----------* """)

print(playerNames)

if carrotInFirstbox:
    print(p1Name + " Победитель!")
else:
    print(p2Name + " Победитель!")
print("Спасибо за игру!")

