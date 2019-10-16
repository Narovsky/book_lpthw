states = {
    'Россия': 'RU',
    'Германия': 'DE',
    'Узбекистан': 'UZ',
    'Зимбабве': 'ZW',
    'Турция': 'TR'
    }
cities = {
    'RU': 'Москва',
    'DE': 'Мюнхен',
    'UZ': 'Газли'
}

cities['ZW'] = 'Гверу'
cities['TR'] = 'Сарыгерме'

print('-' * 10)
print("В стране ZW есть город: ", cities['ZW'])
print("В стране RU есть город: ", cities['RU'])

print('-' * 10)
print("Аббревиатура Турции: ", states['Турция'])
print("Аббревиатура Германии: ", states['Германия'])

print('-' * 10)
print('В Турции есть город: ', cities[states['Турция']])
print("В Германии есть город: ", cities[states['Германия']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} имеет аббревиатуру {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"В стране {abbrev} есть город {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"В стране {state} используется аббревиатура {abbrev}")
    print(f"и есть город {cities[abbrev]}")

print('-' * 10)
state = states.get('США')

if not state:
    print("Прошу прощения, США не существует или уничтожено")

city = cities.get('US', 'не существует')
print(f"В стране 'US' есть город: {city}")
