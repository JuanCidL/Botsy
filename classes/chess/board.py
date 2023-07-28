class Board():
  def __init__(self, image):
    self.borderoffset = (62, 62)
    self.celloffset = 2
    self.image = image
    self.kings_pos = {'white': (4, 0),
                      'black': (3, 7)}
    self.board = [[None]*8 for _ in range(8)]
  
  def add_piece(self, piece):
    cell = self.board[piece.y][piece.x]
    if cell is None:
      self.board[piece.y][piece.x] = piece
  
  def move(self, prev_pos: tuple, post_pos: tuple):
    piece = self.board[prev_pos[1]][prev_pos[0]]
    if piece is not None:
      return piece.move[post_pos[1]][post_pos[0]]
    return False
  
  def move_check(self, prev_pos: tuple, post_pos: tuple):
    prev_pos_piece = self.board[prev_pos[1]][prev_pos[0]]
    color = prev_pos_piece.color
    post_pos_piece = self.board[post_pos[1]][post_pos[0]]
    
    self.board[prev_pos[1]][prev_pos[0]] = None
    self.board[post_pos[1]][post_pos[0]] = prev_pos_piece
    
    check = self.in_check(color)
    
    self.board[prev_pos[1]][prev_pos[0]] = prev_pos_piece
    self.board[post_pos[1]][post_pos[0]] = post_pos_piece
    
    return check
  
  def in_check(self, color):
    for cell in self.board:
      if cell is not None:
        piece = cell
        if color != piece.color:
          for pos in piece.attack_pos(self):
            if self.kings_pos[color] == pos:
              return True
    return False
    
  def in_mate(self, color):
    x, y = self.kings_pos[color]
    king = self.board[y][x]
    if king.check_moves(self) == list():
      if self.in_check(color):
        return True
    return False
  
  def flip(self):
    return self.board[::-1]