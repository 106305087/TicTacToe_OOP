from logic import *
import random
class Game:
  def __init__(self, playerX, playerO):
    self._board = Board()
    self._playerX = playerX
    self._playerO = playerO
    self._current_player = 'O'

  def make_move(self, player):
    valid_move = False
    while not valid_move:
      move = player.get_move(self._board)
      if move is None:
        continue
      row, col = move
      if 0 <= row < 3 and 0 <= col < 3 and self._board.get(row, col) is None:
        valid_move = True
      elif 0 <= row < 3 and 0 <= col < 3 and self._board.get(row, col) is not None:
        print('Please enter the other place.')
      else:
        print('Please enter the valid number.')

    self._board.set(row, col, self._current_player)
    self._current_player = 'O' if self._current_player == 'X' else 'X'
  
  def run(self):
    while self._board.get_winner() is None and not self.is_board_full():
      print(self._board)
      if self._current_player == 'O':
        self.make_move(self._playerX)
      else:
        self.make_move(self._playerO)
    
    print(self._board)
    winner = self._board.get_winner()
    if winner is not None:
      print('{} won!'. format(winner))
    elif winner is None:
      print("It's a draw")
  
  def is_board_full(self):
    for row in self._board._rows:
        for cell in row:
            if cell is None:
                return False
    return True

class Human:
  def get_move(self, board):
    
    player = input('Enter your move for row and column, ex: 1 2: ').split()

    if len(player) != 2:
      print('Please enter only two number, row and column, ex: 1 2')
      return self.get_move(board)
    try:
      row, column = int(player[0])-1, int(player[1])-1
      return row, column
    except ValueError:
      print('Please enter the correct row and column number.')
      return self.get_move(board)


class Bot:
  def get_move(self, board):

    available = []

    for row in range(len(board._rows)):
      for column in range(len(board._rows[row])):
        if board.get(row, column) is None:
          available.append([row, column])
    return random.choice(available)


if __name__ == '__main__':
  game = Game(Human(), Bot())
  game.run()
