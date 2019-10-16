i = 0
x = int(input())
y = int(input())
numbers = []

while i < x:
    print(f"В начале значение i равно {i}")
    numbers.append(i)

    i = i + y
    print("Текущее значение:", numbers)
    print(f"В конце значение i равно {i}")

print("значения: ")

for num in numbers:
    print(num)
