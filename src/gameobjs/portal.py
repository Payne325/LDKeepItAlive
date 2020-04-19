from pygame import mixer
from src.gameobjs.player import Player
from src.InjanStructures import Vector2, Vector3
import time
from random import seed, uniform

class Portal:
   def __init__(self, engine):
      self.pos = self.__generate_random_position()
      self.collidedWithPlayer = False
      self.levelEndSFX = mixer.Sound("assets/sfx/level_up.wav")
      self.playedSFX = False

      spriteID = engine.CreateTexture("assets/sprites/portal.png", Vector2(0, 0), Vector2(32, 32))
      self.sprite = engine.CreateSprite(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0), Vector2(32 ,32), spriteID)
      self.sprite.SetDrawable(True)

   def __generate_random_position(self):
      seedVal = time.time_ns()
      seed(seedVal)
      xPos = uniform(0.0, 750.0)
      yPos = uniform(50.0, 500.0)

      return Vector3(xPos, yPos, 0.0)

   def player_has_reached_portal(self, player):
      playerPos = player.get_position()

      diffX = abs(self.pos.x - playerPos.x)
      diffY = abs(self.pos.y - playerPos.y)

      self.collidedWithPlayer = diffX < 30 and diffY < 30
      return self.collidedWithPlayer

   def move_to_random_position(self):
      self.pos = self.__generate_random_position()
      self.sprite.SetPosition(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0))

   def playSFX(self):
      self.levelEndSFX.play()
      self.playedSFX = True