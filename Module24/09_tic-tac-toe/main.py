class TicTacToe:
    board = list(range(1, 10))
    wins_coords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    def draw_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.board[0 + i * 3], '|', self.board[1 + i * 3], '|', self.board[2 + i * 3], '|')
        print('-------------')

    def take_input(self, player_token):
        while True:
            value = input(f'Куда поставить: {player_token} ? ')
            if not (value in '123456789'):
                print('Ошибочный ввод. Повторите.')
                continue
            value = int(value)
            if str(self.board[value - 1]) in 'XO':
                print('Эта клетка уже занята')
                continue
            self.board[value - 1] = player_token
            break

    def check_win(self):
        for each in self.wins_coords:
            if (self.board[each[0] - 1]) == (self.board[each[1] - 1]) == (self.board[each[2] - 1]):
                return self.board[each[1] - 1]
        else:
            return False


def main():
    game = TicTacToe()
    counter = 0
    while True:
        game.draw_board()
        if counter % 2 == 0:
            game.take_input('X')
        else:
            game.take_input('O')
        if counter > 3:
            winner = game.check_win()
            if winner:
                game.draw_board()
                print(winner, 'Выиграл!')
                break
        counter += 1
        if counter > 8:
            game.draw_board()
            print('Ничья!')
            break


if __name__ == '__main__':
    main()
