from pygame import mixer
from src.gameobjs.player import Player
from src.InjanStructures import Vector2, Vector3
import time
from random import seed, uniform

class Portal:
   def __init__(self, engine):
      self.levelNum = 1
      self.pos = self.__generate_random_position()
      self.timer = 0
      self.collidedWithPlayer = False
      self.levelEndSFX = mixer.Sound("assets/sfx/level_up.wav")
      self.playedSFX = False
      spriteID = engine.CreateTexture("assets/sprites/portal.png", Vector2(0, 0), Vector2(32, 32))
      self.sprite = engine.CreateSprite(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0), Vector2(32 ,32), spriteID)
      self.sprite.SetDrawable(True)

      spriteID2 = engine.CreateTexture("assets/sprites/portal2.png", Vector2(0, 0), Vector2(32, 32))
      self.sprite2 = engine.CreateSprite(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0), Vector2(32 ,32), spriteID2)
      self.sprite2.SetDrawable(True)

   def __generate_random_position(self):
      seedVal = time.time_ns()
      seed(seedVal)
      xPos = uniform(0.0, 750.0)

      yUpperBound = min(500, (self.levelNum * .2) * 500)
      yLowerBound = yUpperBound * .5
      yPos = uniform(yLowerBound, yUpperBound)

      return Vector3(xPos, yPos, 0.0)

   def player_has_reached_portal(self, player):
      playerPos = player.get_position()

      diffX = abs(self.pos.x - playerPos.x)
      diffY = abs(self.pos.y - playerPos.y)

      self.collidedWithPlayer = diffX < 30 and diffY < 30
      return self.collidedWithPlayer

   def adjust_for_new_level(self):
      self.levelNum += 1
      self.pos = self.__generate_random_position()
      self.sprite.SetPosition(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0))
      self.sprite2.SetPosition(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0))

   def playSFX(self):
      self.levelEndSFX.play()
      self.playedSFX = True

   def has_collided_with(self, asteroid):
      asteroidPos = asteroid.get_position()
      
      diffX = abs(self.pos.x - asteroidPos.x)
      diffY = abs(self.pos.y - asteroidPos.y)

      return diffX < 30 and diffY < 30

   def update_sprite(self, dt):
      self.timer += dt

      if self.timer <  0.5:
         self.sprite.SetDrawable(True)
         self.sprite2.SetDrawable(False)
      elif  self.timer <  1:
         self.sprite.SetDrawable(False)
         self.sprite2.SetDrawable(True)
      else:
         self.timer = 0