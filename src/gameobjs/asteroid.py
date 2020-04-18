from src.InjanStructures import *
from src.InjanKeycodes import *

class Asteroid:
   def __init__(self, engine, pos, weight):
      self.engine = engine
      self.pos = pos
      self.weight = weight
      self.floor_height = 0
      self.falling = True

      falling_spriteID = engine.CreateTexture("assets/sprites/asteroid.png", Vector2(0, 0), Vector2(512, 512))
      self.falling_sprite = engine.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,32), falling_spriteID)
      self.falling_sprite.SetDrawable(True)

      stopped_spriteID = engine.CreateTexture("assets/sprites/asteroid_broken.png", Vector2(0, 0), Vector2(512, 512))
      self.stopped_sprite = engine.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,32), stopped_spriteID)
      self.stopped_sprite.SetDrawable(False)

   def update_floor_height(self, height):
      self.floor_height = height

   def update_position(self, dt):
      if self.falling:
         vel = Vector3(0.0, -self.weight * dt, 0.0)
         self.pos += vel

         if self.pos.y < self.floor_height:
            self.pos.y = self.floor_height
            self.falling = False    

   def update_sprite(self):
      if self.falling:
         self.falling_sprite.SetPosition(Vector3(self.pos.x * 32, self.pos.y * 32, 1.0))
      else:
         self.falling_sprite.SetDrawable(False)
         self.stopped_sprite.SetDrawable(True)
         self.stopped_sprite.SetPosition(Vector3(self.pos.x * 32, self.pos.y * 32, 1.0))

   def can_hurt_player(self):
      return self.falling

   def get_position(self):
      return self.pos
