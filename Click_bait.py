import random

OBJECT_PRONOUNS = ["Her", "Him", "Them"]
POSSESIVE_PRONOUNS = ["Her", "His", "Their"]
PERSONAL_PRONOUNS = ["She", "He", "They"]
CITY = ["Тольятти", "Самара", "Москва", "Челябинск", "Чита",
          "Санкт-Петербург", "Новокузнецк", "Новосибирск", "Оренбург", "Томск"]
NOUNS = ["Атлеты", "Клоун", "Рыцарь", "Фокус", "Доктор", "Родитель",
         "Кот", "Собака", "Курица", "Робот", "Игры", "Авокадо",
         "Пластик","Танцы", "Айфон"]
PLACES = ["Дом", "Чердак", "Банк", "Школа", "Подвал",
          "Работа", "Ветклиника", "Бункер"]
WHEN = ["Скоро", "В этом году", "Позже", "СЕЙЧАС", "На следующей недели"]


def main():
    print("Кликбейт генератор.")
    print()
    
    print("Наш сайт должен заставить людей смотреть рекламу!")
    while True:
        print("Введите количество кликбейтных заголовков для генерации:")
        response = input("> ")
        if not response.isdecimal():
            print("Введите номер.")
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()

    website = random.choice(["wobsite", "blag", "Facebuuk", "Googles", 
                            "Facesbook", "Tweedie", "Pastagram"])
    when = random.choice(WHEN).lower()
    print("Опубликуйте это на нашем", website, when, "или вас уволят!")


def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f" Миллениалы убивают {noun} отрасль."


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    return f" Без этого {noun}, {pluralNoun} Может убить тебя {when}"


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(CITY)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f" Большие Компании ненавидят {pronoun}! Посмотрите, как это {state} {noun1} Изобрел дешевле {noun2}."


def generateYouWontBelieveHeadline():
    state = random.choice(CITY)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f" Вы не поверите, что это {state} {noun} найдено в {pronoun} {place}."


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + "s"
    pluralNoun2 = random.choice(NOUNS) + "s"
    return f" О чем {pluralNoun1} вы не должны знать {pluralNoun2}."


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(CITY)
    return f" {number} Идеи подарков для вашего {noun} от {state}"


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluranNoun = random.choice(NOUNS) + "s"
    number2 = random.randint(1, number1)
    return f" {number1} Причины, по которым {pluranNoun} интереснее, чем вы думаете (Число {number2} удивляет тебя!)"


def generateJobAutomatedHeadline():
    state = random.choice(CITY)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == "Their":
        return f" Этот {state} {noun} не думал, что роботы возьмут {pronoun1} работу. {pronoun2} Были неправы."
    else:
        return f" Этот {state} {noun} не думал, что роботы возьмут {pronoun1} работу. {pronoun2} Были неправы."


if __name__ == "__main__":
    main()