from PIL import Image, ImageDraw, ImageFont

fontsize = 40
font = ImageFont.truetype('../../fonts/8_bit_wonder.ttf', size=fontsize)

# Colors
colors = {
  'transparent': (0,0,0,0),
  'white': (255, 255, 255),
  'black': (0, 0, 0),
  'red': (255, 0, 0),
  'green': (0, 255, 0),
  'blue': (0, 0, 255)
}

# Darkens colors
def darken_color(color, amount):
  r,g,b = color
  r = round(r*(1-amount))
  g = round(g*(1-amount))
  b = round(b*(1-amount))
  return (r,g,b)

# Board sizes
cell_size = 160
board_size = cell_size*8
offset = cell_size*3//4

# Creates the cells images
def cell(color: tuple):
  img = Image.new('RGBA', (cell_size, cell_size), colors['transparent'])
  draw = ImageDraw.Draw(img)
  draw.rounded_rectangle(
    (0, 0, cell_size, cell_size),
     outline=darken_color(color, 0.2),
     fill=color,
     radius=20,
     width = 5)
  return img

# Light and dark cells
light_color = colors[input('Light color: ')]
dark_color = colors[input('Dark color: ')]
light_cell = cell(light_color)
dark_cell = cell(dark_color)

# Creation of the board
board = Image.new('RGBA', (board_size, board_size), colors['transparent'])

# Draw the cells
cell = None
for i in range(8):
  for j in range(8):
    x = cell_size*i
    y = cell_size*j
    
    if (i + j) % 2 == 0:
      cell = light_cell
    else:
      cell = dark_cell
    
    board.paste(cell, (x, y), cell)

full_board = Image.new('RGBA',
             (offset*2 + board_size, offset*2 + board_size),
             colors['transparent'])
draw = ImageDraw.Draw(full_board)

draw.rounded_rectangle(
  (offset-10, offset-10,
  offset + board_size + 10, offset + board_size + 10),
   fill=darken_color(light_color, 0.2),
   outline=darken_color(dark_color, 0.2),
   radius=40,
   width = 5)

draw.rounded_rectangle(
  (offset-20, offset-20,
  offset + board_size + 20, offset + board_size + 20),
   outline=darken_color(light_color, 0.2),
   radius=40,
   width = 7)

full_board.paste(board, (offset, offset), board)

letters = 97
numbers = 1
for i in range(8):
  rad = 30
  move = i*cell_size
  midfont = fontsize//2
  
  x_offset = offset//2
  y_offset = offset + cell_size//2
  draw.chord((
    x_offset-rad,
    y_offset-rad + move,
    x_offset+rad,
    y_offset+rad + move),
    0, 360,
    fill=light_color,
    outline=darken_color(light_color, 0.2),
    width=5)
  draw.text((x_offset-midfont+3, y_offset+move-midfont-2),
    f'{8-i}',
    font=font,
    fill=darken_color(dark_color, 0.2))
  
  
  x_offset = offset + cell_size//2
  y_offset = offset + board_size + offset//2
  draw.chord((
    x_offset-rad + move,
    y_offset-rad,
    x_offset+rad + move,
    y_offset+rad),
    0, 360,
    fill=light_color,
    outline=darken_color(light_color, 0.2),
    width=5)
  draw.text((x_offset+move-midfont+3, y_offset-midfont-2),
    chr(letters),
    font=font,
    fill=darken_color(dark_color, 0.2))
  
  letters += 1


full_board = full_board.rotate(180)
draw = ImageDraw.Draw(full_board)

for i in range(8):
  rad = 30
  move = i*cell_size
  midfont = fontsize//2
  
  x_offset = offset//2
  y_offset = offset + cell_size//2
  draw.chord((
    x_offset-rad,
    y_offset-rad + move,
    x_offset+rad,
    y_offset+rad + move),
    0, 360,
    fill=dark_color,
    outline=darken_color(dark_color, 0.2),
    width=5)
  draw.text((x_offset-midfont+3, y_offset+move-midfont-2),
    f'{i+1}',
    font=font,
    fill=darken_color(light_color, 0.2))

  x_offset = offset + cell_size//2
  y_offset = offset + board_size + offset//2
  draw.chord((
    x_offset-rad + move,
    y_offset-rad,
    x_offset+rad + move,
    y_offset+rad),
    0, 360,
    fill=dark_color,
    outline=darken_color(dark_color, 0.2),
    width=5)
  letters -= 1
  draw.text((x_offset+move-midfont+3, y_offset-midfont-2),
    chr(letters),
    font=font,
    fill=darken_color(light_color, 0.2))
  

full_board = full_board.rotate(180)

full_board.save('board.png')