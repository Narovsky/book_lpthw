formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("раз", "два", "три", "четыре"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Спят в конюшне кони,",
    "\nНачал пёс дремать,",
    "\nТолько мальчик Джонни",
    "\nНе ложиться спать!"
))
