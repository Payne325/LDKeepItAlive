import sys, platform, random
from src.gameobjs.player import Player
from src.gameobjs.asteroid import Asteroid
from src.gameobjs.asteroid_spawner import AsteroidSpawner
from src.gameobjs.portal import Portal
from src.Injan import Injan
from src.InjanStructures import Vector2, Vector3
from src.InjanKeycodes import *
import pygame

print("Loading Engine...")

engine = Injan()
engine.Initialise()
engine.SetWindowSizeLimits(Vector2(800, 600), Vector2(800, 600))

pygame.init()

print("Engine Loaded!")

print("Creating overlay...")
textSpriteID = engine.CreateTexture("assets/sprites/LevelText.png", Vector2(0, 0), Vector2(64, 32))
textSprite = engine.CreateSprite(Vector3(705, 550, 1.0), Vector2(64 ,32), textSpriteID)
textSprite.SetDrawable(True)

levelnumSpriteID1 = engine.CreateTexture("assets/sprites/LevelText-1.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID2 = engine.CreateTexture("assets/sprites/LevelText-2.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID3 = engine.CreateTexture("assets/sprites/LevelText-3.png", Vector2(0, 0), Vector2(32, 32))

levelNumSprites = []

levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID1))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID2))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID3))

for i, sprite in enumerate(levelNumSprites):
   if i == 0:
      sprite.SetDrawable(True)
   else:
      sprite.SetDrawable(False)

print("Overlay created!")

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

falling_asteroids = []
stopped_asteroids = []
portal = Portal(engine)

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

   # UPDATE POSITIONS
   for i, asteroid in enumerate(falling_asteroids):
       asteroid.update_position(dt)

   player.update_position(dt)

   # RESOLVE COLLISIONS
   # PLAYER AND FALLING ASTEROIDS -> DEATH
   for asteroid in falling_asteroids:
      if player.has_collided_with(asteroid):
         deathSound = pygame.mixer.Sound("assets/sfx/death_music.wav")
         deathSound.play()
         while True:
            if not pygame.mixer.get_busy():
               print("Broke!")
               break
         
         print("You died!")
         player_alive = False
         player.reset()

         for asteroid in falling_asteroids:
            asteroid.stop_drawing()

         for asteroid in stopped_asteroids:
            asteroid.stop_drawing()

         falling_asteroids = []
         stopped_asteroids = []

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

   

   # todo: if stopped asteroid and exit portal collide
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
      portal.move_to_random_position()

      asteroid_spawner.NextLevel()

      for i, sprite in enumerate(levelNumSprites):
         val = min(level_num, 3)

         if i == val - 1:
            sprite.SetDrawable(True)
         else:
            sprite.SetDrawable(False)

      continue


   # UPDATE SPRITES AND DRAW
   player.update_sprite()

   for asteroid in falling_asteroids:
      asteroid.update_sprite(dt)

   for asteroid in stopped_asteroids:
      asteroid.update_sprite(dt)

   engine.Draw()

   # SFX
   player.playSFX()

   # this is kinda annoying but w/e fuck you its a game jam
   #for asteroid in stopped_asteroids:
      #asteroid.playSFX()
   

# Add some code to tidy up all memory if needed