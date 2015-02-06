import pyglet
import resources
import core
import vars
import childobject
import effect
import random
class Entity(pyglet.sprite.Sprite):
	def __init__(self, x, y, entity_type):
		graphic = resources.get_graphic(entity_type)
		super(Entity, self).__init__(img=graphic, x=x, y=y, batch=core.main_batch)
		self.entity_type = entity_type
		self.life = 0.0
		self.active = True
		self.interactable = False
		self.processed = False
		self.status = None
		self.falling = False
		self.children = {
			vars.SPOT_1:None,
			vars.SPOT_2:None,
			vars.SPOT_3:None,
			vars.SPOT_4:None
		}
		self.child_offsets = {
			vars.SPOT_1:(28, 0),
			vars.SPOT_2:(0, 8),
			vars.SPOT_3:(-12, -19),
			vars.SPOT_4:(10, -19)
		}
		self.key_effect = -1
	
	def update(self, dt):
		self.life += dt
		if self.entity_type == "belt_item_base" or self.entity_type == "belt_item_broken":
			self.x += vars.BELT_SPEED * dt
			if self.falling:
				self.y -= vars.BELT_SPEED * dt * 2.0
			if self.life > vars.INTERACTABLE_POINT and self.life < vars.INTERACTABLE_POINT + vars.INTERACTABLE_TIME:
				if self.interactable and core.manager.action:
					self.update_key(core.manager.action, core.manager.action_current_key)
				else:
					self.key_effect = -1
				if not self.interactable and not self.status:
					core.manager.set_interactable(self)
					self.interactable = True
			else:
				if self.life > vars.INTERACTABLE_POINT + vars.INTERACTABLE_TIME +.5 and not self.status =="accepted" and not self.falling:
					resources.sfxs["ugh1"].play()
					core.manager.bonus = 1.0
					self.falling = True
				if self.interactable:
					self.interactable = False
			if self.life > 30.0:
				if not self.status == "accepted":
					resources.sfxs["kling"].play()
				else:
					resources.sfxs["yes1"].play()
					bonus = 0.0
					for key, child in self.children.iteritems():
						if not child is None:
							if child.rotation == 0:
								bonus += .4
							else:
								bonus -= .2
						else:
							bonus -= .4
					core.manager.bonus += bonus
					if core.manager.bonus < 0.0: core.manager.bonus =0.0 
					core.manager.wage += core.manager.base_wage * core.manager.bonus
					
				self.children = {
					vars.SPOT_1:None,
					vars.SPOT_2:None,
					vars.SPOT_3:None,
					vars.SPOT_4:None
				}
				self.active = False
		for key, child in self.children.iteritems():
			if not child is None:
				child.update(dt)
				
	def get_position(self, child):
		ofx, ofy = self.child_offsets[child]
		position = (self.x + ofx, self.y + ofy)
		return position
		
	def update_position(self, dx, dy):
		self.x += dx
		self.y += dy
		if self.interactable:
			if core.manager.action: core.manager.action = None
			self.interactable = False
			if dy > 0:
				self.status = "accepted"
			else:
				self.status = "discarded"
	
	def do_action(self, key, last=False):
		if last:
			self.children[key].rotation = 0
			self.children[key].interactable = False
		else: 
			core.manager.play_sound()
			self.children[key].rotation = ((random.random() / 2.0) - .25)  * 360
		
	def add_child(self, key):
		if not self.children[key]:
			x = self.x + self.child_offsets[key][0]
			y = self.y + self.child_offsets[key][1]
			self.children[key] = childobject.ChildObject(x, y, self, key)
			self.update_key(key, 0)
			return key
		else:
			return None
			
	def update_key(self, action, current):
		if self.key_effect == current:
			return
		else:
			self.key_effect = current
			core.manager.effects.append(effect.Effect(self.x, self.y, vars.KEYS[vars.ACTIONS[action][current]], self))
		