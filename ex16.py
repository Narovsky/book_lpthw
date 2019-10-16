from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C).")
print("Если Вы хотите стереть файл, нажмите клавишу Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла.")
target.truncate()

print("Теперь я запрошу у Вас три строки.")

line1 = input("Строка 1: ")
line2 = input("СТрока 2: ")
line3 = input("СТрока 3: ")

print("Это я запишу в файл.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Наконец, я закрою файл.")
target.close()
