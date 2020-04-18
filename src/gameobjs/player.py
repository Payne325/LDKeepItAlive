from src.InjanStructures import *
from src.InjanKeycodes import *

class Player:
   def __init__(self, engine):
      self.engine = engine
      self.pos = Vector3(0.0, 0.0, 0.0)

      spriteID = engine.CreateTexture("assets/sprites/player.png", Vector2(0, 0), Vector2(32, 64))
      self.sprite = engine.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,64), spriteID)
      self.sprite.SetDrawable(True)

      self.jump_force = 0
      self.weight = 64.0
      self.floor_height = 0
      self.jumping = False
      self.move_left = False
      self.move_right = False
      self.vel = Vector3(0.0, 0.0, 0.0)

      print("Player initialised")

   def update_floor_height(self, height):
      self.floor_height = height

   def update_sprite(self):
      self.sprite.SetPosition(Vector3(self.pos.x, self.pos.y, 1.0))

   def update_position(self, dt):
      speedModifier = 100 * dt
      self.vel = Vector3(0.0, 0.0, 0.0)

      if self.engine.IsKeyDown(INJAN_KEY_UP):
         if self.jumping == False:
            self.jumping = True
            self.jump_force = 640

      falling_force = 0
      if self.jumping:
         falling_force = self.jump_force * dt
         self.jump_force -= self.weight

      elif self.pos.y > self.floor_height: # if falling but not ending jump animation
         falling_force -= self.weight * dt

      self.vel.y = falling_force

      if self.engine.IsKeyDown(INJAN_KEY_LEFT):
         self.move_right = False
         self.move_left = True
         self.vel.x -= 1 * speedModifier

      if self.engine.IsKeyDown(INJAN_KEY_RIGHT):
         self.move_left = False
         self.move_right = True
         self.vel.x += 1 * speedModifier

      self.pos += self.vel

      # ensure we don't clip through the floor
      if self.pos.y <= self.floor_height:
         self.jumping = False
         self.pos.y = self.floor_height

   def has_collided_with(self, asteroid):
      asteroidPos = asteroid.get_position()

      diffX = abs(self.pos.x - asteroidPos.x)
      diffY = abs(self.pos.y - asteroidPos.y)

      return diffX < 30 and diffY < 30

   def place_next_to_collision(self, asteroid):
      vecBetween = self.pos - asteroid.get_position()
      #vecBetween = vecBetween.get_normalised()

      self.pos += vecBetween