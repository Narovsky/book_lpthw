class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def sum_num(self):
        for x in self.lyrics:
            print(x ** 2)



happy_bday = Song(["Не могу я тебе в день рождения",
                    "Дорогие подарки дарить",
                    "Но зато в эти ночи весенние "])

bulls_on_parade = Song(["Белые розы, белые розы",
                        "Беззащитны шипы"])

num = Song([1,2,3,4])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

num.sum_num()
