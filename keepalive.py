import sys, platform, random
from src.gameobjs.player import Player
from src.gameobjs.asteroid import Asteroid
from src.gameobjs.asteroid_spawner import AsteroidSpawner
from src.gameobjs.portal import Portal
from src.Injan import Injan
from src.InjanStructures import Vector2, Vector3
from src.InjanKeycodes import *
import pygame

def death_func():
   deathSound = pygame.mixer.Sound("assets/sfx/death_music.wav")
   deathSound.play()
   while True:
      if not pygame.mixer.get_busy():
         break
         
   print("You died!")

num_lives = 3 # cant be less than 1

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

levelnumSpriteID0 = engine.CreateTexture("assets/sprites/LevelText-0.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID1 = engine.CreateTexture("assets/sprites/LevelText-1.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID2 = engine.CreateTexture("assets/sprites/LevelText-2.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID3 = engine.CreateTexture("assets/sprites/LevelText-3.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID4 = engine.CreateTexture("assets/sprites/LevelText-4.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID5 = engine.CreateTexture("assets/sprites/LevelText-5.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID6 = engine.CreateTexture("assets/sprites/LevelText-6.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID7 = engine.CreateTexture("assets/sprites/LevelText-7.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID8 = engine.CreateTexture("assets/sprites/LevelText-8.png", Vector2(0, 0), Vector2(32, 32))
levelnumSpriteID9 = engine.CreateTexture("assets/sprites/LevelText-9.png", Vector2(0, 0), Vector2(32, 32))

levelNumSpritePos = Vector3(750, 550, 0.0)

levelNumSprites = []

levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID0))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID1))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID2))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID3))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID4))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID5))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID6))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID7))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID8))
levelNumSprites.append(engine.CreateSprite(Vector3(750, 550, 0.0), Vector2(32 ,32), levelnumSpriteID9))

backgroundTexture = engine.CreateTexture("assets/sprites/background.png", Vector2(0, 0), Vector2(800, 600))
backgroundSprite  = engine.CreateSprite(Vector3(400, 300, 0.0), Vector2(800, 600), backgroundTexture)
backgroundSprite.SetDrawable(True)

for i, sprite in enumerate(levelNumSprites):
   if i == 1:
      sprite.SetDrawable(True)
   else:
      sprite.SetDrawable(False)

textSpriteID2 = engine.CreateTexture("assets/sprites/LivesText.png", Vector2(0, 0), Vector2(64, 32))
textSprite2 = engine.CreateSprite(Vector3(40, 550, 1.0), Vector2(64 ,32), textSpriteID2)
textSprite2.SetDrawable(True)

lifeSpriteID = engine.CreateTexture("assets/sprites/life1.png", Vector2(0, 0), Vector2(32, 32))
lifeSprites = []
for i in range(0, 3):
   xPos = (i * 33) + 89
   lifeSprites.append(engine.CreateSprite(Vector3(xPos, 550, 1.0), Vector2(32 ,32), lifeSpriteID))
   lifeSprites[i].SetDrawable(True)

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

pygame.mixer.music.load("assets/sfx/game_music.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

floor_height = 0
player_alive = True
level_num = 1

debug_mode = False
debug_skip = False
debug_key = False

while engine.IsWindowOpen() and player_alive:
   dt = engine.Update()


   # DEBUG
   if debug_mode:
      if engine.IsKeyDown(INJAN_KEY_S) and debug_key == False:
         debug_skip = True
         debug_key = True

      if engine.IsKeyDown(INJAN_KEY_S) == False:
         debug_key = False
         debug_skip = False

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
         
         num_lives -= 1
         lifeSprites[num_lives].SetDrawable(False)

         if num_lives == 0:
            player_alive = False
            death_func()

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

   # STOPPED ASTEROIDS AND PORTAL
   removal_indices = []
   for i, asteroid in enumerate(stopped_asteroids):
      if portal.has_collided_with(asteroid):
         removal_indices.append(i)
         asteroid.stop_drawing()
   
   for idx in reversed(removal_indices):
      stopped_asteroids.pop(idx)

   # END OF LEVEL COMPUTATION
   if portal.player_has_reached_portal(player) or debug_skip:
      debug_skip = False
      level_num += 1

      portal.playSFX()

      player.reset()

      for asteroid in falling_asteroids:
         asteroid.stop_drawing()

      for asteroid in stopped_asteroids:
         asteroid.stop_drawing()

      falling_asteroids = []
      stopped_asteroids = []
      portal.adjust_for_new_level()

      asteroid_spawner.NextLevel()

      for sprite in levelNumSprites:
         sprite.SetDrawable(False)

      level_num_str = str(level_num)

      characterCount = 0

      for i in level_num_str:
         val = int(i)

         charPos = Vector3(levelNumSpritePos.x, levelNumSpritePos.y, levelNumSpritePos.z)
         charPos.x += characterCount * 12

         levelNumSprites[val].SetPosition(charPos)
         levelNumSprites[val].SetDrawable(True)

         characterCount += 1

      continue


   # UPDATE SPRITES AND DRAW
   player.update_sprite()
   portal.update_sprite(dt)

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