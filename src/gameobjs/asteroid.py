from src.InjanStructures import *
from src.InjanKeycodes import *

class Asteroid:
   def __init__(self, engine, pos, weight):
      self.engine = engine
      self.pos = pos
      self.weight = weight
      self.floor_height = 0

      spriteID = engine.CreateTexture("assets/sprites/asteroid.png", Vector2(0, 0), Vector2(512, 512))
      self.sprite = engine.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,32), spriteID)
      self.sprite.SetDrawable(True)

   def update_floor_height(self, height):
      self.floor_height = height

   def update_position(self, dt):
      vel = Vector3(0.0, -self.weight * dt, 0.0)
      self.pos += vel

      if self.pos.y < self.floor_height:
         self.pos.y = self.floor_height
         self.sprite.SetDrawable(False)

      self.sprite.SetPosition(Vector3(self.pos.x * 32, self.pos.y * 32, 1.0))