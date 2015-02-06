import pyglet
import entity
import core
import resources
from pyglet.window import key
import sys

class Game(pyglet.window.Window):
	def __init__(self):
		super(Game, self).__init__(720, 480)
		self.frame = 0
	def init(self):
		self.cheat = pyglet.sprite.Sprite(resources.graphics["cheat"],x=360, y=240)
		self.logo = pyglet.sprite.Sprite(resources.graphics["factory_logo"],x=184, y=48)
		self.parts = ( 
		pyglet.sprite.Sprite(resources.graphics["partsbox"], x=382, y=160),
		pyglet.sprite.Sprite(resources.graphics["partsbox"], x=412, y=140),
		pyglet.sprite.Sprite(resources.graphics["partsbox"], x=342, y=130)
		
		)
		self.logo.scale = .7
		self.conveyor = pyglet.image.ImageGrid(resources.graphics["conveyor"],3,1)
		pyglet.clock.schedule_interval(self.change_frame, 1/10.0)
		#self.set_fullscreen(True)
	def change_frame(self, dt):
		self.frame -= 1
		if self.frame == -1:
			self.frame = 2
	
	def schedule_lanes(self, dt, lane):
		pyglet.clock.schedule_interval(self.spawn_item, manager.item_spawn_rate, lane=lane)
	
	def update(self, dt):
		core.manager.update(dt)
			
	def on_key_press(self, button, modifiers):
		if core.manager.interactable:	
			if button == key.W:
				core.manager.interactable.update_position(0, 150)
				core.manager.interactable = None
			#elif button == key.S:
			#	core.manager.interactable.update_position(0, -100)
			#	core.manager.interactable = None
			elif button == key.I:
				core.manager.select_action(key.I)
			elif button == key.J:
				core.manager.select_action(key.J)
			elif button == key.K:
				core.manager.select_action(key.K)
			elif button == key.L:
				core.manager.select_action(key.L)
			elif button == key.F:
				core.manager.do_action(key.F)
			elif button == key.G:
				core.manager.do_action(key.G)
			elif button == key.H:
				core.manager.do_action(key.H)
		if button == key.ESCAPE:
			pyglet.app.exit()
			
		
		return pyglet.event.EVENT_HANDLED
		
	def on_key_release(self, button, modifiers):
		return pyglet.event.EVENT_HANDLED
	
	def on_draw(self):
		self.clear()
		resources.graphics["background"].blit(720/2, 480/2)
		self.conveyor[self.frame].blit(100, 180)
		for i in self.parts: i.draw()
		self.conveyor[self.frame].blit(-300, 50)
		
		self.cheat.draw()
		self.logo.draw()
		core.main_batch.draw()
		core.detail_batch.draw()
		core.top_batch.draw()
		core.manager.wage_text.draw()
		core.manager.current_clock.draw()
		if core.manager.timer > 120.0:
			core.manager.help_label.text = "You're done! Your final score is " + str(core.manager.final_score) + "\nThanks for playing!\n\nPlease ESCAPE!"
			resources.graphics["background"].blit(720/2, 480/2)
			self.logo.draw()
		if core.manager.timer > 140.0:
			core.manager.help_label.text = "Sorry about the game running in the background... it's now 2:30am and i'm just super tired so fixing it is not really a priority :p"
		if core.manager.timer > 160.0:
			core.manager.help_label.text = "I was gonna have some witty things here, but yeah, 2:30am, my wit escapes me! Oh well. At least I got this done, mostly. Original concept had a bit more stuff in it, but well, 10 hours before compo deadline I ended scrapping most of my code cause it was just too unmanageable and I had no clue what it was doing... Yes, I coded it sober! Never try a new coding style in the middle of a jam! So this was redone in a hurry. Overall I'm ok with it considering the situation but it could be better... maybe next time!"
		if core.manager.timer > 180.0:
			core.manager.help_label.text = "See ya"
			pyglet.app.exit()
		core.manager.help_label.draw()
		return pyglet.event.EVENT_HANDLED