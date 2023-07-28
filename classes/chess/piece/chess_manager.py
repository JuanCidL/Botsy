from classes.chess.piece.king import King
from classes.chess.piece.pawn import Pawn
from classes.chess.board import Board
from classes.chess.image_loader import ImageLoader

class Manager():
  
  def __init__(self, images):
    self.piece_images = ImageLoader.load_pieces()
    self.board_images = ImageLoader.load_boards()
    
    self.pieces = []
    self.board = Board()
    self.image = self.board.image
    
    self.setup()
    
    
  def setup(self):
    for i in range(8):
      self.pawn('white', (i, 1))
      self.pawn('black', (i, 6))
    
    self.king('white', (4, 0))
    self.king('black', (4, 7))
    
    self.turn = 'w'
    
    for piece in self.pieces:
      self.board.add_piece(piece)
      
  def move(self, prev_pos: tuple, post_pos: tuple):
    if self.board[prev_pos[1]][prev_pos[0]].color[0] != self.turn:
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
        image = piece.image
        pos = (self.board.offset[0])
        copy.paste
    
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