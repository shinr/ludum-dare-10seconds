# resources

import sys
import pyglet


default_img = "default"

graphic_files = {default_img:"default.png", 
						"belt_item_base":"whole_item.png", 
						"belt_item_broken":"broken_item.png",
						"reticle":"reticle.png",
						"part_antenna":"part_antenna.png",
						"part_screen":"part_screen.png",
						"part_dial":"part_dial.png",
						"part_speaker":"part_speaker.png",
						"effect_ret":"effect_ret.png",
						"info_text":"infotext.png",
						"prompt_h":"prompt_h.png",
						"prompt_g":"prompt_g.png",
						"prompt_f":"prompt_f.png",
						"prompt_i":"prompt_i.png",
						"prompt_j":"prompt_j.png",
						"prompt_k":"prompt_k.png",
						"prompt_l":"prompt_l.png",
						"background":"background.png",
						"conveyor":"conveyor_map.png",
						"cheat":"cheat.png",
						"factory_logo":"factory.png",
						"partsbox":"partsbox.png"}
						
sound_files = {
	"ugh1":"ugh1.wav", 
	"ugh2":"ugh2.wav", 
	"yes1":"yes1.wav", 
	"drill":"drill.wav", 
	"bang":"bang.wav", 
	"bang2":"bang2.wav", 
	"bang3":"bang3.wav", 
	"bang4":"bang4.wav",
	"kling":"kling.wav"
}

music = None
graphics = {}
sfxs = {}
path_ready = False

def get_graphic(graphic=default_img):
	if not path_ready:
		print "path not ready"
		sys.exit(1)
	if not graphic in graphics.keys():
		return graphics[default_img]
	return graphics[graphic]

def load_path(*path):
	global path_ready
	pyglet.resource.path.extend(path)
	pyglet.resource.reindex()
	path_ready = True
	
def load_graphics():
	if not path_ready:
		return
	for key, item in graphic_files.iteritems():
		if not key in graphics.keys():
			graphics[key] = pyglet.resource.image(item)
			graphics[key].anchor_x = graphics[key].width // 2
			graphics[key].anchor_y = graphics[key].height // 2
			
def load_sounds():
	global music
	if not path_ready:
		return
	music = pyglet.resource.media('beats.wav')
	for key, item in sound_files.iteritems():
		if not key in sfxs.keys():
			sfxs[key] = pyglet.resource.media(item, streaming=False)
			
