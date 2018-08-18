import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from random import randint, choice

window = pyglet.window.Window(fullscreen = True, caption="Space Invaders")
window.set_location(400, 100)
fps_display = FPSDisplay(window)
fps_display.label.font_size = 50

main_batch = pyglet.graphics.Batch()

space = pyglet.image.load('bg.jpg')
actor_image = pyglet.image.load_animation('python.gif')

actor = pyglet.sprite.Sprite(img=actor_image)
bg_list = []

preloaded = False

@window.event

def on_mouse_motion(x, y, dx, dy):

    window.set_mouse_visible(False)

    window.clear()

    actor.x = x

    actor.y = y

@window.event
def on_draw():
    window.clear()
    if not preloaded:
        preload()
    for bg in bg_list:
        bg.draw()
    actor.draw()

@window.event

def preload():
    global preloaded
    for i in range(2):
        bg_list.append(pyglet.sprite.Sprite(space, x=i*1024, y=0))
    preloaded = True

def bg_move(dt):
    for bg in bg_list:
        bg.x -= 200*dt
        if bg.x <= -1024:
            bg_list.remove(bg)
            bg_list.append(pyglet.sprite.Sprite(space, x=1024.5, y=0))

def update(dt):

    bg_move(dt)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()
