import pyglet
import core

core.init()


if __name__ == "__main__":
	pyglet.clock.schedule_interval(core.game_window.update, 1/120.0)
	pyglet.app.run()