from classes.chess.piece.piece import Piece

class Rook(Piece):
  def __init__(self, color: str):
    super().__init__(color)
  
  def update(self, value) -> None:
    pass
  
  def setimages(self, images: dict) -> None:
    self.front = images[f'C{self.color[0].upper()}F']
    self.back = images[f'C{self.color[0].upper()}B']
  
  def check_moves(self, value) -> list:
    return ['a']
  
