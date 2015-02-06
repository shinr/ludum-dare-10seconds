import pyglet
import src.resources
import src.game
import os
import random
import src.gamemanager
# core

manager = src.gamemanager.GameManager()

keys = []
toggled = []

bottom_batch = pyglet.graphics.Batch()
main_batch = pyglet.graphics.Batch()
detail_batch = pyglet.graphics.Batch()
top_batch = pyglet.graphics.Batch()
res_directory = os.getcwd() + '/res'
#print res_directory
game_window = src.game.Game()

def init():
	src.resources.load_path(res_directory)
	src.resources.load_graphics()
	src.resources.load_sounds()
	game_window.init()
	manager.init()
	random.seed()