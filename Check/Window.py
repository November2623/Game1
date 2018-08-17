import pyglet
import sys
import math
from random import randint,uniform
from pyglet.window import key
from pyglet.window import FPSDisplay
from random import randint, choice

window = pyglet.window.Window(width=1024, height=900, caption="Space Invaders", resizable=False)
window.set_location(400, 100)
fps_display = FPSDisplay(window)
fps_display.label.font_size = 50
A = 0
label = pyglet.text.Label(str(A))

batch = pyglet.graphics.Batch()

space = pyglet.image.load('bg.jpg')
actor_image = pyglet.image.load_animation('UFO.gif')
ghost_image = pyglet.image.load_animation('ghost.gif')
rocket_image = pyglet.image.load_animation('rocket.gif')
stone_image = pyglet.image.load('stone.png')
stone2_image = pyglet.image.load('stone2.png')
spaceship_image = pyglet.image.load('spaceship.png')
actor = pyglet.sprite.Sprite(img=actor_image)
sprite=[
        pyglet.sprite.Sprite(img =ghost_image, x=2000, y =randint(0,1024),batch = batch),
        pyglet.sprite.Sprite(img =rocket_image, x=2000, y =randint(0,1024),batch = batch),
        pyglet.sprite.Sprite(img=stone2_image, x=1024, y=randint(0,1024), batch=batch),]

sprite2=[
        pyglet.sprite.Sprite(img =stone_image, x=randint(0,1024), y =1024,batch = batch),
        pyglet.sprite.Sprite(img=spaceship_image, x=randint(0, 1024), y=1024, batch=batch)
        ]
bg_list = []
enemy_list = []

preloaded = False

def distance(a, b):
    return math.sqrt((a.x - b.x)** 2 + (a.y - b.y)** 2)

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
    batch.draw()
    label.draw()

def game_loop(_):
    label.text = str(int(label.text) + 1)
@window.event
def preload():
    global preloaded
    for i in range(2):
        bg_list.append(pyglet.sprite.Sprite(space, x=i*1024, y=0))
    preloaded = True

def bg_move(dt):
    for bg in bg_list:
        bg.x -= 195*dt
        if bg.x <= -1024:
            bg_list.remove(bg)
            bg_list.append(pyglet.sprite.Sprite(space, x=1024.3, y=0))

def update(dt):
    global A
    for i in sprite2:
        i.y -= 15
        i.x += uniform(-5,5)
        if i.y <0 or i.x<0:
            i.y = 1024
            i.x = randint(0,1024)
        if distance(actor, i) < ((actor.width/2 + i.width/2)-10) and distance(actor, i) < (actor.height/2 + i.height/2):
            sys.exit('GAME OVER')

    for i in sprite:
        i.x -= 20
        i.y += uniform(-2,2)
        if i.y <0 or i.x<0:
            i.x = 1024
            i.y = randint(0,1024)

        if distance(actor, i) < ((actor.width/2 + i.width/2)-10) and distance(actor, i) < (actor.height/2 + i.height/2):
            sys.exit('GAME OVER')

    bg_move(dt)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.clock.schedule(game_loop)
    pyglet.app.run()
