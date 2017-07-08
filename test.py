# -*- coding: utf-8 -*-

from test1 import *

import pyglet
game_window = pyglet.window.Window(800, 600)



@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()
    
    player_ship.draw()
    
    
if __name__ == '__main__':
    pyglet.app.run()
    