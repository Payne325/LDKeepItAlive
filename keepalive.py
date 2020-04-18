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
camera.Move(Vector3(0, 0, 0))
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
asteroid1 = Asteroid(engine, pos=Vector3(320.0, 500.0, 0.0), weight=128)
asteroid2 = Asteroid(engine, pos=Vector3(320.0, 800.0, 0.0), weight=128)

falling_asteroids = [asteroid1, asteroid2]
stopped_asteroids = []

#todo create asteroid/exit portal spawner here

print("Game Objects created!")

print("Commence funtime...")

floor_height = 0
player_alive = True

while engine.IsWindowOpen() and player_alive:
   dt = engine.Update()

   # todo: update spawner -> spawn new asteroid if needed
   new_stopped_asteroids = []
   for i, asteroid in enumerate(falling_asteroids):
      asteroid.update_position(dt)
      
      if not asteroid.can_hurt_player():
         new_stopped_asteroids.append(i)

   for i in reversed(new_stopped_asteroids):
      stopped_asteroids.append(falling_asteroids[i])
      falling_asteroids.pop(i)

   

   new_stopped_asteroids = []
   for falling_asteroid in falling_asteroids:
      for i, stopped_asteroid in enumerate(stopped_asteroids):
         if falling_asteroid.has_collided_with(stopped_asteroid):
            falling_asteroid.land_above(stopped_asteroid)
            new_stopped_asteroids.append(i)

   for i in reversed(new_stopped_asteroids):
      stopped_asteroids.append(falling_asteroids[i])
      falling_asteroids.pop(i)

   player.update_position(dt)
   
   for asteroid in falling_asteroids:
      if player.has_collided_with(asteroid):
         print("You died!")
         player_alive = False
         continue
   
   for asteroid in stopped_asteroids:
      if player.has_collided_with(asteroid):
         player.place_next_to_collision(asteroid)

   # if asteroid and exit portal collide
      # delete asteroid

   # if player and exit portal collide
      # reset game
      # increment level counter
      # up difficulty somehow (more asteroids, faster asteroids, bigger 'tall enough' value?) 

   player.update_sprite()
   asteroid1.update_sprite()
   asteroid2.update_sprite()
   engine.Draw()

# Add some code to tidy up all memory if needed