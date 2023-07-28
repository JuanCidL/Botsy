from PIL import Image, ImageDraw

# Colors
colors = {
  'white': (255, 255, 255),
  'black': (0, 0, 0),
  'red': (255, 0, 0),
  'green': (0, 255, 0),
  'blue': (0, 0, 255)
}

cell_size = 160
board_size = cell_size*8
offset = cell_size//2

def darken_color(color, amount):
  r,g,b = color
  r = r*(1-amount)
  g = g*(1-amount)
  b = b*(1-amount)
  return (r,g,b)

def cell(color: tuple):
  img = Image.new('RGBA', (cell_size, cell_size), color)
  draw = ImageDraw.Draw(img)
  draw.rounded_rectangle(
    (0, 0, cell_size-100, cell_size-100),
     outline=darken_color(color, 0.2),
     fill=colors['white'],
     radius=20,
     width = 10)
  return img

light_cell = cell(colors[input('Light color:')])
dark_cell = cell(colors[input('Dark color:')])

light_cell.save('cell.png')