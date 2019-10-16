print("Введите Ваше имя:", end=" ")
name = input()
print("Введите Вашу Фамилию:", end=" ")
sname = input()
print("Сколько тебе лет?", end=" ")
age = input()
print("Какой твой рост?", end=" ")
hieght = input()
print("Сколько ты весишь?", end=" ")
wieght = input()

first = f"Итак, тебя зовут {sname} {name}"
second = f"Твой возрост {age}, весишь ты {wieght} и ростом {hieght}"
print("Выберите 1 или 2:")
choice = int(input())
if choice == 1:
    print(first)
elif choice == 2:
    print(second)
else:
    print("Данный выбор не возможен")
