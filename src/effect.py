import pyglet
import resources
import core
import math
import vars

class Effect(pyglet.sprite.Sprite):
	def __init__(self, x, y, effect_type, link=None):
		mykey = -1
		graphic = resources.get_graphic(effect_type)
		if effect_type in vars.LETTERS or effect_type in vars.LETTERS2:
			batch=core.top_batch
			if effect_type in vars.LETTERS:
				mykey = link.key_effect
		else:
			batch=core.main_batch
		super(Effect, self).__init__(img=graphic, x=x, y=y, batch=batch)
		self.effect_type = effect_type
		self.life = 0.0
		self.timer = 0.0
		self.timer_ratio = 1.0
		self.active = True
		self.parent = link
		if effect_type == "reticle":	
			self.timer_ratio = 4.0
		self.offsets = [0.0, 0.0]
		if effect_type == "prompt_f":
			self.offsets[0] = -32.0
		elif effect_type == "prompt_g":
			self.offsets[1] = 32.0
		elif effect_type == "prompt_h":
			self.offsets[0] = 32.0
		if mykey > -1:
			self.assigned_key = mykey
		else:
			self.assigned_key = -1
		
		
	def update(self, dt):
		if self.parent:
			self.x, self.y = self.parent.x + self.offsets[0], self.parent.y + self.offsets[1]
		self.life += dt
		self.timer += dt * self.timer_ratio
		if self.effect_type == "info_text":
			#self.rotation = 0 + math.sin(self.life) * 2.0
			self.scale = 1.5 + math.cos(self.life) / 32.0
		elif self.effect_type == "reticle":
			if not self.parent.interactable:
				self.active = False
			self.scale = 1.0 + math.cos(self.timer) / 16.0
			if self.life > vars.INTERACTABLE_TIME:
				self.active = False
		elif self.effect_type == "effect_ret":
			self.rotation += 5
			if not self.parent.interactable: self.active = False
		elif self.effect_type in vars.LETTERS:
			if self.parent.key_effect < 0 or not self.parent.key_effect == self.assigned_key:
				self.active = False
			else:
				self.y += math.sin(self.life) * 10.0
		elif self.effect_type in vars.LETTERS2:
			self.y += math.sin(self.life) / 2.0