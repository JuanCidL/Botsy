from classes.chess.piece.king import King
from classes.chess.piece.pawn import Pawn
from classes.chess.board import Board
from classes.chess.image_loader import ImageLoader

class Manager():
  
  def __init__(self):
    self.piece_images = ImageLoader.load_pieces()
    self.board_images = ImageLoader.load_boards()
    
    self.pieces = []
    self.board = self.board()
    self.board.set_manager(self)
    self.image = self.board.image.copy()
    
    self.setup()
  
  def update(self):
    pieces = []
    for row in self.board.board:
      for cell in row:
        if cell is not None:
          piece = cell
          pieces.append(piece)
    self.pieces = pieces
    
  def setup(self):
    for i in range(8):
      self.pawn('white', (i, 6))
      self.pawn('black', (i, 1))
    
    self.king('white', (4, 7))
    self.king('black', (3, 0))
    
    self.turn = 'w'
    
    for piece in self.pieces:
      self.board.add_piece(piece)
      
  def move(self, prev_pos: tuple, post_pos: tuple):
    
    cell = self.board.board[prev_pos[1]][prev_pos[0]]
    if cell is not None:
      piece = cell
      if piece.color[0] != self.turn:
        return False
      if self.turn == 'w':
        self.turn = 'b'
      if self.turn == 'b':
        self.turn = 'w'
    return self.board.move(prev_pos, post_pos)
    
  
  def to_image(self):
    copy = self.image.copy()
    for piece in self.pieces:
      if piece.color[0] == self.turn:
        image = piece.back
      else:
        image = piece.front
      pos = self.board.pos_board(piece.pos)
      copy.paste(image, pos, image)
    return copy
  
  def flip(self, board):
    bd = []
    for i in range(8):
      bd[i] = board[8-i][::-1]
    return bd
    
  def add(self, piece):
    self.pieces.append(piece)
  
  def pawn(self, color: str, pos: tuple):
    piece = Pawn(color, pos)
    piece.set_images(self.piece_images)
    self.add(piece)
    return piece
  
  def king(self, color: str, pos: tuple):
    piece = King(color, pos)
    piece.set_images(self.piece_images)
    self.add(piece)
    return piece
    
  def board(self, num=1):
    image = self.board_images[f'Board0{num}']
    return Board(image)