from sys import exit

def gold_room():
    print("Здесь полно золота. Сколько кг ты унесёшь?")

    choice = input()
    if choice.isalpha():
        dead("Эй, ввести надо число.")
    else:
        how_much = int(choice)


    if how_much < 50:
        print("Шикарно! Ты не жадный, поэтому выйгрываешь!")
        exit(0)
    else:
        dead("Ты слышишь как срабатывает механизм, видать твоя жадность тебя сгубила.")

def bear_room():
    print("Здесь сидит медвед.")
    print("У медведа бочка с мёдом.")
    print("Медвед закрыл собой дверь выхода.")
    print("Как переместить медведа? Отобрать мед или подразнить медведа?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "отобрать мед":
            dead("Медвед посмотрел на тебя и ударил лапой по лицу.")
        elif choice == "подразнить медведа" and not bear_moved:
            print("Медвед отошел от двери")
            print("ВЫ можете войти в нее. Подразнить медведа или войти в дверь?")
            bear_moved = True
        elif choice == "подразнить медведа" and bear_moved:
            dead("Медвед разолился и откусил тебе ногу.")
        elif choice == "войти в дверь" and bear_moved:
            gold_room()
        else:
            print("Введите одно из предложенных действий.")

def cthulhu_room():
    print("На тебя смотрит великий и ужасный Ктулху.")
    print("Он смотрит на тебя и ты начинаешь сходить с ума.")
    print("Убежать или начать сражаться?")

    choice = input("> ")

    if "убежать" in choice:
        start()
    elif "начать сражаться" in choice:
        dead("Хм, возможно, даже удастся победить!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Ты мёртв!")
    exit(0)

def start():
    print("Ты в темной комнате.")
    print("Отсюда ведут две двери, налево и направо.")
    print("Куда ты повернёшь?")

    choice = input("> ")

    if choice == "налево":
        bear_room()
    elif choice == "направо":
        cthulhu_room()
    else:
        dead("Ты ходишь из комнаты в комнату, пока не умираешь с голоду.")

start()
