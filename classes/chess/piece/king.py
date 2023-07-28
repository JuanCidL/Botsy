from classes.chess.piece.piece import Piece

class King(Piece):
  def __init__(self, color: str, pos: tuple):
    super().__init__(color, pos)
  
  def update(self, value) -> None:
    pass
  
  def name(self):
    return 'K'
  
  def raw_moves(self) -> list:
    x, y = self.pos
    return [(x, y+1),
            (x, y-1),
            (x+1, y),
            (x-1, y),
            (x+1, y+1),
            (x+1, y-1),
            (x-1, y+1),
            (x-1, y-1)]
  
  def validate_moves(self, board):
    moves = []
    
    if self.not_moved:
      if self.color[0] == 'w':
        # Left castle
        if board[0][0] is not None:
          if board[0][1] is None and board[0][2] is None and board[0][3]:
            moves.append((2, 0))
        # Right castle
        if board[0][7] is not None:
          if board[0][5] is None and board[0][6]:
            moves.append((6, 0))
      
      if self.color[0] == 'b'
        # Left castle
        if board[7][0] is not None:
          if board[7][1] is None and board[7][2] is None and board[7][3]:
            moves.append((6, 7))
        # Right castle
        if board[7][7] is not None:
          if board[7][5] is None and board[7][6]:
            moves.append((2, 7))
    
    for move in super().validate_moves(board):
      moves.append(move)
    
    return moves