from pyglet.window import key

SPAWN_RATE = 10.0
BELT_SPEED = 16.0
INTERACTABLE_POINT = 13.0
INTERACTABLE_TIME = 10.0

SPOT_1 = key.I
SPOT_2 = key.J
SPOT_3 = key.K
SPOT_4 = key.L

ACTIONS = {
	key.I:(key.G,key.H,key.F),
	key.J:(key.F, key.F, key.F, key.H, key.H, key.H),
	key.K:(key.F, key.G, key.H, key.F, key.G, key.H, key.F, key.G, key.H),
	key.L:(key.G, key.G, key.G, key.F, key.H)
}

KEYS = {key.F:"prompt_f", key.H:"prompt_h", key.G:"prompt_g"}
LETTERS = ("prompt_f", "prompt_g", "prompt_h")
LETTERS2 = ("prompt_i", "prompt_j", "prompt_k", "prompt_l")