
from settings import *

text_map = [
    'wwwwwwwwwwww',
    'ww.........w',
    'w.ww.w.....w',
    'ww.........w',
    'w.....w..w.w',
    'wwwwwwwwwwww'
    ]

world_map = set()
for j, row in enumerate(text_map):
    for i, col in enumerate(row):
        if col == 'w':
            world_map.add((i*TILE,j*TILE))
