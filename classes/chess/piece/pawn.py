from classes.chess.piece.piece import Piece

class Pawn(Piece):
  def __init__(self, color: str, pos: tuple):
    super().__init__(color, pos)
    self.en_passant = [False, False]
  
  def name(self):
    return 'P'
    
  def get_raw_moves(self):
    x, y = self.pos
    if self.color[0] == 'w':
      return [(x, y-1),
              (x+1, y-1),
              (x-1, y-1)]
    elif self.color[0] == 'b':
      return [(x, y+1),
              (x+1, y+1),
              (x-1, y+1)]
  
  def move(self, board, pos: tuple):
    # Check invalid moves
    if pos not in self.check_moves(board):
      return False
    if self.not_moved:
      # Check if starts with a jump to
      # set en_passant to possible other pawn
      x, y = pos
      if (y-self.y)**2>1:
        if not (x+1 > 7):
          cell = board.board[y][x+1]
          if isinstance(cell, Pawn):
            cell.en_passant[1] = True
        if not (x-1 < 0):
          cell = board.board[y][x-1]
          if isinstance(cell, Pawn):
            cell.en_passant[0] = True
    return super().move(board, pos)
    
  def validate_moves(self, board):
    moves = []
    # Check the first move
    if self.not_moved:
      if self.color[0] == 'w':
        moves.append((self.x, self.y-2))
      elif self.color[0] == 'b':
        moves.append((self.x, self.y+2))
      
    # Check en_passant by left
    if self.en_passant[0]:
      self.en_passant[0] = False
      if self.color[0] == 'w':
        if not (self.x-1 < 0):
          moves.append((self.x-1, self.y-1))
      if self.color[0] == 'b':
        if not (self.x+1 > 7):
          moves.append((self.x+1, self.y+1))
      
    # Check en_passant by right
    if self.en_passant[1]:
      self.en_passant[1] = False
      if self.color[0] == 'w':
        if not (self.x+1 > 7):
          moves.append((self.x+1, self.y-1))
      if self.color[0] == 'b':
        if not (self.x-1  < 0):
          moves.append((self.x-1, self.y+1))
      
    # Check standar pawn moves
    for move in super().validate_moves(board):
      if move[0] != self.x:
        if board.board[move[1]][move[0]] is not None:
          moves.append(move)
      elif board.board[move[1]][move[0]] is None:
        moves.append(move)
    return moves
  
  def attack_pos(self, board):
    moves = []
    for move in self.validate_moves(board):
      if move[0] != self.x:
        moves.append(move)
    return moves
