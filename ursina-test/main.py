from ursina import *

# create a window
app = Ursina()

# most things in ursina are Entities. An Entity is a thing you place in the world.
# you can think of them as GameObjects in Unity or Actors in Unreal.
# the first paramenter tells us the Entity's model will be a 3d-model called 'cube'.
# ursina includes some basic models like 'cube', 'sphere' and 'quad'.

# the next parameter tells us the model's color should be orange.

# 'scale_y=2' tells us how big the entity should be in the vertical axis, how tall it should be.
# in ursina, positive x is right, positive y is up, and positive z is forward.

playerOne = Entity(model='cube', color=color.blue, scale_y=2)
playerTwo = Entity(model='cube', color=color.red, scale_y=2)
# create a function called 'update'.
# this will automatically get called by the engine every frame.

def updateOne():
    playerOne.x -= held_keys['a'] * time.dt
    playerOne.x += held_keys['d'] * time.dt

def updateTwo(key):    
    if key == 'left arrow':
        playerTwo.x += held_keys[key.toString()] * time.dt

    if key == 'right arrow':
        playerTwo.x -= held_keys[key] * time.dt

# this part will make the player move left or right based on our input.
# to check which keys are held down, we can check the held_keys dictionary.
# 0 means not pressed and 1 means pressed.
# time.dt is simply the time since the last frame. by multiplying with this, the
# player will move at the same speed regardless of how fast the game runs.

def input(key):
    if key == 'space':
        playerOne.y += 1
        invoke(setattr, playerOne, 'y', playerOne.y-1, delay=.25)

# start running the game
app.run()