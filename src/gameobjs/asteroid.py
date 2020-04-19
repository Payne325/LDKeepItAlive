from src.InjanStructures import *
from src.InjanKeycodes import *
from pygame import mixer

class Asteroid:
   def __init__(self, engine, pos, weight):
      self.engine = engine
      self.pos = pos
      self.weight = weight
      self.floor_height = 0
      self.falling = True
      self.timer = 0

      self.explosionSFX = mixer.Sound("assets/sfx/Explosion.wav")
      self.playedSFX = False

      self.spriteFlip = True
      falling_spriteID1 = engine.CreateTexture("assets/sprites/flame-asteroid-1.png", Vector2(0, 0), Vector2(32, 32))
      self.falling_sprite1 = engine.CreateSprite(Vector3(0, 16, 1.0), Vector2(32 ,32), falling_spriteID1)
      self.falling_sprite1.SetDrawable(True)

      falling_spriteID2 = engine.CreateTexture("assets/sprites/flame-asteroid-2.png", Vector2(0, 0), Vector2(32, 32))
      self.falling_sprite2 = engine.CreateSprite(Vector3(0, 16, 1.0), Vector2(32 ,32), falling_spriteID2)
      self.falling_sprite2.SetDrawable(False)

      stopped_spriteID = engine.CreateTexture("assets/sprites/asteroid_broken.png", Vector2(0, 0), Vector2(32, 32))
      self.stopped_sprite = engine.CreateSprite(Vector3(0, 16, 1.0), Vector2(32 ,32), stopped_spriteID)
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

   def update_sprite(self, dt):
      self.timer += dt
      if self.falling:
         if self.timer > .25:
            self.spriteFlip = not self.spriteFlip
            self.timer = 0

         if self.spriteFlip:
            self.falling_sprite1.SetPosition(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0))
            self.falling_sprite1.SetDrawable(True)
            self.falling_sprite2.SetDrawable(False)
         else:
            self.falling_sprite2.SetPosition(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0))
            self.falling_sprite2.SetDrawable(True)
            self.falling_sprite1.SetDrawable(False)
      else:
         self.falling_sprite1.SetDrawable(False)
         self.falling_sprite2.SetDrawable(False)
         self.stopped_sprite.SetDrawable(True)
         self.stopped_sprite.SetPosition(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0))

   def stop_drawing(self):
      self.falling_sprite1.SetDrawable(False)
      self.falling_sprite2.SetDrawable(False)
      self.stopped_sprite.SetDrawable(False)

   def can_hurt_player(self):
      return self.falling

   def get_position(self):
      return self.pos

   def has_collided_with(self, asteroid):
      asteroidPos = asteroid.get_position()
      
      diffX = abs(self.pos.x - asteroidPos.x)
      diffY = abs(self.pos.y - asteroidPos.y)

      return diffX < 30 and diffY < 30

   def land_above(self, asteroid):
      self.pos.y = asteroid.pos.y + 32
      self.falling = False

   def playSFX(self):
      if not self.falling and not self.playedSFX:
         self.explosionSFX.play()
         self.playedSFX = True

