from abc import abstractmethod
from classes.chess.piece.observer import Observer
#from board import Board

class Piece(Observer):
  def __init__(self, color: str, pos: tuple):
    self.color = color
    self.pos = pos
    self.x, self.y = pos
    self.not_moved = True
    self.front: str
    self.back: str
    
  @abstractmethod
  def update(self, value) -> None:
    pass
  
  @abstractmethod
  def name(self) -> str:
    pass
  
  def set_images(self, images: dict) -> None:
    self.front = images[f'{self.name()}{self.color[0].upper()}F']
    self.back = images[f'{self.name()}{self.color[0].upper()}B']
  
  @abstractmethod
  def get_raw_moves(self):
    pass
  
  def move(self, board, pos: tuple):
    if pos not in self.check_moves(board, pos):
      return False
    if self.not_moved:
      self.not_moved = False
    self.x, self.y = pos
    self.pos = pos
    return True
  
  # Check if the move is a check position
  def check_moves(self, board, pos: tuple) -> list:
    moves = []
    prev_pos = self.pos
    for move in self.validate_moves(board):
      post_pos = move
      if board.move_check(board, prev_pos, post_pos):
        moves.append(move)
    return moves
  
  # Check if the move is valid
  def validate_moves(self, board):
    moves = []
    for move in self.get_raw_moves():
      x, y = move
      if x<0 or x>7 or y<0 or y>7:
        pass
      cell = board[y][x]
      if cell is not None:
        if cell.color == self.color:
          pass
      moves.append(move)
    return moves
  
  # Get the attacking pos of the piece 
  # (to override it in pawn)
  def attack_pos(self, board):
    return self.valid_moves(self, board)