import datetime

DAYS = ("Sunday", "Monday", "Thuesday", "Wednesday", "Thursday",
        "Friday", "Saturday")

MONTHS = ("January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December")

while True:
    print("Введите год для календаря:")
    response = input("> ")
    
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("Пожалуйста, введите числовое значение года, например 2023.")
    continue

while True:
    print("Введите месяц для календаря, 1-12:")
    response = input("> ")

    if not response.isdecimal():
        print("Пожалуйста, введите числовое значение месяца, например, 3 для Марта")
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print("Введите число от 1 до 12.")


def getCalendarFor(year, month):
    calText = ""

    calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"
    
    calText += "...Sunday.....Monday....Tuesday....Wednesday..Thursday....Friday....Saturday..\n"

    weekSeparator = ("+----------" * 7) + "+\n" 

    blankRow = ("|          " * 7) + "+\n"
    
    currentDate = datetime.date(year,month, 1)
    
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator

        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 8)
            currentDate += datetime.timedelta(days=1)

        dayNumberRow += "|\n"
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)

calendarFilename = f"calendar_{year}_{month}.txt"
with open (calendarFilename, "w") as fileObj:
    fileObj.write(calText)

print("Сохранено в " + calendarFilename)


