def getSevSegStr(number, minWidth=0):
    
    number = str(number).zfill(minWidth)
    
    rows = ["", "", ""]
    for i, numeral in enumerate(number):
        if numeral == ".":
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "
            continue
        elif numeral == "-":
            rows[0] += "    "
            rows[1] += " __ "
            rows[2] += "    "
        elif numeral == "0":
            rows[0] += " __ "
            rows[1] += "|  |"
            rows[2] += "|__|"
        elif numeral == "1":
            rows[0] += "    "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "2":
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += "|__ "
        elif numeral == "3":
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += " __|"
        elif numeral == "4":
            rows[0] += "    "
            rows[1] += "|__|"
            rows[2] += "   |"
        elif numeral == "5":
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += " __|"
        elif numeral == "6":
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += "|__|"
        elif numeral == "7":
            rows[0] += " __ "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "8":
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += "|__|"
        elif numeral == "9":
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += " __|"

        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "
        
    return "\n".join(rows)

if __name__ == "__main__":
    print("Этот модуль предназначен для импорта, а не для запуска.")
    print("Например, этот код:")
    print(" import sevseg")
    print(" myNumber = getSevSegStr(42, 3)")
    print(" print(MyNumber)")
    print("... напечатает 42, дополненное нулями до трех цифр:")
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
