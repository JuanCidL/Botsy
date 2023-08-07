class Board():
  def __init__(self, image):
    self.cellsize = 160
    self.offset = self.cellsize*3//4
    self.manager = None
    self.image = image
    self.kings_pos = {'white': (4, 0),
                      'black': (3, 7)}
    self.board = [[None]*8 for _ in range(8)]
  
  def set_manager(self, manager):
    self.manager = manager
  
  def notify(self):
    self.manager.update()
  
  def add_piece(self, piece):
    cell = self.board[piece.y][piece.x]
    if cell is None:
      self.board[piece.y][piece.x] = piece
  
  def move(self, prev_pos: tuple, post_pos: tuple):
    cell = self.board[prev_pos[1]][prev_pos[0]]
    if cell is not None:
      piece = cell
      
      move = piece.move(self, post_pos)
      if move:
        self.board[prev_pos[1]][prev_pos[0]] = None
        if self.board[post_pos[1]][post_pos[0]] != None:
          self.board[post_pos[1]][post_pos[0]] = piece
          self.notify()
        else:
          self.board[post_pos[1]][post_pos[0]] = piece
        
      return move
    return False
  
  def pos_board(self, pos: tuple):
    x, y = pos
    piece_height = 260
    y_center = 30
    y_correction = -piece_height  - self.cellsize//2 + y_center
    x = x*self.cellsize + self.offset
    y = (y+1)*self.cellsize + self.offset + y_correction
    return (x, y)
  
  def move_check(self, prev_pos: tuple, post_pos: tuple):
    prev_pos_piece = self.board[prev_pos[1]][prev_pos[0]]
    if prev_pos_piece is None:
      return False
    post_pos_piece = self.board[post_pos[1]][post_pos[0]]
    color = prev_pos_piece.color
    
    self.board[prev_pos[1]][prev_pos[0]] = None
    self.board[post_pos[1]][post_pos[0]] = prev_pos_piece
    
    check = self.in_check(color)
    
    self.board[prev_pos[1]][prev_pos[0]] = prev_pos_piece
    self.board[post_pos[1]][post_pos[0]] = post_pos_piece
    
    return check
  
  def in_check(self, color):
    for row in self.board:
      for cell in row:
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