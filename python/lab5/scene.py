import pygame
from sprite import MySprite

all_sprites = pygame.sprite.Group()

bg = MySprite((490, 370))
bg.add_image(
    "/home/dev/Documents/programming/python-sem2/python/lab5/res/bg.jpg", 1
)
all_sprites.add(bg)

borisov_x_start = 700
borisov_x_end = 900
borisov_y = 280

borisov = MySprite((0, 0))
borisov.add_image(
    "/home/dev/Documents/programming/python-sem2/python/lab5/res/borisov.png", 0.5
)
borisov.rotate(0.3, -10, 10)
borisov.linear_move(0.004, (borisov_x_start, borisov_y), (borisov_x_end, borisov_y))

all_sprites.add(borisov)

microphone = MySprite((0, 0))
microphone.add_image(
    "/home/dev/Documents/programming/python-sem2/python/lab5/res/microphone.png", 0.1
)

mic_x_offset = -10
mic_y_offset = -70

microphone.rotate(0.5, -60, -25)
microphone.linear_move(
    0.004,
    (borisov_x_start - mic_x_offset, borisov_y - mic_y_offset),
    (borisov_x_end - mic_x_offset, borisov_y - mic_y_offset),
)
all_sprites.add(microphone)

desk = MySprite((800, 500))
desk.add_image(
    "/home/dev/Documents/programming/python-sem2/python/lab5/res/desk.png", 1.3
)
all_sprites.add(desk)

board = MySprite((170, 260))
board.add_image(
    "/home/dev/Documents/programming/python-sem2/python/lab5/res/board.png", 0.2
)
all_sprites.add(board)

python = MySprite((170, 260))
python.add_image(
    "/home/dev/Documents/programming/python-sem2/python/lab5/res/python-logo.png", 0.15
)
python.rotate(1)
all_sprites.add(python)
