try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


print("Шифр Цезаря шифрует буквы, сдвигая их на")
print("номер ключа. Например, ключ 2 означает, что буква А")
print("зашифрована в C, буква B зашифрована в D и так далее.")
print()

while True: 
    print("Вы хотите (e)ncrypt(зашифровать) или (d)ecrypt(расшифровать)?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Пожалуйста, введите букву 'e' или 'd'.")

while True:
    maxKey = len(SYMBOLS) - 1
    print(f"Пожалуйста, введите ключ (0 to {maxKey}) для сдвига.")
    response = input("> ").upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print(f"Введите сообщение, чтобы {mode}")
message = input("> ")

message = message.upper()

translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
            
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f"Полный {mode}ed текст скопирован в буфер обмена.")
except:
    pass


