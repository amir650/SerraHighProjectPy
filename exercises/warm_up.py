import time

import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
running = True
window = pg.display.set_mode((700, 500))
btn = pg.Rect(0, 0, 100, 30)
rect1 = pg.Rect(0, 30, 100, 100)
move_it = False
move_direction = 1

BLACK = (0, 0, 0)

while running:
    clock.tick(60)
    window.fill(BLACK)
    for e in pg.event.get():
        if e.type == pg.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pg.mouse.get_pos()
            if btn.collidepoint((mouseX, mouseY)):
                move_it = not move_it
        elif e.type == pg.QUIT:
            running = False

    if move_it:
        rect1.move_ip(move_direction * 5, 0)
        if not window.get_rect().contains(rect1):
            move_direction = move_direction * -1

    pg.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rect1, 1)
    pg.draw.rect(window, (255, 0, 0) , btn)
    pg.display.flip()
    print(f"loop count = {time.time_ns()}")

#end main loop
pg.quit()