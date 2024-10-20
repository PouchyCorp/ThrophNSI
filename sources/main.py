import pygame as pg
import sys
from objects.placeable import Placeable
from objects.coord import Coord
from objects.room_config import R1, R2, R3
from objects.popup_config import pop_up_test


WIN = pg.display.set_mode((1920, 1080))
CLOCK = pg.time.Clock()

def draw_grid():
    for x in range(320):
        for y in range(180):
            if x % 2 == 0 and y % 2 != 0:
                pg.draw.rect(WIN, (70, 70, 70), pg.Rect(x * 6, y * 6, 6, 6))
            elif x % 2 != 0 and y % 2 == 0:
                pg.draw.rect(WIN, (70, 70, 70), pg.Rect(x * 6, y * 6, 6, 6))

current_room = R1
popup_active = False     

while True:
    CLOCK.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            for placeable in current_room.placed:
                if placeable.rect.collidepoint(pos[0], pos[1]):
                    match placeable.name:
                        case 'R1_stairs':
                            current_room = R2
                        case 'R2_stairs':
                            current_room = R3
                        case "test_place":
                            popup_active = True
                        case _:
                            print('you should not be seeing this')
                            popup_active = True


    WIN.blit(pg.transform.scale_by(current_room.bg_surf, 6), (0, 0))
    WIN.blits([(placeable.surf, placeable.coord.xy) for placeable in current_room.placed])


    if popup_active:
        pop_up_test.draw(WIN)

    pg.display.flip()
