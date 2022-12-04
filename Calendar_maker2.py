import calendar
# print(calendar.Calendar().monthdatescalendar(2022, 10)) # Простой вывод календаря.
# calendar.TextCalendar().prmonth(2022, 10) # Печает только 1 месяц в году.
# print(calendar.HTMLCalendar().formatmonth(2022, 10)) # Для HTML.
# print(calendar.HTMLCalendar().formatyear(2022, 10)) # Для HTML.
# calendar.TextCalendar().pryear(2022)
print(calendar.LocaleTextCalendar(locale="Russian_Russia").formatyear(2022)) # С добавлением языков.
