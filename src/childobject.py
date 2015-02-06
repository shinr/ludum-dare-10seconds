import pyglet
import resources
import core
import vars
import effect
import random

class ChildObject(pyglet.sprite.Sprite):
	def __init__(self, x, y, parent, slot):
		if slot == vars.SPOT_1:
			graphic = resources.get_graphic("part_antenna")
		elif slot == vars.SPOT_2:
			graphic = resources.get_graphic("part_screen")
		elif slot == vars.SPOT_3:
			graphic = resources.get_graphic("part_speaker")
		elif slot == vars.SPOT_4:
			graphic = resources.get_graphic("part_dial")
		super(ChildObject, self).__init__(img=graphic, x=x, y=y, batch=core.detail_batch)
		self.active = True
		self.interactable = True
		core.manager.effects.append(effect.Effect(self.x, self.y, "effect_ret", link=self))
		self.parent = parent
		self.slot = slot
	
	def update(self, dt):
		self.x, self.y = self.parent.get_position(self.slot)
		if not self.parent.interactable: self.interactable = False
		
		
		