from src.InjanStructures import *

class Player:
   def __init__(self, engine):
      self.engine = engine
      self.pos = Vector3(0.0, 0.0, 0.0)
      self.vel = Vector3(0.0, 0.0, 0.0)

      spriteID = engine.CreateTexture("assets/sprites/player.png", Vector2(0, 0), Vector2(512, 512))
      self.playerSprite = engine.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,32), spriteID)

      print("Player initialised")

   def set_vel(self, vel):
      self.vel = vel
      self.pos += vel
      self.playerSprite.SetPosition(Vector3(self.pos.x * 32, self.pos.y * 32, 1.0))