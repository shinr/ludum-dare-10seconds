import pyglet
import vars
import entity
import effect
import random
import resources
import math
from pyglet.window import key

class GameManager:
	def __init__(self):
		self.to_delete = []
		self.entities = []
		self.effects = []
		self.interactable = None
		self.action = None
		self.action_current_key = 0
		self.wage = 0.0
		self.base_wage = 5.0
		self.bonus = 1.0
		self.final_score = 0.0
		self.wage_info = "Wage per completed product $$"
		self.bonus_info = "X bonus! Total wage "
		self.help = "HOW TO PLAY:\nUse keys next to Parts box to select parts to attach to a device. Then use keys as prompted to fix the stuff. You have 10 seconds per device to attach as many parts as you can before the device rolls off. Press W to move device to upper conveyor belt in order to score. More parts you attach, bigger your bonus. If a device rolls off, your bonus is reset. Good luck!"
		self.help_label = pyglet.text.Label(text=self.help, x=10, y=430,multiline=True, width=592)
		self.wage_text = pyglet.text.Label(text=self.wage_info + str(self.base_wage) + " - " + str(self.bonus)		+ self.bonus_info + str(self.wage), bold=True, x=180, y=460)
		
		self.player = pyglet.media.Player()
		self.timer = 0.0
		self.current_clock =  pyglet.text.Label(text=str(100.0 - self.timer), bold=True, x=10.0, y=460.0)
	def init(self):
		pyglet.clock.schedule_interval(self.spawn_item, vars.SPAWN_RATE)
		self.effects.append(effect.Effect(600, 42, "info_text"))
		self.player.eos_action="loop"
		self.player.queue(resources.music)
		self.player.play()
		self.effects.extend([
			effect.Effect(350, 160, "prompt_i"),
			effect.Effect(370, 160, "prompt_j"),
			effect.Effect(390, 150, "prompt_k"),
			effect.Effect(410, 140, "prompt_l"),
		]
		)
	
	def update(self, dt):
		for ent in self.entities:
			ent.update(dt)
			if not ent.active:
				self.to_delete.append(ent)
		for eff in self.effects:
			eff.update(dt)
			if not eff.active:
				self.to_delete.append(eff)
		for item in self.to_delete:
			if item in self.effects:
				item.delete()
				self.effects.remove(item)
			elif item in self.entities:
				item.delete()
				self.entities.remove(item)
		self.to_delete = []
		self.timer += dt
		if self.timer > 20.0: self.help_label.text = "W to move a device on the upper conveyor belt"
		if self.timer > 120.0:	
			self.final_score = self.wage
		self.current_clock.text = "Time left! " + str(round(120.0 - self.timer))
		self.wage_text.text=self.wage_info + str(self.base_wage) + " - " + str(self.bonus)	+ self.bonus_info + str(self.wage)
	
	def select_action(self, key):
		if self.action:
			return
		self.action = self.interactable.add_child(key)
		self.action_current_key = 0
	
	def play_sound(self, sound="random", type="bang"):
		if sound == "random":
			if type=="bang":
				sfx = random.randint(0, 3)
				if sfx == 0:
					resources.sfxs["bang"].play()
				elif sfx == 1:
					resources.sfxs["bang2"].play()
				elif sfx == 2:
					resources.sfxs["bang3"].play()
				else:
					resources.sfxs["bang4"].play()
	
	def do_action(self, key):
		
		if not self.action:
			return
		if key == vars.ACTIONS[self.action][self.action_current_key]:
			self.action_current_key += 1
			if self.action_current_key == len(vars.ACTIONS[self.action]):
				#print len(vars.ACTIONS[self.action]), self.action_current_key
				self.interactable.do_action(self.action, last=True)
				self.action_current_key = 0
				self.action = None
			else:
				self.interactable.do_action(self.action)
		else:
			self.action_current_key = 0
	
		
	def spawn_item(self, dt):
		self.bonus -= .1
		#if random.random() < .5:
		self.entities.append(entity.Entity(x=-40, y= 150, entity_type="belt_item_base"))
		#else:
		#	self.entities.append(entity.Entity(x=-40, y= 150, entity_type="belt_item_broken"))
			
	def set_interactable(self, ent):
		self.interactable = ent
		if self.action:	self.action = None
		self.effects.append(effect.Effect(ent.x, ent.y, "reticle", link=ent))