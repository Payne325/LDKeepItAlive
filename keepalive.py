import sys, platform, random
from src.gameobjs.player import Player
from src.gameobjs.asteroid import Asteroid
from src.Injan import Injan
from src.InjanStructures import Vector2, Vector3
from src.InjanKeycodes import *


print("Loading Engine...")

engine = Injan()
engine.Initialise()

print("Engine Loaded!")

print("Setting up Camera...")

camera = engine.CreateOrthographicCamera(-1.0, 1.0)
camera.Move(Vector3(-50, -50, 0))
cameraX = 0
cameraY = 0
cameraZ = 0

print("Camera Setup Complete!")

#print("Create Background...")
#todo Set background
#print("Background created!")

print("Creating Game Objects...")

player = Player(engine)

#temporary, just to test asteroids move correctly. spawner will construct this eventually
asteroid = Asteroid(engine, pos=Vector3(10.0, 15.0, 0.0), weight=4)

#todo create asteroid/exit portal spawner here

print("Game Objects created!")

print("Commence funtime...")

while engine.IsWindowOpen():
   dt = engine.Update()

   # todo: update spawner -> spawn new asteroid if needed

   # todo: update all asteroid positions
   asteroid.update_position(dt)

   player.handle_input()
   player.update_position(dt)

   # todo: implement the following
   # detect collisions 
      # if player and asteroid collide
         # player dies -> game ends/life lost (?)

      # if asteroid and ground collide
         # increase floor height
         
         # if floor height is tall enough
            # spawn exit portal

      # if asteroid and exit portal collide
         # delete asteroid

      # if player and exit portal collide
         # reset game
         # increment level counter
         # up difficulty somehow (more asteroids, faster asteroids, bigger 'tall enough' value?) 

   engine.Draw()
