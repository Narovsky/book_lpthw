cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = passangers / cars_driven

print("В наличии", cars, "автомобилей.")
print("И только", drivers, "водителей вышло на работу.")
print("Получается, что", cars_not_driven, "машин пустует.")
print("Мы можем перевезти сегодня", carpool_capacity, "человек.")
print("Сегодня нужно отвезти", passangers, "человек.")
print("В каждой машине будет, примерно", average_passangers_per_car, "человек.")
