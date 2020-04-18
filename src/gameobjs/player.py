from src.InjanStructures import *
from src.InjanKeycodes import *

class Player:
   def __init__(self, engine):
      self.engine = engine
      self.pos = Vector3(0.0, 0.0, 0.0)

      spriteID = engine.CreateTexture("assets/sprites/player.png", Vector2(0, 0), Vector2(512, 512))
      self.sprite = engine.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,32), spriteID)
      self.sprite.SetDrawable(True)

      self.jump_force = 0
      self.weight = 2.0
      self.floor_height = 0
      self.jumping = False
      self.move_left = False
      self.move_right = False

      print("Player initialised")

   def update_floor_height(self, height):
      self.floor_height = height

   def update_sprite(self):
      self.sprite.SetPosition(Vector3(self.pos.x * 32, self.pos.y * 32, 1.0))

   def update_position(self, dt):
      speedModifier = 10 * dt
      vel = Vector3(0.0, 0.0, 0.0)

      if self.engine.IsKeyDown(INJAN_KEY_UP):
         if self.jumping == False:
            self.jumping = True
            self.jump_force = 20

      if self.jumping:
         total_jump_force = self.jump_force * dt
         self.jump_force -= self.weight

         vel.y = total_jump_force

      if self.engine.IsKeyDown(INJAN_KEY_LEFT):
         self.move_right = False
         self.move_left = True
         vel.x -= 1 * speedModifier

      if self.engine.IsKeyDown(INJAN_KEY_RIGHT):
         self.move_left = False
         self.move_right = True
         vel.x += 1 * speedModifier

      self.pos += vel

      if self.jumping and self.pos.y <= self.floor_height:
         self.jumping = False
         self.pos.y = self.floor_height

   def has_collided_with(self, asteroid):
      asteroidPos = asteroid.get_position()

      diffX = abs(self.pos.x - asteroidPos.x)
      diffY = abs(self.pos.y - asteroidPos.y)

      return diffX < 0.5 and diffY < 0.5