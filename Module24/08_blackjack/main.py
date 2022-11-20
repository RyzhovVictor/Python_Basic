import random


class Card:
    def __init__(self, other):
        self.suit = other[0][1]
        self.rang = other[0][0]
        self.value = other[1]

    def __repr__(self):
        return f'{self.suit} {self.rang}'

    def give_point(self):
        return self.value

    def give_rang(self):
        return self.rang


class Bot:
    list_card = []
    point = 0

    def __init__(self, other):
        self.name = 'Бот'
        self.other = other
        self.get_shuffle()

    def __repr__(self):
        return f'{self.name}: {self.list_card}'

    def get_shuffle(self):
        self.list_card.append(self.other.give_out_playing_card())
        self.list_card.append(self.other.give_out_playing_card())
        for card in self.list_card:
            self.point += card.give_point()

    def bot_game(self):
        while self.point < 17:
            self.list_card.append(self.other.give_out_playing_card())
            self.point += self.list_card[-1].give_point()
            self.give_point()

    def give_point(self):
        flag = False
        tmp_count = 0
        while self.point > 21:
            if flag and tmp_count != 0:
                self.point -= 10
                break
            if flag:
                break
            for card in self.list_card:
                if card.give_rang() == 'Туз':
                    tmp_count += 1
            if tmp_count > 1:
                self.point -= ((tmp_count - 1) * 10)
            flag = True

        return self.point


class Player:
    list_card = []
    point = 0

    def __init__(self, other):
        self.name = 'Вы'
        self.other = other
        self.get_shuffle()

    def __repr__(self):
        return f'{self.name}: {self.list_card}'

    def get_shuffle(self):
        self.list_card.append(self.other.give_out_playing_card())
        self.list_card.append(self.other.give_out_playing_card())
        for card in self.list_card:
            self.point += card.give_point()

    def get_game_card(self):
        self.list_card.append(self.other.give_out_playing_card())
        self.point += self.list_card[-1].give_point()

    def give_point(self):
        flag = False
        tmp_count = 0
        while self.point > 21:
            if flag and tmp_count != 0:
                self.point -= 10
                break
            if flag:
                break
            for card in self.list_card:
                if card.give_rang() == 'Туз':
                    tmp_count += 1
            if tmp_count > 1:
                self.point -= ((tmp_count - 1) * 10)
            flag = True

        return self.point


class Deck:
    deck_cards = {
        ('Десятка', 'Червы'): 10, ('Десятка', 'Бубны'): 10, ('Десятка', 'Крести'): 10, ('Десятка', 'Пики'): 10,
        ('Девятка', 'Червы'): 9, ('Девятка', 'Бубны'): 9, ('Девятка', 'Крести'): 9, ('Девятка', 'Пики'): 9,
        ('Восьмерка', 'Червы'): 8, ('Восьмерка', 'Бубны'): 8, ('Восьмерка', 'Крести'): 8, ('Восьмерка', 'Пики'): 8,
        ('Семерка', 'Червы'): 7, ('Семерка', 'Бубны'): 7, ('Семерка', 'Крести'): 7, ('Семерка', 'Пики'): 7,
        ('Шестерка', 'Червы'): 6, ('Шестерка', 'Бубны'): 6, ('Шестерка', 'Крести'): 6, ('Шестерка', 'Пики'): 6,
        ('Пятерка', 'Червы'): 5, ('Пятерка', 'Бубны'): 5, ('Пятерка', 'Крести'): 5, ('Пятерка', 'Пики'): 5,
        ('Четверка', 'Червы'): 4, ('Четверка', 'Бубны'): 4, ('Четверка', 'Крести'): 4, ('Четверка', 'Пики'): 4,
        ('Тройка', 'Червы'): 3, ('Тройка', 'Бубны'): 3, ('Тройка', 'Крести'): 3, ('Тройка', 'Пики'): 3,
        ('Двойка', 'Червы'): 2, ('Двойка', 'Бубны'): 2, ('Двойка', 'Крести'): 2, ('Двойка', 'Пики'): 2,
        ('Валет', 'Червы'): 10, ('Валет', 'Бубны'): 10, ('Валет', 'Крести'): 10, ('Валет', 'Пики'): 10,
        ('Дама', 'Червы'): 10, ('Дама', 'Бубны'): 10, ('Дама', 'Крести'): 10, ('Дама', 'Пики'): 10,
        ('Король', 'Червы'): 10, ('Король', 'Бубны'): 10, ('Король', 'Крести'): 10, ('Король', 'Пики'): 10,
        ('Туз', 'Червы'): 11, ('Туз', 'Бубны'): 11, ('Туз', 'Крести'): 11, ('Туз', 'Пики'): 11,
    }
    lst_gamer = []

    def __init__(self):
        self.lst_gamer.append(Player(self))
        self.lst_gamer.append(Bot(self))
        self.bot = self.lst_gamer[1]

    def pin_amount_deck(self):
        return len(self.deck_cards)

    def give_out_playing_card(self):
        choice = random.choice(list(self.deck_cards.items()))
        self.deck_cards.pop(choice[0])
        return Card(choice)


game = Deck()
player = game.lst_gamer[0]

while True:
    print()
    print(player)
    print(f'Всего очков: {player.give_point()}')
    print(f'\nКарт в колоде осталось: {game.pin_amount_deck()}')
    if int(input('Будите брать карту ? 1/0 -> ')) == 0:
        break
    else:
        player.get_game_card()

if player.give_point() <= 21:
    game.bot.bot_game()
    if game.bot.give_point() < player.give_point():
        print('\n***Вы победили***\n')
    elif game.bot.give_point() == player.give_point():
        print('\n***Все остались при своих***\n')
    else:
        print('\n***Вы проиграли***\n')
else:
    print('\n***Вы проиграли***\n')

print(f'\nКарты бота: {game.bot.list_card}')
print(f'Очки карт бота: {game.bot.give_point()}')
