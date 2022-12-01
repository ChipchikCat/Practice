import datetime, random


def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA


print("""Парадокс дня рождения,показывает нам, что в группе из N человек 
шансы  на то, что у двоих из них совпадают дни рождения, на удивление велико.
Эта программа выполняет симуляцию Монте-Карло.
(Т. е. повторяющиеся случайные моделирование), чтобы изучить эту концепцию
(На самом деле это не парадокс, это просто неожиданный результат.""")

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    print("Сколько дней рождения я должен генерировать? (Max 100)")
    response = input (">")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print("Here are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end="")
    monthName = MONTHS[birthday.month - 1]
    dateText = f"{monthName} {birthday.day}"
    print(dateText, end="")
print()
print()

match = getMatch(birthdays)

print("В этой симуляции, ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f"{monthName} {match.day}"
    print('У нескольких людей день рождения', dateText)
else:
    print("Нет подходящих дней рождения.")
print()
print("Generating", numBDays, "random birthdays 100_000 times...")
input("Нажмите Enter, чтобы начать...")

print("Давайте проведем еще 100 000 симуляций.")
sinMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "симуляций прошло...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        sinMatch = sinMatch + 1
print("100_000 симуляций запущено.")

probability = round(sinMatch / 100_000 * 100, 2)
print("Из 100_000 симуляций", numBDays, "люди, были")
print('Совпадение дня рождения в этой группе', sinMatch, "раз.Это означает")
print("Это", numBDays, "у людей есть", probability, "% шанса")
print("Имея соответствующий день рождения в их группе.")
print("Вероятно, это больше, чем вы думаете!")

