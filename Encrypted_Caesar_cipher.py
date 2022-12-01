print("Введите зашифрованное сообщение шифра Цезаря для взлома.")
message = input("> ")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

for key in range(len(SYMBOLS)):
    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
        
    print(f"Ключ # {key}: {translated}")
