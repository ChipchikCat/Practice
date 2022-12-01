import random

NUM_DIGITS = 2
MAX_GUESSES = 20

def main():
    print("""Бейглз, дедуктивная логическая игра.
    Постарайтесь угадать задуманное число,где:
    'Pico'   'Одна цифра правильная, но в неправильном месте'
    'Fermi'  'Одна цифра правильная и в правильном положении'
    'Bagels' 'Правильных цифр нет вообще'""") 

    while True:
        secretNum = getSecretNum()
        print("Я придумал число ")
        print(f"У вас есть {MAX_GUESSES} количество попыток чтобы отгадать задуманное число.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Попытка #{numGuesses}:")
                guess = input(" > ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("У вас закончились попытки")
                print(f"Ответ был {secretNum}")

        print("Хотите ли сыграть еще раз? (да или нет)")
        if not input(">").lower().startswith("да"):
            break
    print("Спасибо за игру")


def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "Вы угадали!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == "__main__":
    main()
