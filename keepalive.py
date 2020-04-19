import sys, platform, random
from src.gameobjs.player import Player
from src.gameobjs.asteroid import Asteroid
from src.gameobjs.asteroid_spawner import AsteroidSpawner
from src.gameobjs.portal import Portal
from src.Injan import Injan
from src.InjanStructures import Vector2, Vector3
from src.InjanKeycodes import *
import pygame

def endgame_death():
   pygame.mixer.music.load("assets/sfx/death_music.wav")
   pygame.mixer.music.play(0)
   print("You died!")


print("Loading Engine...")

engine = Injan()
engine.Initialise()
engine.SetWindowSizeLimits(Vector2(800, 600), Vector2(800, 600))

pygame.init()

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

asteroid_spawner = AsteroidSpawner(engine)

#temporary, just to test asteroids move correctly. spawner will construct this eventually
#asteroid1 = Asteroid(engine, pos=Vector3(320.0, 500.0, 0.0), weight=128)
#asteroid2 = Asteroid(engine, pos=Vector3(320.0, 800.0, 0.0), weight=128)

falling_asteroids = []
stopped_asteroids = []
portal = Portal(engine, Vector3(320.0, 200, 0.0))

#todo create exit portal spawner here

print("Game Objects created!")

print("Commence funtime...")

floor_height = 0
player_alive = True
level_num = 1

while engine.IsWindowOpen() and player_alive:
   dt = engine.Update()

   # SPAWN NEW ASTEROIDS IF NEEDED
   spawned_asteroids = asteroid_spawner.Spawn(dt)
   for asteroid in spawned_asteroids:
      falling_asteroids.append(asteroid)

   # TODO: SPAWN EXIT PORTAL IF NEEDED

   # UPDATE POSITIONS
   for i, asteroid in enumerate(falling_asteroids):
       asteroid.update_position(dt)

   player.update_position(dt)

   # RESOLVE COLLISIONS
   # PLAYER AND FALLING ASTEROIDS
   for asteroid in falling_asteroids:
      if player.has_collided_with(asteroid):
         endgame_death()
         player_alive = False
         continue

   # PLAYER AND STOPPED ASTEROIDS
   for asteroid in stopped_asteroids:
      if player.has_collided_with(asteroid):
         player.place_next_to_collision(asteroid)

   # FALLING ASTEROIDS AND THE GROUND
   removal_indices = []
   for i, asteroid in enumerate(falling_asteroids):
      if not asteroid.can_hurt_player():
         stopped_asteroids.append(asteroid)
         removal_indices.append(i)

   for idx in reversed(removal_indices):
      falling_asteroids.pop(idx)

   # FALLING ASTEROIDS AND STOPPED ASTEROIDS
   removal_indices = []
   new_stopped_asteroids = []

   for i, falling_asteroid in enumerate(falling_asteroids):
      for stopped_asteroid in stopped_asteroids:
         if falling_asteroid.has_collided_with(stopped_asteroid):
            falling_asteroid.land_above(stopped_asteroid)
            removal_indices.append(i)
            new_stopped_asteroids.append(falling_asteroid)

   for asteroid in new_stopped_asteroids:
      stopped_asteroids.append(asteroid)

   for idx in reversed(removal_indices):
      falling_asteroids.pop(idx)

   

   # todo: if asteroid and exit portal collide
      # delete asteroid

   # END OF LEVEL COMPUTATION
   if portal.player_has_reached_portal(player):
      level_num += 1

      portal.playSFX()

      for asteroid in falling_asteroids:
         asteroid.stop_drawing()

      for asteroid in stopped_asteroids:
         asteroid.stop_drawing()

      falling_asteroids = []
      stopped_asteroids = []
      player.reset()

      asteroid_spawner.NextLevel()
      continue


   # UPDATE SPRITES AND DRAW
   player.update_sprite()

   for asteroid in falling_asteroids:
      asteroid.update_sprite()

   for asteroid in stopped_asteroids:
      asteroid.update_sprite()

   engine.Draw()

   # SFX
   player.playSFX()

   # this is kinda annoying but w/e fuck you its a game jam
   #for asteroid in stopped_asteroids:
      #asteroid.playSFX()
   

# Add some code to tidy up all memory if needed