import pygame
import serial
port = 'COM7'
bautRate = 9600


try:
    ser = serial.Serial(port, bautRate, timeout=None)
    arduino = 'ada'
    #startNyelem = 1000
except:
    arduino = 'gada'
    print('------------gada arduino------------')

pygame.init()

#initialise the joystick module
pygame.joystick.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Joysticks")

#define font
font_size = 30
font = pygame.font.SysFont("Futura", font_size)

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#create clock for setting game frame rate
clock = pygame.time.Clock()
FPS = 60

#create empty list to store joysticks
joysticks = []

#create player rectangle
x = 350
y = 200
player = pygame.Rect(x, y, 100, 100)

xx = 0
yy = 0
xx2 = 0
yy2 = 0

#define player colour
col = "royalblue"

#game loop
run = True
while run:

  clock.tick(FPS)

  #update background
  screen.fill(pygame.Color("midnightblue"))

  #draw player
  player.topleft = (x, y)
  pygame.draw.rect(screen, pygame.Color(col), player)

  #show number of connected joysticks
  draw_text("Controller: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)


  for joystick in joysticks:
    
    # respon pada button
    if joystick.get_button(0):
      print('A')
    if joystick.get_button(1):
      print('B')
    if joystick.get_button(2):
      print('X')
    if joystick.get_button(3):
      print('Y')
    if joystick.get_button(4):
      print('L1')
    if joystick.get_button(5):
      print('R1')

    # respon pada analog
    # if joystick.get_axis(0) > 0:
    #   print('Gerak Kanan Analog Kiri')
    # if joystick.get_axis(0) < 0:
    #   print('Gerak Kiri Analog Kiri')
    # if joystick.get_axis(1) > 0:
    #   print('Gerak Bawah Analog Kiri')
    # if joystick.get_axis(1) < 0:
    #   print('Gerak Atas Analog Kiri')
    if joystick.get_axis(2) > 0 : 
      print('L2')
    # if joystick.get_axis(3) > 0:
    #   print('Gerak Kanan Analog Kanan')
    # if joystick.get_axis(3) < 0:
    #   print('Gerak Kiri Analog Kanan')
    # if joystick.get_axis(4) > 0:
    #   print('Gerak Bawah Analog Kanan')
    # if joystick.get_axis(4) < 0:
    #   print('Gerak Atas Analog Kanan')
    if joystick.get_axis(5) > 0 : 
      print('R2')

    # respon pada button arrow
    hats = joystick.get_numhats()
    for i in range(hats):
      hat = joystick.get_hat(i)
      if hat[0]==-1:
        print("Arrow Kiri")
        x-=5
      if hat[0]==1:
        print("Arrow Kanan")
        x+=5
      if hat[1]==-1:
        print("Arrow Bawah")
        y+=5
      if hat[1]==1:
        print("Arrow Atas")
        y-=5

    # gerak analog kiri
    horiz_move = joystick.get_axis(0)
    vert_move = joystick.get_axis(1)
    if abs(vert_move) > 0.05:
      y += vert_move * 5
      yy = vert_move * 5
    if abs(horiz_move) > 0.05:
      x += horiz_move * 5
      xx = horiz_move * 5

    # gerak analog kanan
    horiz_move2 = joystick.get_axis(3)
    vert_move2 = joystick.get_axis(4)
    if abs(vert_move2) > 0.05:
      y += vert_move2 * 5
      yy2 = vert_move2 * 5
    if abs(horiz_move2) > 0.05:
      x += horiz_move2 * 5
      xx2 = horiz_move2 * 5

    # Vertikal Analog Kiri
    if yy >= 2.5:
      print('Gerak Bawah Analog Kiri')
      yy = 0
    if yy < 2.5 and yy > 1:
      print('Gerak Bawah Sedikit Analog Kiri')
      yy = 0

    if yy <= -2.5:
      print('Gerak Atas Analog Kiri')
      yy = 0
    if yy > -2.5 and yy < -1:
      print('Gerak Atas Sedikit Analog Kiri')
      yy = 0

    # Horizontal Analog Kiri
    if xx >= 2.5:
      print('Gerak Kanan Analog Kiri')
      xx = 0
    if xx < 2.5 and xx > 1:
      print('Gerak Kanan Sedikit Analog Kiri')
      xx = 0

    if xx <= -2.5:
      print('Gerak Kiri Analog Kiri')
      xx = 0
    if xx > -2.5 and xx < -1:
      print('Gerak Kiri Sedikit Analog Kiri')
      xx = 0

    # Vertikal Analog Kanan
    if yy2 >= 2.5:
      print('Gerak Bawah Analog Kanan')
      yy2 = 0
    if yy2 < 2.5 and yy2 > 1:
      print('Gerak Bawah Sedikit Analog Kanan')
      yy2 = 0

    if yy2 <= -2.5:
      print('Gerak Atas Analog Kanan')
      yy2 = 0
    if yy2 > -2.5 and yy2 < -1:
      print('Gerak Atas Sedikit Analog Kanan')
      yy2 = 0

    # Horizontal Analog Kanan
    if xx2 >= 2.5:
      print('Gerak Kanan Analog Kanan')
      xx2 = 0
    if xx2 < 2.5 and xx2 > 1:
      print('Gerak Kanan Sedikit Analog Kanan')
      xx2 = 0

    if xx2 <= -2.5:
      print('Gerak Kiri Analog Kanan')
      xx2 = 0
    if xx2 > -2.5 and xx2 < -1:
      print('Gerak Kiri Sedikit Analog Kanan')
      xx2 = 0

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
      joy = pygame.joystick.Joystick(event.device_index)
      joysticks.append(joy)
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()

# KOnfigurasi untuk Linux

# Axis 0 value = -0, analog kiri gerak kiri, 0.992, analog kiri gerak kanan
# Axis 1 value = -0.992, analog kiri gerak atas, 1, analog kiri gerak bawah
# Axis 2 value = 1, R2 ditekan, -1,  R2 dilepas
# Axis 3 value =  -1, analog kanan gerak kiri,  0.992 analog kanan gerak kanan
# Axis 4 value =  -0.992 analog kanan gerak atas,  1, analog kanan gerak bawah
# Axis 5 value = 1, L2 ditekan, -1,  L2 dilepas

# Default Value
# Axis 0 value: 0
# Axis 1 value: -0
# Axis 2 value: -1
# Axis 3 value: 0
# Axis 4 value: -0
# Axis 5 value: -1

# Button 0 value: 0 (A)
# Button 1 value: 0 (B)
# Button 2 value: 0 (X)
# Button 3 value: 0 (Y)
# Button 4 value: 0 (L1)
# Button 5 value: 0 (R1)
# Button 6 value: 0 (SELECT)
# Button 7 value: 0 (START)
# Button 8 value: 0 (HOME)
# Button 9 value: 0 (R3)
# Button 10 value: 0 (L3)

# Hat 0 value: (0,0)
# Hat 0 value: (0,1) (Arrow Atas)
# Hat 0 value: (0,-1) (Arrow Bawah)
# Hat 0 value: (1,0) (Arrowa Kanan)
# Hat 0 value: (-1,0) (Arrow Kiri)

