the_count = [1, 2, 3, 4, 5]
fruits = ["яблоко", "апельсин", "персик", "абрикос"]
change = [1, "червонец", 2, "полтинник", 3, "сотня"]

for number in the_count:
    print(f"Счетчик {number}")

for fruit in fruits:
    print(f"Фрукт: {fruit}")

for i in change:
    print(f"Я получил {i}")

elements = []

elements = [i for i in range(0, 6)]
print(f"Добавление {elements} в список.", sep=" ")

for i in elements:
    print(f"Номер элемента: {i}")
